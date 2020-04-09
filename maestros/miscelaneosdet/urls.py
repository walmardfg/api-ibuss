from django.urls import path
from .views import DetMiscelaneoList,DetMiscelaneoDetail

urlpatterns = [
    path('miscelaneosdet/', DetMiscelaneoList.as_view()),
    path('miscelaneosdet/<int:pk>/', DetMiscelaneoDetail.as_view()),
]
