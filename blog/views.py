from xml.etree.ElementTree import Comment
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm


def get_date(post):
    return post['date']

# Create your views here.


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


class AllPostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'


class PostDetailsView(View):
    template_name = 'blog/post-details.html'
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, 'blog/post-details.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-details', args=[slug]))

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request, 'blog/post-details.html', context)
