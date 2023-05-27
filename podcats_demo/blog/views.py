from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Blog(View):
    def Home(request):
        return render(request, 'blog/blog.html', {'title' : 'Home'})
