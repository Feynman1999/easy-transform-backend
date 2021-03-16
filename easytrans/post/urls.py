from django.urls import path
from .views import PosterViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
]

router = DefaultRouter()
router.register('postes', PosterViewSet)

urlpatterns += router.urls

