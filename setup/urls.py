from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu.views import index  # Garanta que este import aponta para o menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), # O caminho vazio '' é a sua página inicial
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
