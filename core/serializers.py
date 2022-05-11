from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Category,Course, Subject, Lesson

class CategorySlz(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CourseSlz(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class LesssonSlz(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

    def validate_source(self, value):
        if not value.endswith('.pm4'):
            raise ValidationError(detail="Siz video formatdagi url kiritmadingiz!")
        return value

class SubjectSlz(ModelSerializer):
    course = CourseSlz
    class Meta:
        model = Subject
        fields = ('student', 'course')