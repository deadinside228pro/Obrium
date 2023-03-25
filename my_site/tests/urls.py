from django.urls import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('math/', views.tests, name='Математика'),
    path('literature/', views.tests, name='Литература'),
    path('rus/', views.tests, name='Русский язык'),
    path('phys/', views.tests, name='Физика'),
    path('eng/', views.tests, name='Английский язык'),
    path('chem/', views.tests, name='Химия'),
    path('alg/', views.tests, name='Алгебра'),
    path('geom/', views.tests, name='Геометрия'),
    path('hist/', views.tests, name='История'),
    path('soc/', views.tests, name='Обществознание'),
    path('geogr/', views.tests, name='География'),
    path('bio/', views.tests, name='Биология'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
