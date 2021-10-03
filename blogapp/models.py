from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, time
from django.urls import reverse
# Create your models here.
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'published')


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique_for_date='publish',)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post' )
    article = models.TextField(max_length=500000)

    publish = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() #default manager
    pulished = PublishedManager()  #custom manager
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title   


    def get_absolute_url(self):
        return reverse('post_details', args=[self.slug])

