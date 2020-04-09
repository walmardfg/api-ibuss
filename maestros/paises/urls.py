from django.urls import path
from .views import PaisDetail,PaisList
urlpatterns = [
    path('paises/', PaisList.as_view()),
    path('paises/<int:pk>/', PaisDetail.as_view()),
]
