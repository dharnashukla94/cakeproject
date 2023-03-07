from django.db import models

# Create your models here.
class Course(models.Model):
    cid = models.CharField(primary_key=True, max_length=30)
    course_name = models.CharField(max_length=30)
    duration = models.CharField(max_length=20)

class StudentDetails(models.Model):
    sid = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=40)
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
