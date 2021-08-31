from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('answer', views.answer, name='answer'),
    path('testView', views.testView, name='testView'),
    path('testAnswer', views.testAnswer, name='testAnswer')
    # path('demo3', views.demo, name='demo3'),
    # path('GEM', views.gaussElim),
    # path('GEMans', views.guassAns, name='GEMans'),
]