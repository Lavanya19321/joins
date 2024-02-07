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
    SO=SalGrade.objects.filter(grade__in=(1,4))#=>for getting the data which  is having salgrade is 3 and 4
    EO=Emp.objects.none() #=> here we get empty list of employee object
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))#=>|is for concatination


    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)

def selfjoins(request):
    EO=Emp.objects.select_related('mgr').all()
    EO=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    EO=Emp.objects.select_related('mgr').filter(mgr__ename='ALLEN')
    EO=Emp.objects.select_related('mgr').filter(sal__lte=2000)
    EO=Emp.objects.select_related('mgr').filter(sal__gte=2000)
    EO=Emp.objects.select_related('mgr').filter(ename='JONES')
    EO=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    EO=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    EO=Emp.objects.select_related('mgr').filter(mgr__ename='SCOTT')
    EO=Emp.objects.select_related('mgr').filter(sal__gte=1000,mgr__ename='ALLEN')
    EO=Emp.objects.select_related('mgr').filter(sal__lte=2000,mgr__ename='KING')
    EO=Emp.objects.select_related('mgr').filter(mgr__ename='KING',ename='JONES')
    EO=Emp.objects.select_related('mgr').filter(ename='JONES',sal__gte=2000)
    EO=Emp.objects.select_related('mgr').filter(ename='BLAKE',sal__lte=2000)
    d={'EO':EO}
    return render(request,'selfjoins.html',d)