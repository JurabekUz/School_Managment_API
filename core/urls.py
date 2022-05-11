from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import *

router = DefaultRouter()
router.register('categories',CategoryViewSet)
router.register('courses',CourseViewSet)
router.register('lessons',LessonViewSet)

urlpatterns = [
    path('home/', home, name='home'),
    path('',include(router.urls)),
    path('subjects/', SubjectList.as_view(),name='subject_list'),
    path('student/<int:pk>/', SubjectDetail.as_view(), name = 'student_course'),
    #path('teacher/<int:pk>/', TeacherCourse.as_view(), name = 'teacher_course'),
]