from django.urls import path

from . import views

urlpatterns = [
    path('create', views.index),
     path('update', views.update),
      path('delete', views.delete),
]