from django.db import models
from authentication.models import User
from django.core.validators import MinValueValidator


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}"
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ['user__username']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name



class Speciality(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    picture = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_who = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    what_will_you_learn = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    
    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'
    
    def __str__(self):
        return self.name



class Module(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
    
    def __str__(self):
        return self.name



class Lesson(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    source = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
    
    def __str__(self):
        return self.name



class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    source = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Homework'
        verbose_name_plural = 'Homeworks'
    
    def __str__(self):
        return self.lesson.name


class Resource(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    source = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'
    
    def __str__(self):
        return self.lesson.name