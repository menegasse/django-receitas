from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Model

def paginar(request, modelObject: Model, qtd_pagina: int = 3):
    "cria a paginação dos resultados apartir de um obejto Model do django"
    

    paginacao = Paginator(modelObject, qtd_pagina)
    pagina = request.GET.get('page')

    return paginacao.get_page(pagina) 