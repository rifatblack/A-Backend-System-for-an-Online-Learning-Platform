# models.py
from django.db import models


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  # Allow null and blank

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
