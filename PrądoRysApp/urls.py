from django.urls import path
from . import views
from .views import chart_view, file_upload

urlpatterns = [
    path('', views.chart_view, name='chart'),
    path('upload/', views.file_upload, name='file_upload'),
    path('api/chart-data/', views.read_chart_data, name='read_chart_data'),
]
