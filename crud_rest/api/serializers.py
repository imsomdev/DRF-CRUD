from .models import Student
from rest_framework.serializers import ModelSerializer


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'stu_name', 'stu_address', 'stu_uid']
