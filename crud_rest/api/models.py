from django.db import models
import uuid

class Student(models.Model):
    stu_uid = models.CharField(max_length=100, blank=True, null = True, default=uuid.uuid4)
    stu_name = models.CharField(max_length=200)
    stu_address = models.CharField(max_length=200)
