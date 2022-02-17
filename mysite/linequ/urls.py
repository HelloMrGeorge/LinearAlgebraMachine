from django.urls import path
from . import views

urlpatterns = [
    path('', views.LinequSolverPage),
    path('LinequSolver', views.LinequSolver, name='LinequSolver'),
    path('LinequSolverPage', views.LinequSolverPage, name='LinequSolverPage'),

    path('GESolver', views.GESolver, name='GESolver'),
    path('GESolverPage', views.GESolverPage, name='GESolverPage'),

    path('InverseSolverPage', views.InverseSolverPage, name='InverseSolverPage'),
    path('InverseSolver', views.InverseSolver, name='InverseSolver'),

    path('LambdaLinSolverPage', views.LambdaLinSolverPage, name='LambdaLinSolverPage'),
    path('LambdaLinSolver', views.LambdaLinSolver, name='LambdaLinSolver'),
]