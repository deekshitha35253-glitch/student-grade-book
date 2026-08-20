# Student Gradebook

## Problem Statement

Build a simple Python CLI application to manage students, subjects, marks, grades, and performance reports with JSON file persistence.

## Features

- Add students
- Add subjects
- Add marks
- Generate student reports
- List students
- List subjects
- Persist data in `data.json`

## How to Run

```bash
python3 main.py
```

## Input Format

```text
ADD STUDENT <student_id> <name>
ADD SUBJECT <subject_id> <subject_name>
ADD MARK <student_id> <subject_id> <marks>
REPORT <student_id>
LIST STUDENTS
LIST SUBJECTS
EXIT
```

For compatibility with the simplified official test case, the CLI also accepts:

```text
ADD <student_id> <name> <subject_name> <marks>
```

Example:

```text
ADD S01 Ravi Python 82
```

Output:

```text
A
```

## Output Format

The program prints a success message, error message, list output, or a student performance report based on the command entered.

## Example

```text
ADD STUDENT S01 Ravi
ADD SUBJECT PYTHON Python
ADD MARK S01 PYTHON 82
REPORT S01
```

Example output:

```text
Student added successfully.
Subject added successfully.
Mark added successfully.
Grade: A
Student: Ravi
Subject: Python
Marks: 82
Grade: A
Average Marks: 82.00
Performance: Excellent
Subjects Count: 1
```

## Test Command

```bash
python3 -m unittest test_gradebook.py
```
