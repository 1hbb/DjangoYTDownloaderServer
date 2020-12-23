from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
posts = [{
    'author': 'Harun Burak Bursa',
    'title': 'Blog Post 1',
    'content': 'First Blog Pots',
    'date_posted': '27 July, 2020',
},
    {
    'author': 'Bursa Harun Burak',
    'title': 'Blog Post 2',
    'content': 'Second Blog Pots',
    'date_posted': '20 August, 2020',
}]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
