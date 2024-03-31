from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import RegisterForm, LoginForm,ProfileUpdateForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from my_app.models import Category, Books, Author
import requests
from users.models import User
from django.views.generic.edit import UpdateView
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,(f" Salom {user.first_name} {user.last_name} sizni yana ko'rib turganimizdan hursandmiz"))
                return redirect('books:index')
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
    return redirect('books:index')

from django.shortcuts import get_object_or_404

def Yuklash(request):
    context = {
        'category': Category.objects.all(),
        'author': Author.objects.all()
    }
    if request.method == "POST":
        r = request.POST
        f = request.FILES
        print(r)
        category_id = r['category']
        photo = f['photo']
        name = r['name']
        author = r['author']
        description = r['description']
        pdf = f['pdf']
        muallif = r['muallif']
        
        if author == '':
            muallif_base = Author.objects.create(name=muallif)
            author_id = muallif_base.id
            avtor_id = get_object_or_404(Author, id=author_id)

            category = get_object_or_404(Category, id=category_id)
            yaratish = Books.objects.create(category=category, name=name, author=avtor_id, photo=photo, pdf=pdf, description=description)
            return redirect('/')
        else:
            category = get_object_or_404(Category, id=category_id)
            Books.objects.create(category=category, name=name, author_id=author, photo=photo, pdf=pdf, description=description)
            return redirect('/')
    else:
        return render(request, 'yuklash1.html', context)
    

class ProfileUpdateView(UpdateView):

    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, 'account_update.html', {'form':form})
    def post(self, request):
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        r = request.POST
        f = request.FILES
        print(r)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'account_update.html', {'form':form})

class Profile(View):
    def get(self, request):
        return render(request, 'account_view.html')
    
def image_edit(request):
    context = {
        'user': User.objects.all()
    }
    if request.method == "POST":
        r = request.POST
        f = request.FILES
        print(r)
      
        photo = f['photo']
        name = r['name']
        author = r['author']
        description = r['description']
        pdf = f['pdf']
        muallif = r['muallif']
