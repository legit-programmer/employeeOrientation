from django.urls import path
from.import views

urlpatterns = [
    path('allEmp/', views.allEmp),
    path('addEmp/', views.addEmp),
    path('manageEmp/', views.manageEmp)
]