from django.urls import path
from . import views

urlpatterns = [
    path('',views.QuadSolverPage),
    path('QuadSolver', views.QuadSolver, name='QuadSolver'),
    path('QuadSolverPage', views.QuadSolverPage, name='QuadSolverPage'),
]