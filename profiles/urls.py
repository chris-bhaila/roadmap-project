from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_detail, name='detail'),
    path('edit/', views.profile_edit, name='edit'),
    path('setup/', views.profile_setup, name='setup'),
    path('upload/', views.profile_upload, name='upload'),
    path('skills/', views.profile_skills, name='skills'),
]
