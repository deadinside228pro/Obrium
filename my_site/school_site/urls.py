
from django.urls import *
from . import views

urlpatterns = [
    path('reg', views.reg, name='reg'),
    path('student/', include("student.urls")),
    path('teacher/', include("teacher.urls")),
    path('main/<int:pk>', views.WorksDetailView.as_view(), name='main_detail'),
    path('testiruyu', views.testiruyu, name='testiruyu')
]
