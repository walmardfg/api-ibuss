from django.urls import path
from .views import ParroquiaList,ParroquiaDetail

urlpatterns = [
    path('parroquias/', ParroquiaList.as_view()),
    path('parroquias/<int:pk>/', ParroquiaDetail.as_view()),
]
