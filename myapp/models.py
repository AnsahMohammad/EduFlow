from django.db import models

# Create your models here.

class Class(models.Model):
    class_id = models.CharField(max_length=10)
    class_name = models.CharField(max_length=20)
    

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    phone_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=50)
    salary = models.CharField(max_length=7)
    hire_date = models.DateField()
    subject_id = models.CharField(max_length=10)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    

class Parent(models.Model):
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)


class Student(models.Model):
    addmission_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    addmission_date = models.DateField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)

class Subject(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_id = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=20)

class Grade(models.Model):
    # grade_id = models.CharField(max_length=10)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    score_no = models.CharField(max_length=10)
    exam_date = models.DateField()

class Fee(models.Model):
    # fee_id
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    # class_id = models.ForeignKey()
    fee_amount = models.CharField(max_length=10)
    fee_type = models.CharField(max_length=10)
    payment_date = models.DateField()