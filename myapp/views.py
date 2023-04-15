from django.shortcuts import render,redirect
import json
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from .models import Class, Teacher, Subject,Student,Parent


# Create your views here.

def index(request):
    return render(request,'index.html')


def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        stud = Student.objects.create(first_name=first_name,last_name=last_name,gender=gender,dob=dob)
        stud.save()
        stud.addmission_no = stud.id
        stud.save()
        redirect_url = reverse('parent_add')+f'?data={stud.id}'
        return HttpResponseRedirect(redirect_url)
    return render(request,'student.html')

def parent_add(request):
    data = request.GET.get('data')
    if request.method == "POST":
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('motherName')
        address = request.POST.get('address')
        phone_number = request.POST.get('fatherPhone')
        email = request.POST.get('email')
        student_id = request.POST.get('id')
        par = Parent.objects.create(father_name=father_name,mother_name=mother_name,address=address,phone_number=phone_number,email=email)
        par.save()
        stud = Student.objects.filter(pk=student_id)
        for i in stud:
            i.parent_id=par
            i.save()
        return HttpResponse("Data saved")
    return render(request,'parent.html',{"data":data})

def teacher(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        hire_date = request.POST.get('hire_date')
        
        subject_id = request.POST.get('subject_id')
        # Extracting Subject Info
        sub_info = subject_id.split("-")

        class_id = request.POST.get('class_id')
        # Retrieve the Class instance
        cls = Class.objects.get(pk=class_id)

        email = request.POST.get('email')

        teacher = Teacher.objects.create(
            first_name = first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            phone_no=phone_no,
            address=address,
            salary=salary,
            hire_date=hire_date,
            subject_id=sub_info[0],
            class_id=cls,
            email=email
        )
        teacher.save()
        teacher.teacher_id = teacher.pk
        teacher.save()
        subject = Subject.objects.create(
                teacher_id = teacher,
                subject_id = sub_info[0],
                subject_name = sub_info[1],
            )
        subject.save()
        return HttpResponse(request,"Teacher Database Saved")

    try:
        classes = Class.objects.all()
    except classes.DoesNotExist:
        raise Http404('No class found to assign the teacher to')
    context = {"classes" : classes}
    return render(request,'teacherReg.html', context)