import requests
import json
from Course import Course

# INSERT YOUR CANVAS API TOKEN HERE
AUTH_TOKEN = '1109~CaCWLep5armHkvr8XEboNc7UeByCurf77kOLPelxLSugYLQ9S3hTTrNlnFf0GNP5'

test_url = 'https://canvas.instructure.com/api/v1/courses.json/?per_page=100'
headers = {'Authorization' : 'Bearer ' + AUTH_TOKEN}

# request all courses
r = requests.get(test_url, headers = headers)
outputtxt = json.loads(str(r.text))

# initialize course objects
courses = []
for i in range(len(outputtxt)):
    # check if the course is restricted by date
    # if so, we won't be able to access any data so we must skip it
    try:
        outputtxt[i]['access_restricted_by_date']
    # if it's not restricted, we can initialize and store in list of courses
    except KeyError:
        courses.append(Course(outputtxt[i]))

# print all course names
for course in courses:
    course.show_course()
