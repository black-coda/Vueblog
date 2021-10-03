from django.shortcuts import render
from . import models
# Create your views here.

def post_list(request):
    posts = models.Post.objects.filter(status = 'published') #filter 
    return render(request, 'post_list.html', {'post':post_list} )