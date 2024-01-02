from django.shortcuts import render , redirect
from .forms import RegisterForm

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
           # return redirect("/home")        # you must to add redirect in the top of this file
    else:
        form = RegisterForm()
    return render(response , "register/register.html",{"form": form})