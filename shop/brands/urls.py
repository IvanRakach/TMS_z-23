from rest_framework import routers

from .views import BrandViewSet

router = routers.DefaultRouter()
router.register('brands', BrandViewSet, basename='brands')

urlpatterns = router.urls
