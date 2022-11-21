
import os
from .models import Artista, Faixa
from os import chdir, getcwd, listdir
from os.path import isfile

def lista_musicas(request):
    lis_mus= []

    #print("listalouca", lis_mus)

    return {"lis_mus": lis_mus}

def lista_forro(request):
    lista_forro = Artista.objects.all()
    return {"lista_forro": lista_forro}