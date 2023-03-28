from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.index, name='reg'),
    path('main', views.main, name='main'),
    path('profile', views.profile, name='profile'),
    path('main/<int:pk>', views.WorksDetailView.as_view(), name='main_detail'),
    path('testiruyu', views.testiruyu, name='testiruyu')
]
