from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('parent',views.parent,name='parent'),
    path('student_add',views.student_add,name='student_add')
]