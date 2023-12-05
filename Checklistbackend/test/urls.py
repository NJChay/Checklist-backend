from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.getData),
    path('post', views.postData),
    # path('<string:pk>/', views.deleteData, name='task-delete'),
    path('delete', views.deleteData)
]
