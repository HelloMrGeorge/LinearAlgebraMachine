from django.urls import path
from . import views

urlpatterns = [
    path('', views.LinequSolver),
    path('LinequSolver', views.LinequSolver, name='LinequSolver'),
    path('GESolver', views.GESolver, name='GESolver'),
    path('GESolverPage', views.GESolverPage, name='GESolverPage'),
]