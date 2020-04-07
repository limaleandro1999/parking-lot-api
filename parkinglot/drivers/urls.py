from rest_framework import routers

from parkinglot.drivers.views import DriverViewSet

router = routers.DefaultRouter()
router.register("drivers", DriverViewSet, basename="drivers")

urlpatterns = router.urls