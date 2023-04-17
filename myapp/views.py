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
        return redirect('index')
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
        email = request.POST.get('email')
        # subject_id = request.POST.get('subject_id')
        # # Extracting Subject Info
        # sub_info = subject_id.split("-")
        teacher = Teacher.objects.create(
            first_name = first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            phone_no=phone_no,
            address=address,
            salary=salary,
            hire_date=hire_date,
            # subject_id=sub_info[0],
            # class_id=cls,kjsjdflak
            email=email
        )
        teacher.save()
        teacher.teacher_id = teacher.pk
        teacher.save()
        return redirect('index')

    try:
        classes = Class.objects.all()
    except classes.DoesNotExist:
        raise Http404('No class found to assign the teacher to')
    context = {"classes" : classes}
    return render(request,'teacher.html', context)

def show(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {
        "students":students,
        "teachers":teachers
    }
    return render(request,'show_data.html',context)

def edit_student(request,pk):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        pk = request.POST.get('id')
        stud = Student.objects.filter(id=pk)
        for s in stud:
            s.first_name = first_name
            s.last_name = last_name
            s.gender = gender
            s.dob = dob
            s.save()
        return redirect('show')
    student = Student.objects.filter(id=pk)
    context = {
        "students":student
    }
    return render(request,'edit_student.html',context)

def edit_teacher(request,pk):
    if request.method == "POST":
        teacher_id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        phone_no = request.POST.get('phone_no')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        hire_date = request.POST.get('hire_date')
        subject_id = request.POST.get('subject_id')
        email = request.POST.get('email')
        pk = request.POST.get('id')
        teach = Teacher.objects.filter(id=pk)
        for t in teach:
            t.teacher_id = teacher_id
            t.first_name = first_name
            t.last_name = last_name
            t.dob = dob
            t.phone_no = phone_no
            t.gender = gender
            t.address = address
            t.salary = salary
            t.hire_date = hire_date
            t.subject_id = subject_id
            t.email = email
            t.save()
        return redirect('show')
    teacher = Teacher.objects.filter(id=pk)
    context = {
        "teacher":teacher
    }
    return render(request,'edit_teacher.html',context)