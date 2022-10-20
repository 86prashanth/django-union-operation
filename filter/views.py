from .models import Employee
from django.shortcuts import render

# Create your views here.
def filter(request):
    blogs=['python','main','mysql','machinelearning','postgresql']
    order=[100,101,102,103,104,105]
    fair=(99 not in order)
    languages=['c','c++','python','java']
    test=['c sharp']
    vowels=['A','E','I','O','U']
    const=['A']
    result=('mysql' not in blogs)
    queryset=Employee.objects.exclude(Age__in=[28,25])
    queryset1=Employee.objects.exclude(pk__in=[1,3,5])
    queryset2=Employee.objects.exclude(position__in=['voicepresident'])
    print(queryset)
    print(queryset1)
    print(queryset2)
    return render(request,'app/first.html',{'result':result,'fair':fair,'languages':languages,'test':test,'vowels':vowels,'const':const})