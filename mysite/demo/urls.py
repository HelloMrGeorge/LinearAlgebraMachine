from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('testPage', views.testPage, name='testPage'),
    path('testSolver', views.testSolver, name='testSolver'),
    path('csrf_test_func(', views.csrf_test_func, name='csrf_test'),
    path('csrf', views.csrf_page),
]