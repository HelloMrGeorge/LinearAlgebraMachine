from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('answer', views.answer, name='answer'),
    path('GEM', views.gaussElim),
    path('GEMans', views.guassAns, name='GEMans'),
]