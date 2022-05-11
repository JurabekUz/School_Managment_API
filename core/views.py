from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework.decorators import action
from rest_framework.permissions import  IsAdminUser
from .permissions import IsTeacher, IsAdminOrOnlyRead, IsTeachAdminOrRead

from .serializers import SubjectSlz, CourseSlz, LesssonSlz, CategorySlz
from .models import *

def home(request):
    courses = Course.objects.all()
    return render(request, template_name='home.html',context={"courses":courses})

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrOnlyRead,)
    queryset = Category.objects.all()
    serializer_class = CategorySlz

    # category ga tegishli kurslarni korish uchun
    @action(methods=['GET'], detail=True)
    def clist(self,request, *args, **kwargs):
        cat = self.get_object()
        courses = Course.objects.filter(category=cat)

        serializer = CourseSlz(courses, many=True)
        return Response(data=serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes =(IsTeachAdminOrRead,)
    queryset = Course.objects.all()
    serializer_class = CourseSlz

    # kurs ga tegishli darslar ro'yxati
    @action(detail=True, methods=['GET'])
    def lessons(self, request, *args, **kwargs):
        course = self.get_object()
        lessons = Lesson.objects.filter(course_id=course.id)

        serializer = LesssonSlz(lessons, many=True)
        return Response(data=serializer.data)

    # teacher ga tegisli darslar ro'yxati
    @action(detail=False, methods=['GET'])
    def teacher(self, request, *args, **kwargs):
        teacher_id = request.user.id
        courses = Course.objects.filter(teacher=teacher_id)

        serializer = CourseSlz(courses, many=True)
        return Response(data=serializer.data)

    # admin panel da korinadigan data lar
    @action(detail=False, methods=['GET'])
    def all_data(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSlz(courses, many=True)
        return Response(data = serializer.data)

class LessonViewSet(viewsets.ModelViewSet):
    permission_classes =(IsTeachAdminOrRead,)
    queryset = Lesson.objects.all()
    serializer_class = LesssonSlz

class SubjectList(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request):
        subjects = Subject.objects.all()
        serializer = SubjectSlz(subjects, many=True)
        return Response(data=serializer.data)

class SubjectDetail(APIView):

    # studentga tegishli kurslar ro'yxati
    def get(self, request, pk):
        subject = Subject.objects.get(student_id=pk)
        student_courses = Course.objects.filter(course_subject=subject)

        serializer = CourseSlz(student_courses,many=True)
        return Response(data=serializer.data)

    # kursga yozilish
    def post(self, request, pk):
        user_id=pk
        subjects = Subject.objects.all()
        subject = get_object_or_404(subjects, student_id=user_id)

        if subject:
            subject = subject.course.add(request.data.get('course'))
            print("subject mavjud")
        else:
            print("subject mavjud emas")
            subject = Subject(student=user_id)
            subject.course.add(request.data.get('course'))

        subject = Subject.objects.get(student_id=user_id)
        serializer = SubjectSlz(subject)
        return Response(data=serializer.data)

    # kursdan chiqish
    def delete(self, request, pk):
        user_id = pk
        subject = Subject.objects.get(student_id=user_id)
        if subject:
            subject = subject.course.remove(request.data.get('course'))

        subject = Subject.objects.get(student_id=user_id)
        serializer = SubjectSlz(subject)
        return Response(data=serializer.data)







