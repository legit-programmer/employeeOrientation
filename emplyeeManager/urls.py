from django.urls import path
from.import views

urlpatterns = [
    path('allEmp/', views.EmpListView.as_view()),
    path('addEmp/', views.addEmp),
    path('update/<int:id>', views.updateEmp),
    path('rem/<int:id>', views.deleteEmp)
   
]