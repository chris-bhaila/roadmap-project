from django.urls import path

from . import views

app_name = 'roadmap'

urlpatterns = [
    path('', views.roadmap_overview, name='overview'),
    path('skill-gap/', views.skill_gap, name='skill_gap'),
    path('projects/', views.recommended_projects, name='projects'),
    path('internships/', views.internships, name='internships'),
]
