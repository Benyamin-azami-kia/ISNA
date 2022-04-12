from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    id=models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    is_published=models.BooleanField(default=False)
    body=models.TextField()
    photo=models.ImageField(upload_to='images', null=True, blank=True)
    reporter=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publish=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='New'


class Review(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=250)
    body=models.TextField()
    created=models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name