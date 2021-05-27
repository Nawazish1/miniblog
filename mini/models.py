from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    desc = models.TextField()


class Image(models.Model):
    photo=models.ImageField(upload_to='myimage')
    date=models.DateTimeField(auto_now_add=True)