from django.urls import path
from .views import MonedaList,MonedaDetail

urlpatterns = [
    path('monedas/', MonedaList.as_view()),
    path('monedas/<int:pk>/', MonedaDetail.as_view()),
]
