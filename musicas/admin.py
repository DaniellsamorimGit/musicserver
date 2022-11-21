from django.contrib import admin
from .models import Artista, Faixa

# Register your models here.
#admin.site.register(Musica)

class PostImageAdmin(admin.StackedInline):
    model=Faixa

@admin.register(Artista)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model=Artista

@admin.register(Faixa)
class PostImageAdmin(admin.ModelAdmin):
    pass