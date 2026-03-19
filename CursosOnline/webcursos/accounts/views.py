from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'account/accounts.html', {'form':form})

def login_view(request):
    error = None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Email ou senha inválidos'
    return render(request, 'account/login.html', {'error':error})