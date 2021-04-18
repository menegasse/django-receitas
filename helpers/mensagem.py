from django.contrib import messages as django_messages

def adicionar_mensagens(request, lista_de_mensagem: list = []):
        for mensagem in lista_de_mensagem:
            django_messages.add_message(request, mensagem['tipo'], mensagem['texto'])