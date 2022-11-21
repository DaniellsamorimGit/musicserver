
from django.urls import path
from musicas.views import HomePage, MusicsPage

app_name='musicas'

urlpatterns = [
    path('', HomePage.as_view(), name= 'homepage'),
    path('<int:pk>', MusicsPage.as_view(), name='detail')
]
