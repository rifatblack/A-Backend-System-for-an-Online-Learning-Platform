
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.get_courses, name='get_courses'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:pk>/', views.get_course_by_id, name='get_course_by_id'),
    path('courses/filter/', views.filter_courses, name='filter_courses'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('enrollment/validate/', views.validate_enrollment, name='validate_enrollment'),
]
