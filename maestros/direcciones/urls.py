from django.urls import path
from .views import DireccionList,DireccionDetail
urlpatterns = [
    path('direcciones/', DireccionList.as_view()),
    path('direcciones/<int:pk>/', DireccionDetail.as_view()),
]
