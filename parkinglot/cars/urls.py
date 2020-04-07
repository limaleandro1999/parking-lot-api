from rest_framework import routers

from parkinglot.cars.views import CarViewSet

router = routers.DefaultRouter()
router.register("cars", CarViewSet, basename="cars")

urlpatterns = router.urls
