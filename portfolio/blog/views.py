import markdown
import os
import os.path as osp
from django.shortcuts import render, get_object_or_404

from .models import Post


def blog_index(request):
    blogs = Post.objects.all()
    return render(request, 'blog/index.html', {
        'blogs': blogs
    })


def detail(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    config = {
        'codehilite': {
            'use_pygments': False,
            'css_class': 'prettyprint linenums',
        }
    }
    blog.blog_body = markdown.markdown(blog.blog_body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    print("Body")
    print(os.getcwd())
    print(blog.blog_body)
    return render(request, 'blog/detail.html', {
        'blog': blog
    })
