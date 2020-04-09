from django.urls import path
from .views import ParametroList,ParametroDetail

urlpatterns = [
    path('parametros/', ParametroList.as_view()),
    path('parametros/<int:pk>/', ParametroDetail.as_view()),
]
