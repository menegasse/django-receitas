from django.db.models import Model, CharField

class Pessoa(Model):
    nome = CharField(max_length=200)
    email = CharField(max_length=200)

    def __str__(self):
        return self.nome