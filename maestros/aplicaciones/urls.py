from django.urls import path
from .views import AplicacionList,AplicacionDetail
urlpatterns = [
    path('aplicaciones/', AplicacionList.as_view()),
    path('aplicaciones/<int:pk>/', AplicacionDetail.as_view()),
]
