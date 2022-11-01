from rest_framework import routers

from .views import ProductViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('items', ItemViewSet, basename='items')

urlpatterns = router.urls
