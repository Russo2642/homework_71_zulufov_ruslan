from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from posts.forms import CommentForm
from posts.forms import PostForm
from posts.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.author = request.user
    #         form.save()
    #     return reverse('profile', kwargs={'pk': str(request.user.pk)})


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post


class PostUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'posts/post_update.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.author_id})

    def test_func(self):
        return self.get_object().author == self.request.user


class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)
        return redirect(request.META.get('HTTP_REFERER'))


class AddComments(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.author = request.user
            form.save()
        return redirect(request.META.get('HTTP_REFERER'))
