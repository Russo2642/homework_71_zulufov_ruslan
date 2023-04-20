from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from posts.forms import CommentForm
from posts.forms import PostForm
from posts.models import Comment
from posts.models import Like
from posts.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDetailView(FormMixin, DetailView):
    template_name = 'posts/post_detail.html'
    model = Post
    form_class = CommentForm


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
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        old_like = Like.objects.filter(user=request.user, post=post)
        if old_like:
            like = Like.objects.get(user=request.user, post=post)
            if request.user == like.user:
                like.delete()
        else:
            new_like = Like(user=request.user, post=post)
            new_like.save()
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


class DeleteComments(UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post_id})

    def test_func(self):
        return self.request.user == self.get_object().author
