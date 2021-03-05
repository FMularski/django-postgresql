from django.urls import path
from . import views

app_name = 'drivers'

urlpatterns = [
    path('', views.DriversIndexView.as_view(), name='index'),
    path('<int:pk>/', views.DriversDetailView.as_view(), name='detail')
]
