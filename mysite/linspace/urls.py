from django.urls import path
from . import views

urlpatterns = [
    path('', views.MLIGSolverPage),
    path('MLIGSolverPage', views.MLIGSolverPage, name='MLIGSolverPage'),
    path('MLIGSolver', views.MLIGSolver, name='MLIGSolver'),
]