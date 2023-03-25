from accounts.forms import CustomUserCreationForm
from accounts.forms import LoginForm
from accounts.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.models import Account


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, 'Некорректные данные')
            return redirect('index')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if not user:
            messages.error(request, 'Пользователь не найден')
            return redirect('login')
        login(request, user)
        messages.success(request, 'Добро пожаловать')
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('index')


def logout_view(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    logout(request)
    return redirect(return_path)


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object() == self.request.user


def follow(request, pk):
    user_object = Account.object.get(pk=pk)
    current_user = Account.object.get(username=request.user.username)
    following = user_object.subscriptions.all()
    if pk != current_user.pk:
        if current_user in following:
            user_object.subscriptions.remove(current_user.id)
        else:
            user_object.subscriptions.add(current_user.id)
    return redirect(request.META.get('HTTP_REFERER'))
