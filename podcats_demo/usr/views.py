from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.views import View

# Create your views here.

class Register(View):
    def register(self, request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.isvalid():
                form.save()
                username = form.cleaned_data.get('username')
                print(f'Successfully registered. Welcome{username}')
        else:
            form = UserRegisterForm()
        context = {
            'form' : form,
            'title' : 'Register'
        }
        return render(request, 'usr/register.html', context)