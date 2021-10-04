from django.shortcuts import get_object_or_404, render
from . import models
# Create your views here.

def post_list(request):
    posts = models.Post.objects.all() #return all object in db
    context = {'posts': posts}
    return render(request, 'blogapp/post_list.html',context)

def post_details(request,post):
    post = get_object_or_404(models.Post, slug = post, status = 'publised')
    return render(request, 'blogapp/post_detail.html', {'post': post})

def test_view(request):
    return render(request, 'blogapp/home.html',)
