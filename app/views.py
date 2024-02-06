from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_emp(request):
    dn=input('enter deptno:')
    eno=input('enter empno:')
    en=input('enter ename:')
    job=input('enter job:')
    hd=input('enter hiredate:')
    sal=input('enter sal:')
    com=input('enter comm:')
    do=Department.objects.get(deptno=dn)
    eo=Emp.objects.get_or_create(deptno=do,empno=eno,ename=en,job=job,sal=sal,hiredate=hd,comm=com)
    eo.save()
    
    return HttpResponse('data inserted successfully')

def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=SalGrade.objects.all()#=>for getting the all salgrades
    #SO=SalGrade.objects.filter(grade=3)#=>for getting the  data only which is having salgrade is 3
    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    SO=SalGrade.objects.filter(grade__in=(3,4))#=>for getting the data which  is having salgrade is 3 and 4
    EO=Emp.objects.none() #=> here we get empty list of employee object
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))#=>|is for concatination


    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)
