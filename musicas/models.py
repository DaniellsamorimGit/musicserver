from django.db import models
from musicas.helper import get_audio_length
from .validators import validate_is_audio
# Create your models here.




class Artista(models.Model):
    nome_artista = models.CharField(max_length=500)
    local_show = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='midia/', blank=False)



    def __str__(self):
        return (self.nome_artista + ' - ' + self.local_show)

class Faixa(models.Model):
    post = models.ForeignKey(Artista, default=None, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='musics/', validators=[validate_is_audio])
    time_length = models.DecimalField(max_digits=20, decimal_places=2, blank=True)

    def __str__(self):
        return (self.post.nome_artista + self.post.local_show)

    def save(self,*args, **kwargs):
        if not self.time_length:
            # logic for getting length of audio
            audio_length=get_audio_length(self.audio_file)
            self.time_length = f'{audio_length:.2f}'

        return super().save(*args, **kwargs)

    class META:
        ordering="id"