from django.shortcuts import render, redirect
from.models import Employee
from django.views.generic import ListView, UpdateView





def addEmp(request):
    
    if request.method == "POST":
       name = request.POST.get('name')
       age = request.POST.get('age')
       salary = request.POST.get('salary')
       qualification = request.POST.get('qualification')
       designation = request.POST.get('designation')
       file = request.FILES.get('myfile')
       
       
       Employee(name=name, age=int(age), salary=int(salary), qualification=qualification, designation=designation, image=file).save()
       return redirect('/employeeManager/allEmp')
    
    else:
        return render(request, 'addEmp.html')


def updateEmp(request, id):
    
    emp = Employee.objects.get(pk=id)
    
 
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        qualification = request.POST.get('qualification')
        designation = request.POST.get('designation')
        file = request.FILES.get('myfile')
        emp.delete()
        Employee(name=name, age=int(age), salary=int(salary), qualification=qualification, designation=designation, image=file).save()
        return redirect('/employeeManager/allEmp')
    else:
        return render(request, 'update.html', {'emp':emp})
        
def deleteEmp(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('/employeeManager/allEmp')


class EmpListView(ListView):
    
    model = Employee
    template_name = 'allEmp.html'
    context_object_name = 'emp'


    
