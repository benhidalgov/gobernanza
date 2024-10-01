from django.urls import path
from . import views  # Importa las vistas desde views.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('actualizacion/', views.actualizacion,
         name='actualizacion'),  # Página de actualización
    path('login/', views.login_view, name='login'),  # Página de login
]
