from django.contrib.admin import site, ModelAdmin 
from .models import Receitas

class ListandoReceitas(ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada',)
    list_display_links =  ('id', 'nome_receita',)
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 2

site.register(Receitas, ListandoReceitas)
