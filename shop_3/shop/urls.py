from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_slug>[-\w]+)/$',
#         views.product_list,
#         name='product_list_by_category'),
#     url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$',
#         views.product_detail,
#         name='product_detail'),
# ]

from django.urls import path

urlpatterns = [
    path('', views.index, name="HOME"),
    path('products', views.product_list, name="product_list"),
    path('product_detail', views.product_detail, name="product_detail"),
]