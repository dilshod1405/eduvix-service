from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ModuleViewSet,
    TeacherViewSet,
    CategoryViewSet,
    SpecialityViewSet,
    LessonViewSet,
    HomeworkViewSet,
    ResourceViewSet
)

router = DefaultRouter()
router.register(r'modules', ModuleViewSet, basename='module')
router.register(r'specialities', SpecialityViewSet, basename='speciality')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'homeworks', HomeworkViewSet, basename='homework')
router.register(r'resources', ResourceViewSet, basename='resource')

urlpatterns = [
    path('', include(router.urls)),
]