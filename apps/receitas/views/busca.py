from ..models import Receitas
from django.shortcuts import render
from helpers.paginacao import paginar

def buscar_receitas(filters:dict = {}):
    """ Busca receitas de acordo com o filtro passado """

    filters['publicada'] = True

    return Receitas.objects.filter(**filters).order_by('-date_receita') #sinal de - indica ordenação DESC


def buscar(request):
    """ Busca por uma receita e monta a view com os resultados """

    filters = dict()

    if 'receita' in request.GET:
        filters['nome_receita__icontains'] = request.GET['receita']

    receitas = buscar_receitas(filters)
    
    receitas_por_paginas = paginar(request, receitas)
    
    return render(request, 'index.html', {'lista_de_receitas' : receitas_por_paginas})