from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=100,unique=True)
    hod_name =  models.CharField(max_length=100,blank=True)

# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=100,unique=True)
#     department = models.ForeignKey(
#         Department,
#         on_delete=models.CASCADE
#         related_name='course',
#     )
#     semester = models.SmallIntegerField(default=1)
#     credits = models.SmallIntegerField(default=1)

class Student(models.Model):
    GENDER_CHOICES=[('M','Male'),('F','Female'),('0','other')]
    roll_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,blank=True)
    date_of_birth = models.DateField(null=[True,blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    department =  models.ForeignKey(Department,on_delete=models.PROJECT,related_name='students')
    year_of_students = models.TextField(blank=True)
    adddress = models.TextField(blank=True)
    photo = models.ImageField(upload_to='students_photos/',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    admitted_on = models.DateField(default=timezone.now)
    created_at = models.DateTimerField(auto_now_add=True)
    
    
                                    