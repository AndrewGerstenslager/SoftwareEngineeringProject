# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://example.com"
# Canvas API key
API_KEY = "p@$$w0rd"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

SwEngCourse = 1533396


course = canvas.get_course(course=123456)
print(course.name)