
# A Backend System for an Online Learning Platform 


This application provides an API for managing courses and student enrollments. It's built using Django, a popular web framework, and Django REST framework for creating APIs. I also use django-cors-headers to handle sharing resources across different origins.

To make it easy to understand how the API works, I've included drf_yasg for clear documentation. For testing, I use Django's built-in testing framework to ensure everything works smoothly.

Behind the scenes, data is stored in PostgreSQL, a reliable database system, to handle all the course and enrollment information effectively.
## Table of Contents

- Dependencies
- Installation
- API Endpoints
    - Get Courses
    - Create Course
    - Get Course by ID
    - Filter Courses
    - Enroll Student
    - Validate Enrollment
- Run Tests



## Dependencies

- Django
- Django REST Framework
- corsheaders
- drf_yasg



## Installation

#### 1. Clone the repository:

```bash
git clone https://github.com/rifatblack/A-Backend-System-for-an-Online-Learning-Platform 
cd A-Backend-System-for-an-Online-Learning-Platform
```

#### 2. Build the Docker container:

```bash
docker-compose build
```
#### 3. Run the Docker containers:

```bash
docker-compose up
```
#### 4. Access the API at http://localhost:8000/
    
## API Endpoints

#### Retrieve a list of all courses

```http
  GET /courses/
```
- **Description:** Retrieve a list of all courses.
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:** List of courses in JSON format.

#### Create a new course

```http
  POST /courses/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Title of the course |
| `description`      | `string` | **Required**. Description  of the course |
| `instructor`      | `string` | **Required**. instructor of the course |
| `duration`      | `string` | **Required**. Duration of the course in Minutes |
| `price`      | `string` | **Required**. Price of the course |

- **Description:** Create a new course.
- **Response:**
  - **Status Code:** `201 Created`
  - **Body:** Details of the created course in JSON format.



#### Get Course by ID

```http
  GET /courses/${id}/
```
- **Description:** Retrieve details of a specific course by its ID.
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:** Details of the course in JSON format.





#### Filter Courses

```http
  GET /courses/filter/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `instructor`      | `string` | **Optional**. Filter courses by instructor name |
| `price`      | `float` | **Optional**. Id of item to fetch |
| `duration`      | `integer` | **Optional**. Id of item to fetch |
- **Description:** Filter courses based on instructor, price, and duration.
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:** List of filtered courses in JSON format.


#### Enroll Student

```http
  POST /enroll/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `student_name`      | `string` | **Required**. Filter courses by instructor name |
| `course_id`      | `integer` | **Required**. Id of item to fetch |

- **Description:** Enroll a student in a course.
- **Response:**
  - **Status Code:** `201 Created`
  - **Body:** Details of the enrollment in JSON format.

  #### Validate Enrollment

```http
  POST /enrollment/validate/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `enrollment_id`      | `string` | **Optional**.  ID of the enrollment (if available) |
| `course_id`      | `float` | **Required**. Id of item to fetch |
| `student_name`      | `integer` | **Required**. Id of item to fetch |
- **Description:** Validate a student's enrollment.
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:** `valid` (boolean): Indicates whether the enrollment is valid.




## Run Tests

To run tests, run the following command

```bash
  docker-compose run web python manage.py test
```


## Authors

- [@rifatblack](https://github.com/rifatblack/)


## License

[MIT](https://choosealicense.com/licenses/mit/)

