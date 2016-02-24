from django.db import models

#
# Post model, takes on structure from http://jsonplaceholder.typicode.com/posts
#
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    body = models.TextField()

#
# Post model, takes on structure from http://jsonplaceholder.typicode.com/comments
#
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    body = models.TextField()

