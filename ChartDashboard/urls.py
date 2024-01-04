from django.urls import include, path

from ChartDashboard import views

urlpatterns = [
    path('', views.index, name='index')
]