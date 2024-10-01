from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Asegúrate de que 'datos.urls' esté bien escrito
    path('', include('datos.urls')),
]
