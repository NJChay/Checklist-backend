from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.getData),
    path('post', views.postData),
    path('postuser', views.postUser),
    path('delete', views.deleteData),
    path('put', views.putData),
    path('login', views.loginUser)
]
