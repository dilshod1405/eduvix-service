from django.contrib import admin
from .models import Teacher, Category, Speciality, Module, Lesson, Homework, Resource

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'teacher', 'category', 'for_who', 'requirements', 'what_will_you_learn', 'duration', 'id')
    search_fields = ('name',)
    list_filter = ('teacher', 'category')
    ordering = ('name',)
    list_editable = ('description', 'for_who', 'requirements', 'what_will_you_learn', 'duration',)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'price', 'description', 'id')
    search_fields = ('name',)
    list_filter = ('speciality',)
    ordering = ('name',)
    list_editable = ('price', 'description',)
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user__username',)
    ordering = ('user__username',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'description', 'source', 'id')
    search_fields = ('name',)
    list_filter = ('module',)
    ordering = ('id',)
    list_editable = ('description', 'source',)
    
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'description', 'source', 'id')
    search_fields = ('lesson',)
    list_filter = ('lesson',)
    ordering = ('id',)
    list_editable = ('description', 'source',)
    

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'source', 'id')
    search_fields = ('lesson',)
    list_filter = ('lesson',)
    ordering = ('id',)
    list_editable = ('source',)