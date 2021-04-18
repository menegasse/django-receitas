#decorators
from .decorators import  validar_parametros_cadastro, validar_parametros_login
from helpers.mensagem import adicionar_mensagens

#django functions 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as django_messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from helpers.paginacao import paginar

#models 
from django.contrib.auth.models import User 
from receitas.models import Receitas

def cadastro(request):    
    if(request.method == 'POST'): 
        register_POST(request) 

    return render(request, 'usuario/cadastro.html')

@validar_parametros_cadastro
def get_register_params(request) -> dict:
    parametros = request.POST.dict() 
    return {
        'username': parametros['username'],
        'email': parametros['email'],
        'password' : parametros['password']
    }

def register_POST(request):

    messages = []
    parametros = get_register_params(request)
    
    try:
        new_user = User.objects.create_user(**parametros)
        new_user.save()

        if(new_user.id):           
            messages.append({'tipo': django_messages.SUCCESS, 'texto':"Usuário cadastrado com sucesso"})
        else:
            messages.append({'tipo': django_messages.ERROR, 'texto':"Falha ao cadastrar novo usuário"})
    except:
        messages.append({'tipo': django_messages.ERROR, 'texto':"Falha ao cadastrar novo usuário"})

    adicionar_mensagens(request, messages)

def login(request):
    if(request.method == 'POST'): 
        return login_POST(request) 

    return render(request, 'usuario/login.html')

@validar_parametros_login
def parametros_login(request) -> dict:
    parametros = request.POST.dict() 
    return parametros['email'],parametros['password']

def login_POST(request):
    
    messages = []
    email, password = parametros_login(request)

    try:
        username = User.objects.filter(email=email).values_list('username', flat=True).get()
        user = authenticate(request, username=username, password=password)
        auth_login(request, user)
        return redirect('dashboard')     
    except:
        messages.append({'tipo': django_messages.ERROR, 'texto':'Email ou senha incorreto'})          

    adicionar_mensagens(request, messages) 
    return render(request, 'usuario/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        recipes = Receitas.objects.order_by('-date_receita').filter(pessoa= request.user.id)
        receitas_por_paginas = paginar(request, recipes)
        return render(request, 'usuario/dashboard.html', {'lista_de_receitas': receitas_por_paginas})
    else: 
        return redirect ('index')

def logout(request):
    auth_logout(request)
    return redirect ('index')