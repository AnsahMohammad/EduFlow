from django.shortcuts import render,redirect
import json
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from .models import Class, Teacher, Subject


# Create your views here.

def index(request):
    return render(request,'index.html')


def addstudent(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')

        data = {
            'first_name':first_name,
            'last_name':last_name,
            'gender':gender,
            'dob':dob
        }

        data_str = json.dumps(data)
        redirect_url = reverse('parent') + f'?data={data_str}'
        return HttpResponseRedirect(redirect_url)
    return render(request,'student.html')


def parent(request):
    data = request.GET.get('data')
    data = json.loads(data)
    return HttpResponse("hello")

def teacher(request):
    if request.method == "POST":
        teach_ID = request.POST.get('teacher_id')
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
            teacher_id = teach_ID,
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

        subject = Subject.objects.create(
                teacher_id = teacher,
                subject_id = sub_info[0],
                subject_name = sub_info[1],
            )

        return redirect('index')

    try:
        classes = Class.objects.all()
    except classes.DoesNotExist:
        raise Http404('No class found to assign the teacher to')
    context = {"classes" : classes}
    return render(request,'teacherReg.html', context)