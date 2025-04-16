from rest_framework import serializers
from .models import Module, Speciality, Teacher, Category, Lesson, Homework, Resource
from authentication.service.serializers import UserDetailSerializer

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id','speciality', 'price']


# Teacher serializer
class TeacherSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'

# Get categories
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

# Get speciality serializer
class SpecialitySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    teacher = TeacherSerializer()
    class Meta:
        model = Speciality
        fields = '__all__'


# Get lesson serializer
class LessonSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()
    class Meta:
        model = Lesson
        fields = '__all__'
    
    
# Get homework serializer
class HomeworkSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    class Meta:
        model = Homework
        fields = '__all__'
        

# Get resource serializer
class ResourceSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    class Meta:
        model = Resource
        fields = '__all__'