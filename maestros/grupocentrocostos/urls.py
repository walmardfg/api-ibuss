from django.urls import path
from .views import GrupoCentroCostoList,GrupoCentroCostoDetail

urlpatterns = [
    path('grupocentrocostos/', GrupoCentroCostoList.as_view()),
    path('grupocentrocostos/<int:pk>/', GrupoCentroCostoDetail.as_view()),
]
