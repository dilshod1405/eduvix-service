from .serializers import (
    ModuleSerializer,
    SpecialitySerializer,
    TeacherSerializer,
    CategorySerializer,
    LessonSerializer,
    HomeworkSerializer,
    ResourceSerializer,
)
from rest_framework import viewsets
from .models import Module, Speciality, Teacher, Category, Lesson, Homework, Resource
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsAuthenticated]



class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def get_specialities_by_category(self, request):
        category_id = request.query_params.get("category_id")
        if category_id:
            specialities = Speciality.objects.filter(category_id=category_id)
            serializer = self.get_serializer(specialities, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Category ID is required."}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=["get"])
    def get_specialities_by_teacher(self, request):
        teacher_id = request.query_params.get("teacher_id")
        if teacher_id:
            specialities = Speciality.objects.filter(teacher_id=teacher_id)
            serializer = self.get_serializer(specialities, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Teacher ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsAuthenticated]
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]
    

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated]
    

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    # permission_classes = [IsAuthenticated]
    

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    # permission_classes = [IsAuthenticated]

