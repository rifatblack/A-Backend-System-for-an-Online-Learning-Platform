
from .models import Course, Enrollment
from rest_framework.response import Response
from rest_framework import status


class CourseService:
    @staticmethod
    def get_courses():
        return Course.objects.all()

    @staticmethod
    def create_course(title, description, instructor, duration, price):
        return Course.objects.create(title=title, description=description, instructor=instructor, duration=duration, price=price)

    @staticmethod
    def get_course_by_id(course_id):
        return Course.objects.get(course_id=course_id)

    @staticmethod
    def filter_courses(**kwargs):
        return Course.objects.filter(**kwargs)

class EnrollmentService:
    @staticmethod
    def enroll_student(student_name, course_id):
        course = CourseService.get_course_by_id(course_id)
        return Enrollment.objects.create(student_name=student_name, course=course)

    @staticmethod
    def validate_enrollment(enrollment_id):
        try:
            enrollment = Enrollment.objects.get(enrollment_id=enrollment_id)
            if enrollment: 
                return True
        except Enrollment.DoesNotExist:
            return False
