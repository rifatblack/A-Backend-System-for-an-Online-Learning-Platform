
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import CourseService, EnrollmentService
from .serializers import CourseSerializer, EnrollmentSerializer
from .models import Course, Enrollment

@api_view(['GET'])
def get_courses(request):
    courses = CourseService.get_courses()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        instructor = serializer.validated_data.get('instructor')
        duration = serializer.validated_data.get('duration')
        price = serializer.validated_data.get('price')

        CourseService.create_course(title, description, instructor, duration, price)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_course_by_id(request, pk):
    try:
        course = CourseService.get_course_by_id(pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course)
    return Response(serializer.data)

@api_view(['GET'])
def filter_courses(request):
    instructor = request.query_params.get('instructor')
    price = request.query_params.get('price')
    duration = request.query_params.get('duration')

    filters = {}
    if instructor:
        filters['instructor'] = instructor
    if price:
        filters['price'] = price
    if duration:
        filters['duration'] = duration

    courses = CourseService.filter_courses(**filters)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def enroll_student(request):
    student_name = request.data.get('student_name')
    course_id = request.data.get('course_id')

    if student_name is not None and course_id is not None:
        try:
            course = CourseService.get_course_by_id(course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course does not exist'}, status=status.HTTP_404_NOT_FOUND)
        enrollment = EnrollmentService.enroll_student(student_name, course_id)
        if enrollment:
            return Response({'message': 'Enrollment created successfully'}, status=status.HTTP_201_CREATED)

    return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def validate_enrollment(request):
    enrollment_id = request.data.get('enrollment_id')
    course_id = request.data.get('course_id')
    student_name = request.data.get('student_name')
    if course_id is not None and student_name is not None:
        try:
            course = CourseService.get_course_by_id(course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Assuming validation is handled in the EnrollmentService
        is_valid = EnrollmentService.validate_enrollment(enrollment_id)
    return Response({'valid': is_valid}, status=status.HTTP_200_OK)
