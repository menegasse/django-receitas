from helpers.mensagem import adicionar_mensagens
from django.contrib import messages as django_messages
 
def validar_parametros_receita(function):
    def validar_parametros(request):

        parametros = request.POST.dict()

        mensagens = []

        if('nome_receita' not in parametros or not parametros['nome_receita'].strip()):
            mensagens.append({'type': django_messages.ERROR, 'text': "Nome da receita não informado"})
        
        if('rendimento' not in parametros or not parametros['rendimento'].strip()):
            mensagens.append({'type': django_messages.ERROR, 'text': "Rendimento não informados"})

        if('ingredientes' not in parametros or not parametros['ingredientes'].strip()):
            mensagens.append({'type': django_messages.ERROR, 'text': "Ingredientes não informados"})
        
        if('categoria' not in parametros or not parametros['categoria'].strip()):
            mensagens.append({'type': django_messages.ERROR, 'text': "Categoria não informados"})
        
        if('modo_preparo' not in parametros or not parametros['modo_preparo'].strip()):
            mensagens.append({'type': django_messages.ERROR, 'text': "Modo de preparo não informados"})
        
        if('tempo_preparo' not in parametros or not parametros['tempo_preparo'].strip()):
            mensagens.append({'type': django_messages.ERROR, 'text': "Tempo de preparo não informados"})
              

        if(not len(mensagens)):
            return function(request)  
        else:
            adicionar_mensagens(request, mensagens) 

    return validar_parametros