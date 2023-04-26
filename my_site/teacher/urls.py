from django.urls import *
from . import views

urlpatterns = [
    path('main', views.main, name='tch_main'),
    path('profile', views.profile, name='tch_profile'),
]
