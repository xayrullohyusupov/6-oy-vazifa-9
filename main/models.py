from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def last_img(self):
        return BlogImg.objects.filter(blog__id = self.id).last().img


class BlogImg(models.Model):
    img = models.ImageField(upload_to='blog-img/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

class BlogVideo(models.Model):
    video = models.FileField(upload_to='blog-vidos/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} -> {self.blog.title}"

class Networks(models.Model):
    title = models.URLField()
    icon = models.TextField(max_length=18)
    text = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Blogicon(models.Model):
    title = models.URLField()
    icon = models.TextField(max_length=15)

    def __str__(self):
        return self.title


class Blog_icon_2(models.Model):
    title = models.URLField()
    icon = models.TextField(max_length=25)

    def __str__(self):
        return self.title

class Blog_icon_3(models.Model):
    title = models.URLField()
    icon = models.TextField(max_length=20)
    text = models.CharField(max_length=18)

    def __str__(self):
        return self.title