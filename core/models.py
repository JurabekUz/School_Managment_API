from accounts.models import  User
from django.db import models

# course ( name category teacher, discription
# category ( name
# lesson ( name, course, source, discription
# subject (mycource) ( student, course)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, related_name='course', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='cat_course')

    def student_count(self):
        return self.course_subject.count()

    def lesson_count(self):
        return self.lesson.count()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    source = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson')

    def __str__(self):
        return f" {self.name} - {self.course} "

class Subject(models.Model): #mycourse
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subject')
    course = models.ManyToManyField(Course, related_name='course_subject' )

    def __str__(self):
        return str(self.student)