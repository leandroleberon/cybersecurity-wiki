from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='article.jpg', upload_to='article_pics')
    content = models.TextField()
    citation = models.TextField(default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})