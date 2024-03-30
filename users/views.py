from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import RegisterForm, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,(f" Salom {user.first_name} {user.last_name} sizni yana ko'rib turganimizdan hursandmiz"))
                return redirect('index')
            else:
                messages.error(request,("Login yoki parolni notogri kiritdingiz  iltimos qayta urinib koring "))

    else:
        form = LoginForm()



    return render(request,'login.html',{'form_login':form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,(" Ro'yhatdan o'tish muvaffaqiyatli yakunlandi "))
            return HttpResponseRedirect(reverse('users:login')) 
            
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')