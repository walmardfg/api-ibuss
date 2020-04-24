from django.urls import path
from .views import SubGrupoCentroCostoList,SubGrupoCentroCostoDetail

urlpatterns = [
    path('subgrupocentrocostos/', SubGrupoCentroCostoList.as_view()),
    path('subgrupocentrocostos/<int:pk>/', SubGrupoCentroCostoDetail.as_view()),
]
