from django.db import models

# Create your models here.

class Class(models.Model):
    class_id = models.CharField(max_length=10)
    class_name = models.CharField(max_length=20)

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10,null=True,blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    phone_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=50)
    salary = models.CharField(max_length=7)
    hire_date = models.DateField()
    subject_id = models.CharField(max_length=10) # subject Name
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE,null=True,blank=True)
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
    addmission_date = models.DateField(auto_now_add=True,null=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE,null=True,blank=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.addmission_no)

class Subject(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_id = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=20)

class Grade(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score_no = models.CharField(max_length=10)
    exam_date = models.DateField()

class Fee(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_amount = models.CharField(max_length=10)
    fee_type = models.CharField(max_length=10)
    payment_date = models.DateField()