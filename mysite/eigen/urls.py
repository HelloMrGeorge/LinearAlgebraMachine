
from django.urls import path
from . import views

urlpatterns = [
    path('',views.eigen,name='eigen'),
    path('eigenCourse', views.eigenCourse, name='eigenCourse'),
    path('eigenvectors',views.eigenvectors,name='eigenvectors'),
    path('eigenvalue',views.eigenvalue,name='eigenvalue'),
    path('eigencharpoly',views.eigencharpoly,name='eigencharpoly'),
]

urlpatterns += [

    path('eigenvaluePage',views.eigenvaluePage,name='eigenvaluePage')

]