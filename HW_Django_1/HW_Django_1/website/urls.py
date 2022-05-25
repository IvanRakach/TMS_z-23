from django.urls import path
from . import views
from .views import *

urlpatterns = \
    [
        path('', views.show_index, name="home"),
        path('about-us', views.show_about_us, name="about-us"),
        path('feedback', views.show_feedback, name="feedback"),
        path('sales', views.add_new_sale, name="sales"),
    ]
