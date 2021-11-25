
from django.urls import path
from . import views

urlpatterns = [
    path('',views.eigen,name='eigen'),
    path('eigenanswer', views.eigenanswer, name='eigenanswer'),
]