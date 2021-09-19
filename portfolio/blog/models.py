# Create your models here.
from django.db import models


# 注意每次更改后执行加载模型
# 1. python manage.py makemigrations
# 加载数据库
# 2. python manage.py migrate
# 创建管理员
# 3.python manage.py createsuperuser


class Post(models.Model):
    blog_title = models.CharField('title', max_length=200)
    blog_body = models.TextField('body')
    blog_time = models.DateTimeField('time')

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
