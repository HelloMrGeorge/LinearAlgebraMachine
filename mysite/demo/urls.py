from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('test', views.testPage, name='testPage'),
    path('csrf_test_func(', views.csrf_test_func, name='csrf_test'),
    path('csrf', views.csrf_page),
]