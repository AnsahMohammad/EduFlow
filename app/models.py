from django.db import models

# Create your models here.


class Parent(models.Model):
    father_name = models.CharField(max_length=30,null=False,blank=False)
    f_occupation = models.CharField(max_length=20)
    f_phone_no = models.CharField(max_length=10)
    mother_name = models.CharField(max_length=30,null=False,blank=False)
    m_occupation = models.CharField(max_length=20) 
    m_phone_no = models.CharField(max_length=10) 
    address = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.father_name)
    

class Student(models.Model):
    fname = models.CharField(max_length=30,null=False,blank=False)
    lname = models.CharField(max_length=30,null=False,blank=False)
    dob = models.DateField()
    mothertounge = models.CharField(max_length=10)
    admission_no = models.CharField(max_length=10)
    st_par = models.OneToOneField(Parent,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self) :
        return str(self.admission_no)
    

class Teacher(models.Model):
    t_fname = models.CharField(max_length=30,null=False,blank=False)
    t_lname = models.CharField(max_length=30,null=False,blank=False)
    dob = models.DateField()
    t_phone_no = models.CharField(max_length=10)

    def __str__(self) :
        return str(self.t_lname)
    

class Fee(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    fee_paid = models.CharField(max_length=10)
    fee_remaining = models.CharField(max_length=10)
    history = models.DateField()

    def __str__(self):
        return str(self.student.admission_no)
    



