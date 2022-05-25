from django.urls import path

from . import views
from .views import *

urlpatterns = \
    [
        path('', views.show_private_room_page, name="private_room_home"),
        # path('login/', LoginUser.as_view(), name='login'),
        path('login/', views.login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        # path('register/', RegisterUser.as_view(), name='register'),
        path('register/', views.register_user, name='register'),
        # path('register_success/', views.show_register_success, name='register_success'),
    ]
