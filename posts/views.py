from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM POSTS'

    posts = Posts.__class__.objects.all()[:10]
    #Posts.

    context = {
        'title' : 'Latest Posts-1',
        'posts' : posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.__class__.objctes.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)