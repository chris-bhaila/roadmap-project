from django.urls import path

from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('taxonomy/', views.taxonomy, name='taxonomy'),
    path('taxonomy/save/', views.taxonomy_save, name='taxonomy_save'),
    path('resources/', views.resources, name='resources'),
    path('analytics/', views.analytics, name='analytics'),
]
