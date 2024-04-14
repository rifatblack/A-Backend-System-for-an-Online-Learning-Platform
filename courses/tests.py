
  
from django.test import TestCase
from rest_framework.test import APIClient
from .services import CourseService, EnrollmentService
from .models import Course, Enrollment
from faker import Faker
from rest_framework import status


class CourseServiceTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.course = Course.objects.create(
            title="Test Course",
            description="Test Description",
            instructor="Test Instructor",
            duration=5,
            price=50
        )

    def test_get_courses(self):
        courses = CourseService.get_courses()
        self.assertEqual(len(courses), 1)

    def test_create_course(self):
        title = self.fake.name()
        description = self.fake.text()
        instructor = self.fake.name()
        duration = self.fake.random_int(min=1, max=10)  
        price = self.fake.random_int(min=10, max=100)  
        course = CourseService.create_course(title, description, instructor, duration, price)
        self.assertEqual(course.title, title)

    def test_get_course_by_id(self):
        course = CourseService.get_course_by_id(self.course.course_id)
        self.assertEqual(course.title, "Test Course")


class EnrollmentServiceTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.course = Course.objects.create(
            title="Test Course",
            description="Test Description",
            instructor="Test Instructor",
            duration=5,
            price=50
        )
        self.enrollment = Enrollment.objects.create(student_name="Test Student", course=self.course)

    def test_enroll_student(self):
        student_name = self.fake.name()
        enrollment = EnrollmentService.enroll_student(student_name, self.course.course_id)
        self.assertEqual(enrollment.student_name, student_name)

    def test_validate_enrollment(self):
        self.assertTrue(EnrollmentService.validate_enrollment(self.enrollment.enrollment_id))


class CourseViewsTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.client = APIClient()
        self.course = Course.objects.create(
            title="Test Course",
            description="Test Description",
            instructor="Test Instructor",
            duration=5,
            price=50
        )

    def test_get_courses(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_course(self):
        data = {
            'title': self.fake.name(),
            'description': self.fake.text(),
            'instructor': self.fake.name(),
            'duration': self.fake.random_int(min=1, max=10),
            'price': self.fake.random_int(min=10, max=100)
        }
        response = self.client.post('/courses/create/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], data['title'])


class EnrollmentViewsTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.client = APIClient()
        self.course = Course.objects.create(
            title="Test Course",
            description="Test Description",
            instructor="Test Instructor",
            duration=5,
            price=50
        )
        self.enrollment = Enrollment.objects.create(student_name="Test Student", course=self.course)
       
    def test_enroll_student(self):
        data = {
            'student_name': self.fake.name(),
            'course_id': self.course.course_id
        }
        response = self.client.post('/enroll/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], 'Enrollment created successfully')

        enrollment_exists = Enrollment.objects.filter(student_name=data['student_name'], course=self.course).exists()
      
        self.assertTrue(enrollment_exists)

    def test_validate_enrollment(self):
        data = {
            'enrollment_id': 2,
            'student_name': 'Test Student',
            'course_id': self.course.course_id,
        }
        response = self.client.post('/enrollment/validate/', data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data['valid'])

