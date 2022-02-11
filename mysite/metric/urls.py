from django.urls import path
from . import views

urlpatterns = [
    path('',views.SchmidtVectorSolverPage),
    path('SchmidtVectorSolverPage',views.SchmidtVectorSolverPage, name='SchmidtVectorSolverPage'),
    path('SchmidtVectorSolver',views.SchmidtVectorSolver, name='SchmidtVectorSolver'),
]