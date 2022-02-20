
from django.urls import path
from . import views

urlpatterns = [
    path('',views.DeterminantSolver,name='DeterminantSolver'),

    path('DeterminantSolverPage', views.DeterminantSolverPage, name='DeterminantSolverPage'),
    path('DeterminantSolver', views.DeterminantSolver, name='DeterminantSolver'),
]

# urlpatterns += [
#     path('Determinantcalculator',views.HOME,name='HOME')
# ]

