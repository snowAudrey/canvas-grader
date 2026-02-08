import os
from dotenv import load_dotenv
from canvasapi import Canvas

#Step1: Canvas API authenticaiton & setup

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

#get all assignments from this course
print("\nRetrieving assignments...")
assignments = course.get_assignments()

print("\nAll assignments in this course:")
for assignment in assignments:
    print(f"\n- {assignment.name} (ID: {assignment.id})")
    print(f"    Grading Type: {assignment.grading_type}")
    print(f"    Published: {assignment.published}")
    print(f"    Submission types: {assignment.submission_types}")

#Step2: Filter assignments
#filter assignments for auto-grading
print("\n")
print("="*50)
print(f"Assignments eligible for auto-grading after filtering")
print("="*50)

eligible_assignments = []
for assignment in assignments:
    #skip unpublished assignments
    if not assignment.published:
        continue

    #skip assignments with no online submission
    if assignment.submission_types == ["none"]:
        continue

    #this assignment is eligible for auto-grading
    eligible_assignments.append(assignment)
    print("\n")
    print(f"✓ {assignment.name}")
    print(f"    Grading Type: {assignment.grading_type}")
    print(f"    Submission types: {assignment.submission_types}")

print("\n\n")
print(f"Total eligible assignments: {len(eligible_assignments)}")

#Step3: The auto-grading logic