from django.shortcuts import render, get_object_or_404
from .models import Artista, Faixa
from django.views.generic import ListView, DetailView




# Create your views here.
class HomePage(ListView):
    template_name = 'homepage.html'
    model = Artista
    print('homepage')


class MusicsPage(DetailView):
    template_name = "detail.html"
    model = Faixa
    musicas_do_artista = []

    def get(self, request, *arg, **kwargs):
        artista = self.get_object()  # pega o artista que esta sendo acessado
        musicas = list(Faixa.objects.filter(post=artista.pk).values())
        self.musicas_do_artista.clear()
        for mus in musicas:
            self.musicas_do_artista.append(mus['audio_file'])

        print("PRINTAaaaaaaaaa: ", self.musicas_do_artista)
        return super().get(request, *arg, *kwargs)  # redireciona pro link final


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["musicas_do_artista"] = self.musicas_do_artista
            print("PRINTA: ")
            return context