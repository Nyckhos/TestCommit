from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_personas, name ='lista_personas'),
    path('tarjetas', views.lista_tarjetas, name ='lista_tarjetas'),
    path('tarjetas_con_plata', views.tarjetas_con_plata, name ='tarjetas_con_plata'),
    path('registro', views.persona_nueva, name ='registro'),
    path('index', views.index, name = 'index'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('index', views.index, name = 'index'),
    path('index', views.index, name = 'index'),


]

urlpatterns+= [
    path('accounts/', include ('django.contrib.auth.urls'))

]