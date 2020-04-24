from django.urls import path
from .views import SucursalList,SucursalDetail

urlpatterns = [
    path('sucursales/', SucursalList.as_view()),
    path('sucursales/<int:pk>/', SucursalDetail.as_view()),
]
