from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def sayhello(request):
#     return HttpResponse("Hello world!")

def website(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Views
@login_required
def home(request):
    return render(request, "registration/index.html", {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
