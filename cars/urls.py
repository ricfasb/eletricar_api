from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cars.views import CarViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
