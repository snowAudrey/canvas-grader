import os
from dotenv import load_dotenv
from canvasapi import Canvas
from datetime import datetime, timezone

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


#Step2: filter assignments
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

    #skip assignments whose due date has not passed yet
    if assignment.due_at:
        due_date = datetime.fromisoformat(assignment.due_at.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        if due_date > now:
            continue

    #this assignment is eligible for auto-grading
    eligible_assignments.append(assignment)
    print("\n")
    print(f"✓ {assignment.name}")
    print(f"    Grading Type: {assignment.grading_type}")
    print(f"    Submission types: {assignment.submission_types}")

print("\n\n")
print(f"Total eligible assignments: {len(eligible_assignments)}")


#Step3: auto-grade submissions with confirmation
print("\n")
print("="*50)
print(f"Auto-grading with Confirmation")
print("="*50)

#first pass: Dry run to see what will be graded
print(f"\nDry Run - Analyzing submissions...")
print("="*50)

#store submissions that need grading
submissions_to_grade = []

for assignment in eligible_assignments:
    for submission in assignment.get_submissions():
        #skip if already graded with no late submission
        if submission.grade is not None:
            #if students submitted after being graded, re-grade them
            if submission.submitted_at and submission.graded_at and submission.submitted_at > submission.graded_at:
                #late submission - needs regrading
                pass
            else:
                #already graded, no late submission - skip
                continue

        #determine what grade to apply
        if submission.workflow_state == "unsubmitted":
            if assignment.grading_type == "pass_fail":
                grade_to_apply = "incomplete"
            elif assignment.grading_type == "points":
                grade_to_apply = 0
            else:
                continue
        else:
            #student submitted - would give full credit
            if assignment.grading_type == "pass_fail":
                grade_to_apply = "complete"
            elif assignment.grading_type == "points":
                grade_to_apply = assignment.points_possible
            else:
                continue 
        
        #store this submission for grading
        submissions_to_grade.append({
            "assignment": assignment,
            "submission": submission,
            "grade": grade_to_apply
        })

#show summary
print("\nSummary of What Will be Graded: ")
print("="*50)

#group by assignment 
assignment_counts = {}
for item in submissions_to_grade:
    assignment_name = item["assignment"].name
    if assignment_name not in assignment_counts:
        assignment_counts[assignment_name] = 0
    else:
        assignment_counts[assignment_name] += 1

for assignment_name, count in assignment_counts.items():
    print(f"    • {assignment_name}: {count} submissions")

print(f"\n  Total: {len(submissions_to_grade)} submission will be graded.")
print("="*50)

#ask for confirmation
response = input("\nDo you want to proceed with grading? (yes/no):")
#second pass: actual grading after typing "yes"
if response.strip().lower() == "yes":
    print("\nStarting grading process...")
    print("="*50)

    graded_count = 0
    error_count = 0

    for item in submissions_to_grade:
        assignment = item["assignment"]
        submission = item["submission"]
        grade = item["grade"]

        try:
            submission.edit(submission = {"posted_grade": grade})
            print(f"   ✓ {assignment.name} - Student {submission.user_id}: {grade}")
            graded_count += 1
        except Exception as e:
            print(f"   ✗ Error = {assignment.name} - Student {submission.user_id}: {e}")
            error_count += 1
    
    print("\n")
    print("="*50)
    print(f"Grading Complete")
    print(f"    ✓ Successfully graded: {graded_count}")
    if error_count > 0:
        print(f"    ✗ Errors: {error_count}")
    print("="*50)
else:
    print(f"\nGrading cancelled. No changed were made to Canvas.")
    print("="*50)



       
