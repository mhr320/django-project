from django.shortcuts import render
from .models import Post, ForcedMovePost

def home(request):
    context = {
        'posts': Post.objects.all(),
        'forced_moves': ForcedMovePost.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
