from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

# Create your urls here.
router = DefaultRouter()

router.register("", CategoryViewSet, basename="category")

urlpatterns = router.urls