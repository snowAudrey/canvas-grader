import os
from dotenv import load_dotenv
from canvasapi import Canvas

#Read .env and make these variables available
load_dotenv()

# Get Canvas API credentials from .env
API_TOKEN = os.getenv("CANVAS_API_TOKEN")
API_URL = os.getenv("CANVAS_API_URL")
COURSE_ID = os.getenv("CANVAS_COURSE_ID")

#initialize a new Canvas object
canvas = Canvas(API_URL, API_TOKEN)

#get the Canvas course
course = canvas.get_course(COURSE_ID)

#print course name to verify connection
print(f"Successfully connected to course: {course.name}")
print(f"Course ID: {course.id}")
