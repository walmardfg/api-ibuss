from django.urls import path
from .views import MiscelaneoList,MiscelaneoDetail
urlpatterns = [
    path('miscelaneos/', MiscelaneoList.as_view()),
    path('miscelaneos/<int:pk>/', MiscelaneoDetail.as_view()),
]
