from django.urls import path
from .views import BancoList,BancoDetail

urlpatterns = [
    path('bancos/', BancoList.as_view()),
    path('bancos/<int:pk>/', BancoDetail.as_view()),
]
