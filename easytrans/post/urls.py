from django.urls import path
from .views import PosterAPIView, PosterDetails

urlpatterns = [
    path('post', PosterAPIView.as_view()),
    path('detail/<int:id>/', PosterDetails.as_view())
]
