from django.urls import path
#se importa todo de views
from . import views
from django.conf import settings
from django.conf.urls.static import static


#se asigna ruta, se toma funcion de views y se le da nombre
urlpatterns = [



    path('',views.Index,name='index'),
    path('menu',views.Menu,name='menu'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)