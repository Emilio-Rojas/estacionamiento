from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .views import *


urlpatterns = [
    path('', home, name='pagina-principal')
]