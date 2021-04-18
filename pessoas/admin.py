from django.contrib.admin import site, ModelAdmin
from .models import Pessoa

# Register your models here.

class ListandoPessoas(ModelAdmin):   
    list_display = ('id','nome', 'email',)
    list_display_links = ('id', 'email',)
    search_fields = ('nome',)
    list_per_page = 2
    
site.register(Pessoa, ListandoPessoas)
