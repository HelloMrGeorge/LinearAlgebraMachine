
from django.urls import path
from . import views

urlpatterns = [
    path('',views.eigen,name='eigen'),
    path('eigenvectorsCourse', views.eigenvectorsCourse, name='eigenvectorsCourse'),
    path('eigenvectors',views.eigenvectors,name='eigenvectors'),
    path('eigenvalue',views.eigenvalue,name='eigenvalue'),
    path('eigencharpoly',views.eigencharpoly,name='eigencharpoly'),
]