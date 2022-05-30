from django.urls import path
from . import views


urlpatterns = [
  # add paramters to views 
  path('<int:id>', views.index, name="index"),
  # path('', views.index, name="index"),
]