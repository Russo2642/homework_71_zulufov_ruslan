from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from posts.forms import PostForm
from posts.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post
