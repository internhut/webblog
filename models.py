from django.db import models

# Create your models here.

# Category Model

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)
    imageURL = models.CharField(max_length=200)
    addDate = models.DateTimeField(auto_now_add=True, null=True)


class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)
    imageURL = models.CharField(max_length=200)
    videoURL = models.CharField(max_length=200)
    pubDate = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)