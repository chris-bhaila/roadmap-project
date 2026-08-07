from django.urls import path

from . import views

app_name = 'predictions'

urlpatterns = [
    path('', views.predict, name='predict'),
    path('result/', views.prediction_result, name='result'),
]
