from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='std_main'),
    path('profile', views.profile, name='std_profile'),
]
