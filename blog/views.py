from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_queryset(self):
        self.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.post

    def form_valid(self, form):
        form.instance.post = self.get_queryset()
        form.instance.author = 'John Smith'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.id})