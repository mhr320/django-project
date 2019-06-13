from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('polls/', include('polls.urls')),
    path('about/', views.about, name='blog-about'),
]
