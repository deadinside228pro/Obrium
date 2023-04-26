
from django.urls import *
from . import views

urlpatterns = [
    path('reg', views.reg, name='reg'),
    re_path(r'/student', include("student.urls")),
    path('profile', views.profile, name='profile'),
    path('main/<int:pk>', views.WorksDetailView.as_view(), name='main_detail'),
    path('testiruyu', views.testiruyu, name='testiruyu')
]
