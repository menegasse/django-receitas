from ..decorators import validar_parametros_receita
from helpers.mensagem import adicionar_mensagens

from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages as django_messages

from ..models import Receitas
from django.contrib.auth.models import User 


def receita(request, receita_id):

    receita_a_exibir = {
        'receita' : get_object_or_404(Receitas, pk=receita_id)
    }

    return render(request, "receitas/receita.html", receita_a_exibir)
    
def cria_receita(request):

    if(request.method == 'POST'): 
        cria_receita_POST(request) 

    return render(request, 'receitas/criar_receita.html')

@validar_parametros_receita
def receitas_parametros(request) -> dict:

    parametros = request.POST.dict() 
    
    data = {
                'id': parametros.get('receita_id', None),
                'nome_receita' : parametros['nome_receita'],
                'ingredientes': parametros['ingredientes'],
                'modo_preparo': parametros['modo_preparo'],
                'tempo_preparo': parametros['tempo_preparo'],
                'rendimento': parametros['rendimento'],
                'categoria': parametros['categoria'],
                'pessoa' : get_object_or_404(User, pk= request.user.id),
            }

    if 'foto_receita' in  request.FILES :
        data['foto_receita'] = request.FILES['foto_receita']
    
    return data

def cria_receita_POST(request):

    mensagens = []
    parametros = receitas_parametros(request)
    
    try:
        nova_receita = Receitas(**parametros)
        nova_receita.save()

        if(nova_receita.id):           
            mensagens.append({'tipo': django_messages.SUCCESS, 'texto':"Receita cadastrado com sucesso"})
        else:
            mensagens.append({'tipo': django_messages.ERROR, 'texto':"Falha ao cadastrar nova receita"})
    except:
        mensagens.append({'tipo': django_messages.ERROR, 'texto':"Falha ao cadastrar nova receita"})

    adicionar_mensagens(request, mensagens)

def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    return render(request, 'receitas/editar_receita.html', {'receita':receita})

def atualiza_receita(request):
    mensagens = []
    parametros = receitas_parametros(request)
    
    try:
    
        receita = get_object_or_404(Receitas, pk=parametros['id'])

        for key, value in parametros.items():
            setattr(receita, key, value)

        receita.save()
                    
        mensagens.append({'tipo': django_messages.SUCCESS, 'texto':"Receita atualizada com sucesso"})
            
    except:
        mensagens.append({'tipo': django_messages.ERROR, 'texto':"Falha ao atualiza receita"})

    adicionar_mensagens(request, mensagens)

    return render(request, 'receitas/editar_receita.html', {'receita': parametros})