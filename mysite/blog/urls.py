from django.urls import path
from .views import home
from .views import about

urlpatterns = [
    path('', home, name="blog-home"),
    path('about/', about, name="blog-about")
]
