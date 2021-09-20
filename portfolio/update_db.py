import markdown
import os
import os.path as osp
from django.shortcuts import render, get_object_or_404

from blog.models import Post

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

if __name__ == '__main__':
    update_blogs_from_markdown()
