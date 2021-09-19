import markdown
import os
import os.path as osp
from django.shortcuts import render, get_object_or_404

from .models import Post

def read_blog_title_and_body(filename, path):

    blog_id = int(filename.split('-')[0])
    blog = Post.objects.get(id=blog_id)
    # blog = get_object_or_404(Post, pk=blog_id)
    if osp.getmtime(osp.join(path, filename)) != blog.blog_time.timestamp():
        print(f"Updating blog {blog_id} ...")
        with open(osp.join(path, filename), "r", encoding="utf-8") as f:
            content = f.readlines()
            blog.update(blog_body=content)
            # blog.blog_body = content

def update_blogs_from_markdown():
    path = osp.join('static', 'markdown')
    filenames = os.listdir(path)
    for filename in filenames:
        read_blog_title_and_body(filename, path)


def blog_index(request):
    update_blogs_from_markdown()
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
