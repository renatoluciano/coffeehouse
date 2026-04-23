from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu import views as menu_views 
from accounts import views as accounts_views
from orders import views as orders_views # Importe orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.index, name='index'),
    path('product/<int:pk>/', menu_views.product_detail, name='product_detail'),
    
    # Auth & Profile
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    path('profile/', accounts_views.profile, name='profile'),
    path('profile/edit/', accounts_views.edit_profile, name='edit_profile'),
    
    # Orders
    path('order/create/<int:product_id>/', orders_views.create_order, name='create_order'),

    # Barista Routes
    path('barista/', orders_views.barista_dashboard, name='barista_dashboard'),
    path('barista/status/<int:order_id>/<str:new_status>/', orders_views.update_status, name='update_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)