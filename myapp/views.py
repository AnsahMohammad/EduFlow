from django.shortcuts import render,redirect
import json
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from .models import Class


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
    try:
        classes = Class.objects.all()
    except classes.DoesNotExist:
        raise Http404('No class found to assign the teacher to')
    context = {"classes" : classes}
    return render(request,'teacherReg.html', context)