from django.urls import path
from .views import EstadoList,EstadoDetail

urlpatterns = [
    path('estados/', EstadoList.as_view()),
    path('estados/<int:pk>/', EstadoDetail.as_view()),
]
