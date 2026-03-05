# Canvas Autograder

## Overview
This tool connects to a Canvas course site, get assignments from it and selects the assignments eligible for autograding. It then does a dry run to show the user what assignments will be graded and automatically grades the eligible assignments after the user gives permission. 

## Purpose
Instructors at higher education have been experiencing burnout in recent years due to various reasons (e.g., financial difficulties at institutions, heavier teaching loads, significant rise in adminstrative tasks). According to the 2025 Anthology Faculty Survey, which collected responses from 2500 instructors at US-based institutions, 6 out of 10 instructors report their workload has increased in the past five years. The survey suggests that many instructors are teaching more courses and the number of students in a course has often increased.  During one academic term in 2026, I taught 78 students without a teaching assistant or grader. Therefore, I built this tool to help automate completion-based grading on Canvas (cloud-based learning management system).  
See "Addressing the Hidden Crisis: The Realities of Faculty Burnout and What Comes Next" by Anthology: https://backstage.anthology.com/sites/default/files/2025-08/AddressingTheHiddenCrisisTheRealitiesOfFacultyBurnout_WhitePaper_v1.pdf 

## Features
- Connects to Canvas API securely
- Filters assignments intelligently: 
  - Published only
  - Has online submissions to preseve instructor judgment
  - Due date has passed 
- Handles late submissions
- Shows dry-run summary and asks for confirmation before automatically grading
- Protected with .gitignore (no API tokens exposed)

## How It Works
- Connects to the user's Canvas course site
- Gets assignments from it and filters assignments based on the following criteria: 
  - skipping assignments that are not published
  - skipping assignments whose due date has not passed
  - skipping assignments with no online submissions (e.g., presentations,     paper-based exams)
  - skipping assignments that were already graded
- Shows the user what assignments will be graded
- Asks the user if she/he/they wants the program to proceed with grading
- If the user types "yes," the program will autograde theses assignments on Canvas


## Setup Instructions
[How someone would set this up on their own computer - you can fill this in later or I can help]

## Usage
[How to run the program]

## Requirements
- Python 3.x
- Canvas API access
- [Any other requirements]

## Future Enhancements
[Things you plan to add later, like the text-detection feature from Step 2]

## Notes
This tool was built with the help of Claude Code. 