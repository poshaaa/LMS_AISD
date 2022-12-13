from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name','teacher_profile_img', 'email', 'password', 'qualification', 'mobile_number']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','category', 'teacher', 'title', 'descriprion', 'cousre_img']