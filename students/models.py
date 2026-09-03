from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=100,unique=True)
    hod_name =  models.CharField(max_length=100,blank=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100,unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
        related_name='course',
    )
    semester = models.SmallIntegerField(default=1)
    credits = models.SmallIntegerField(default=1)
