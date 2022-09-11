from django.shortcuts import render
from.models import Employee


empid = 10000
def allEmp(request):
    emp = Employee.objects.all()
    return render(request, 'allEmp.html', {'emp':emp})

def addEmp(request):
    global empid
    if request.method == "POST":
       name = request.POST.get('name')
       age = request.POST.get('age')
       salary = request.POST.get('salary')
       qualification = request.POST.get('qualification')
       designation = request.POST.get('designation')
       file = request.FILES.get('myfile')
       
       
       Employee(name=name, age=int(age), salary=int(salary), qualification=qualification, designation=designation, image=file).save()
    return render(request, 'addEmp.html')

def manageEmp(request):
    return render(request, 'manageEmp.html')
