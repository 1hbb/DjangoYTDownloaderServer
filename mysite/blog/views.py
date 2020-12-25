import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ratelimit.decorators import ratelimit

# Create your views here.
posts = [{
    'author': 'xxxx',
    'title': 'Blog Post 1',
    'content': 'First Blog Pots',
    'date_posted': '27 July, 2020',
},
    {
    'author': 'xxxx',
    'title': 'Blog Post 2',
    'content': 'Second Blog Pots',
    'date_posted': '20 August, 2020',
}]




@ratelimit(key='ip', rate='100/h', block=True)
def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


@ratelimit(key='ip', rate='100/h', block=True)
def about(request):
    return render(request, 'blog/about.html')
