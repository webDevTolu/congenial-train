from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    # pagination with 5 post per page
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post,
                             publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})
