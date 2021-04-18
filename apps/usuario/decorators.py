from helpers.mensagem import adicionar_mensagens
from django.contrib import messages as django_messages
from django.contrib.auth.models import User 

# valida os campos nescessários para que o usuário seja cadastrado 
def validar_parametros_cadastro(func):
    def validar_parametros(request):

        parametros = request.POST.dict()        

        mensagens = []

        if('username' not in parametros or not parametros['username'].strip()):
            mensagens.append({'tipo': django_messages.ERROR, 'texto': 'Nome do usurio não informado'})

        if('email' not in parametros or not parametros['email'].strip()):
            mensagens.append({'tipo': django_messages.ERROR, 'texto':'Email do usurio em branco'})

        if('password' not in parametros or 'password2' not in parametros):
            mensagens.append({'tipo': django_messages.ERROR, 'texto':'Preencha os campos de senha e de confirmação de senha'})

        if(parametros['password'] != parametros['password2']):
            mensagens.append({'tipo': django_messages.ERROR, 'texto':'os campos de senha e de confirmação de senha não são iguais'})

        # verifica se o email do usuário já existe no banco
        if(User.objects.filter(email= parametros['email']).exists()):
            mensagens.append({'tipo': django_messages.ERROR, 'texto':'Usuário já cadastrado no sistema'})
        
        if(User.objects.filter(username= parametros['username']).exists()):
            mensagens.append({'tipo': django_messages.ERROR, 'texto':'Usuário já cadastrado no sistema'})

        if(not len(mensagens)):
            return func(request)  
        else:
            adicionar_mensagens(request, mensagens)     
    
    return  validar_parametros     
        

def validar_parametros_login(function):
    def validar_parametros(request):

        parametros = request.POST.dict()

        mensagens = []

        if(('email' not in parametros or not parametros['email'].strip()) or 
          ('password' not in parametros or not parametros['password'].strip())):
            mensagens.append({'tipo': django_messages.ERROR, 'texto': "Email ou senha não informado"})
        
                    
        if(len(mensagens)):
            adicionar_mensagens(request, mensagens) 

        return function(request)  

    return validar_parametros