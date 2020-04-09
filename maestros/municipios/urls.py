from django.urls import path
from .views import MunicipioList,MunicipioDetail

urlpatterns = [
    path('municipios/', MunicipioList.as_view()),
    path('municipios/<int:pk>/', MunicipioDetail.as_view()),
]
