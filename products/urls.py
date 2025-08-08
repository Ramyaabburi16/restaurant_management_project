from django.urls import path
from .views import MenuAPIView

urlpatterns = [
    path('menu/',MenuAPIView.as_view(), name='menu'),
]