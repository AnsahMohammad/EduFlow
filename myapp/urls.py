from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('parent/',views.parent,name='parent'),
    path('add_teacher/',views.teacher,name='add_teacher'),
]