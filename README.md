# Canvas Autograder

## Overview
This tool connects to a Canvas course, retrieves assignments, and selects the eligible assignments for autograding. It performs a dry run to show the user what assignments will be graded, then automatically grades the eligible assignments after receiving user confirmation. 

## Purpose
Instructors in higher education have been experiencing burnout in recent years due to various factors, including financial difficulties at institutions, heavier teaching loads, and a significant rise in administrative tasks. According to the 2025 Anthology Faculty Survey, which collected responses from 2,500 instructors at US-based institutions, 6 out of 10 instructors report their workload has increased in the past five years. The survey suggests that many instructors are teaching more courses and class sizes have often increased.  During one academic term in 2026, I taught 78 students without a teaching assistant or grader. Therefore, I built this tool to help automate completion-based grading on Canvas (a cloud-based learning management system).  

See "Addressing the Hidden Crisis: The Realities of Faculty Burnout and What Comes Next" by Anthology: https://backstage.anthology.com/sites/default/files/2025-08/AddressingTheHiddenCrisisTheRealitiesOfFacultyBurnout_WhitePaper_v1.pdf 

## Features
- Connects to Canvas API securely
- Filters assignments intelligently: 
  - Published assignments only
  - Assignments with online submissions (to preserve instructor judgment on presentations, paper-based exams, etc.)
  - Assignments whose due dates have passed 
- Handles late submissions (Late submissions do not lose points)
- Re-grades students who submitted after receiving a 0
- Shows dry-run summary and asks for confirmation before grading
- Protected with `.gitignore` (no API tokens exposed)

## How It Works
- Connects to your Canvas course
- Retrieves and filters assignments based on: 
  - Published status
  - Due date has passed
  - Has online submission types (skips presentations and paper-based exams)
  - Not already graded (or has late submissions)
- Displays a summary of assignments to be graded
- Asks for confirmation: "Do you want to proceed with grading? (yes/no):"
- If you type "yes," the program automatically grades these assignments on Canvas


## Setup Instructions

### Prerequisites 
- Python 3.x installed on your computer
- A Canvas account with instructor access to a course
- Canvas API token (see below for how to get one)

### Installation Steps

1. **Download the project**
  - Download this project: 
    - Go to https://github.com/snowAudrey/canvas-grader
    - Click the green "Code" button
    - Click "Download ZIP"
    - Unzip the file to a folder on your computer (e.g., Desktop/canvas-grader)

2. **Set up a virtual environment**
```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Mac/Linux
   # OR
   .venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Create a `.env` file**
   - In your project folder, create a file named `.env`
   - Add the following lines (no spaces around the `=`):
```
   CANVAS_API_TOKEN=your_token_here
   CANVAS_API_URL=https://canvas.youruniversity.edu
   CANVAS_COURSE_ID=your_course_id_here
```

5. **Get your Canvas information**

   **Canvas API URL:**
   - Go to your Canvas course
   - Look at the URL: `https://canvas.university.edu/courses/123456`
   - Your `CANVAS_API_URL` is: `https://canvas.university.edu`

   **Canvas Course ID:**
   - From the same URL: `https://canvas.university.edu/courses/123456`
   - Your `CANVAS_COURSE_ID` is: `123456` (the number after `/courses/`)

   **Canvas API Token:**
   - Log into Canvas
   - Go to **Account → Settings**
   - Scroll down to **Approved Integrations**
   - Click **+ New Access Token**
   - Give it a name (e.g., "Canvas Autograder")
   - Click **Generate Token**
   - **Copy the token immediately** (you won't see it again!)
   - Paste it into your `.env` file

6. **Your `.env` file should look like this:**
```
   CANVAS_API_TOKEN=1234~abcdefghijklmnopqrstuvwxyz
   CANVAS_API_URL=https://canvas.yourschool.edu
   CANVAS_COURSE_ID=123456
```


## Usage

### Running the Autograder 

1. **Activate your virtual environment** (if not already active)
```bash
   source .venv/bin/activate  # Mac/Linux
   # OR
   .venv\Scripts\activate  # Windows
```

2. **Run the program**
```bash
   python autograder.py
```

3. **Review the dry-run summary**
   - The program will show you which assignments will be graded
   - Review the list carefully

4. **Confirm or cancel**
   - Type `yes` to proceed with grading
   - Type `no` to cancel (no changes will be made)

5. **Verify on Canvas**
   - Go to your Canvas course gradebook to confirm grades were applied correctly

## Requirements
- Python 3.7 or higher
- Canvas API access (instructor role)
- Libraries: `canvasapi`, `python-dotenv` (installed via `requirements.txt`)

## Future Enhancements
- Add content detection to verify if students submitted meaningful content (not empty documents)
- Expand to web application or browser extension for easier use by non-technical instructors  

## Notes
- This tool is designed for **completion-based grading only** (complete/incomplete or full points/zero points)
- Always review the dry-run summary before confirming
- Your `.env` file is protected by `.gitignore` and will never be pushed to GitHub
- This project was built with guidance from Claude AI

## License
MIT License - see the [LICENSE](LICENSE) file for details

## Questions or Issues?
If you encounter any problems or have questions, please open an issue on GitHub.