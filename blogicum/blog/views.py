from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone



def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)



def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.all().filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
            pk=post_id
        )
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_id):
    category = get_object_or_404(Category, slug=category_id)

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category.html', context)
