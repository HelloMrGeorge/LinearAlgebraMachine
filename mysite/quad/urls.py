from django.urls import path
from . import views

urlpatterns = [
    path('',views.quad,name='eigen'),
    path('quadCourse', views.quadCourse, name='quadCourse'),
]