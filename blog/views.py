from django.shortcuts import render, get_object_or_404
from .models import Post


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/posts.html', {
        'posts': all_posts
    })


def post_details(request, slug):
    target_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-details.html', {'post': target_post,
                                                      'tags': target_post.tags.all()
                                                      })
