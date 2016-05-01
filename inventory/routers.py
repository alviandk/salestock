from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'variations', views.VariationViewSet)
router.register(r'categories', views.CategoryViewSet)
