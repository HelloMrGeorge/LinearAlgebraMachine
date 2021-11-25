
from django.urls import path
from . import views

urlpatterns = [
    path('',views.determinant,name='determinant'),
    path('deteranswer', views.deteranswer, name='deteranswer'),

]
