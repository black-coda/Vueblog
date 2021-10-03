from django.shortcuts import render
from . import models
# Create your views here.

def post_list(request):
    posts = models.Post.objects.all() #return all object in db
    return render(request, 'post_list.html', {'post':post_list} )