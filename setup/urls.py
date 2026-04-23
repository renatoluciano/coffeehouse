from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu import views as menu_views 
from accounts import views as accounts_views # Importe as views de accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.index, name='index'),
    path('product/<int:pk>/', menu_views.product_detail, name='product_detail'),
    path('signup/', accounts_views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
