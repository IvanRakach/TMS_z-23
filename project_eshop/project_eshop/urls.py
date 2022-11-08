from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from project_eshop import settings

API_PATTERNS = [
    # path('', include('carts.urls')),
    # path('', include('categories.urls')),
    path('', include('phone_items.urls')),
    path('', include('phone_orders.urls')),
    # path('', include('users.urls')),
]

from phone_items.views import ProductAPIView
from phone_items import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(API_PATTERNS)),
    path('productlist/', ProductAPIView.as_view(), name='catalog'),
    path('', views.index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
