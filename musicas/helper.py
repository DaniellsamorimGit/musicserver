from mutagen.mp3 import MP3

def get_audio_length(file):
    '''
    pega as informações do arquivo mp3
    como o tamanho da musica para definirmos o tempo
    '''
    audio = MP3(file)
    return audio.info.length
    