from rest_framework import routers

# from .views import ProductViewSet
from .views import ItemViewSet, ProductAPIView

router = routers.DefaultRouter()
# router.register('products', ProductViewSet, basename='products')
router.register('items', ItemViewSet, basename='items')

urlpatterns = router.urls

# urlpatterns = [
#     path("api/v1/women/", WomenAPIList.as_view()),
# ]
