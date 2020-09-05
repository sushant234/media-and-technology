from django.db import models

# Create your models here.
class services(models.Model):
    heading = models.CharField(max_length=400)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    post = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)


class blogg(models.Model):
    heading = models.CharField(max_length=400)
    img = models.ImageField(upload_to='pics')
    summary = models.CharField(max_length=400)
    desc = models.TextField()
    writer = models.CharField(max_length=400, default='VNM')
    post = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

class employee(models.Model):
    img = models.ImageField(upload_to='pics')
    f_name = models.CharField(max_length=70)
    l_name = models.CharField(max_length=70)
    position = models.CharField(max_length=100)
    twitter = models.CharField(max_length=200, default='https://twitter.com/')
    fb = models.CharField(max_length=200, default='https://www.facebook.com/')
    google = models.CharField(max_length=200, default='https://plus.google.com/')
    linkdn = models.CharField(max_length=200, default='"https://www.linkedin.com/')
