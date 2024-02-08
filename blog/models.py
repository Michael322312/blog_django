from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=63)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    text = models.TextField()
    author = models.CharField(max_length=63)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author