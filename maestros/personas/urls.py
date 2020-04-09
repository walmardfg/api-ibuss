from django.urls import path
from .views import PersonaList,PersonaDetail

urlpatterns = [
    path('personas/', PersonaList.as_view()),
    path('personas/<int:pk>/', PersonaDetail.as_view()),
]
