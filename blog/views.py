from django.shortcuts import render
from .models import Post, Forced, Period

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def forced(request):

    period_id = Period.objects.get(pk=1)
    force = Forced.objects.filter(period=period_id)
    # period = Period.objects.order_by("-pay_period")

    forced_move = {
        'period': period_id,
        'forced': force,
    }

    return render(request, 'blog/forcedMoves.html', forced_move)
