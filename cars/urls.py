from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.CarsIndexView.as_view(), name='index'),
    path('<int:pk>/', views.CarsDetailView.as_view(), name='detail')
]
