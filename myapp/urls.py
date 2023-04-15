from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('parent_add',views.parent_add,name='parent_add'),
    path('teacher_add',views.teacher,name='teacher_add'),
    path('student_add',views.add_student,name='add_student')
]