from typing import ContextManager
import app1
from django.shortcuts import render, redirect
from .models import  Comentario, User
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/") 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date = request.POST.get('date_of_birth')
        email = request.POST.get('register_email')
        password = request.POST.get('password')
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        loged_user = User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash,date_of_birth=date)
        request.session['id'] = loged_user.id
        print(date)
        return redirect('/main_register')
    else:
        if "logged_user.id" not in request.session:
            return redirect("/")
    return redirect("/")

def main_register(request):
    if 'id' in request.session:
        user_id=request.session['id']
        user= User.objects.get(id=user_id)
        context={
            'name': f'{user.first_name} {user.last_name}'
        }
        return render(request, 'main_register.html', context)
    else:
        return redirect("/")

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/")
        email=request.POST.get('login_email')
        user = User.objects.filter(email = email)
        if len(user) == 1:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
                request.session['id'] = logged_user.id
                return redirect("/main_logeado")
    return redirect("/")

def main_logeado(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        text_area = request.POST.get('textarea')
        sesion = request.session['id']
        usuario = User.objects.filter(id=sesion)[0]
        posted_user = Comentario.objects.create(name=name,comentario=text_area)
        print(usuario)
        return redirect("/main_logeado")
    else:
        comentarios = Comentario.objects.all()
        context={
            'posted_user' : comentarios
        }
        return render(request, 'main_logeado.html', context=context)  
    