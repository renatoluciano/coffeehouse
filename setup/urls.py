from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu import views as menu_views 
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.index, name='index'),
    path('product/<int:pk>/', menu_views.product_detail, name='product_detail'),
    
    # Auth Routes
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    
    # Profile Routes
    path('profile/', accounts_views.profile, name='profile'),
    path('profile/edit/', accounts_views.edit_profile, name='edit_profile'), # NOVA ROTA
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
