from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post

class Blog(View):
    def get(self , request):
        context = {
            'post' : Post.objects.all(),
            'title' : 'Home'
        }
        return render(request, 'blog/blog.html', context)
