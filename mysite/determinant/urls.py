
from django.urls import path
from . import views

urlpatterns = [
    path('',views.determinant,name='determinant'),
    path('deteranswer', views.deteranswer, name='deteranswer'),
    path('answer', views.answer, name='answer'),
    path('test', views.test, name='csrf_test'),
    path('csrf', views.csrftest),
]
