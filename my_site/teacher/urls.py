from django.urls import *
from . import views

urlpatterns = [
    path('', views.teacher_main),
]
