from django.urls import path
from .views import CiudadList,CiudadDetail

urlpatterns = [
    path('ciudades/', CiudadList.as_view()),
    path('ciudades/<int:pk>/', CiudadDetail.as_view()),
]
