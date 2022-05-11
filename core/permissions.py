from  rest_framework import permissions

from .models import Lesson, Subject
# category ni ozgartirish uchun faqat admin ruxsat bor, boshqalar koroladi
# course ni ozgartirish uchun faqat teacherga ruxsat bor, boshqalar koroladi
# lesson ni ozgartirish uchun faqat admin va teacherga ruxsat bor, boshqalar koroladi

class IsAdminOrOnlyRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

class IsTeachAdminOrRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_teacher or request.user.is_staff

class IsTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.is_teacher == True

