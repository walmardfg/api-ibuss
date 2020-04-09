from django.urls import path
from .views import CompaniaList,CompaniaDetail

urlpatterns = [
    path('companias/', CompaniaList.as_view()),
    path('companias/<int:pk>/', CompaniaDetail.as_view()),
]
