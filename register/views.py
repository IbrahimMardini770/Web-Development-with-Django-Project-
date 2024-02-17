from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.http import HttpResponse

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
           # return redirect("/home")        # you must to add redirect in the top of this file
    else:
        form = RegisterForm()
    return render(response , "register/register.html",{"form": form})

def home(request):
    return render(request, "home.html")