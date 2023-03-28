from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Max
from django.shortcuts import render
from django.views import View

from posts.forms import CommentForm


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('search')
        form = CommentForm
        context = {}
        if query:
            users = get_user_model().objects.filter(Q(username__icontains=query) | Q(email__icontains=query) | Q(
                first_name__icontains=query))
            context = {
                'user_search': users
            }
        else:
            users = get_user_model().objects.filter(Q(subscriptions=request.user.pk))
            users = users.annotate(posts_sort=Max('posts')).order_by('-posts_sort')
            context = {
                'user_obj': users,
                'form': form
            }
        return render(request, 'index.html', context=context)
