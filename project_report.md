# Project Report: Student Gradebook

## Project Name

Student Gradebook

## Problem Statement

The goal of this project is to build a simple Python CLI application that manages students, subjects, marks, grades, and student performance reports. The application must validate important error cases, save data in a JSON file, and remain small, functional, and easy to explain.

## Approach

The solution was implemented as a command-line application using Python. The design was intentionally kept small:

- `main.py` handles user input and command parsing
- `gradebook.py` contains the main business logic
- `data.json` stores persistent data
- `test_gradebook.py` contains unit tests
- `README.md` documents setup and usage

The application uses a single `Gradebook` class to manage students, subjects, marks, grade calculation, persistence, and reports.

## Technologies Used

- Python 3
- JSON for persistence
- `unittest` for testing

All tools and resources used are free and zero-cost.

## Implemented Features

- Add student
- Add subject
- Add mark
- Generate student report
- List students
- List subjects
- Calculate grades using the required grading scale
- Validate unknown student, unknown subject, invalid marks, and duplicate marks
- Save and load data using `data.json`
- Support the simplified official test case `ADD S01 Ravi Python 82`

## Validation and Error Handling

The application handles the required important error cases:

- Marks outside `0-100`
- Student not found
- Subject not found
- Duplicate marks for the same student and subject
- Invalid commands

## Testing

Unit tests were added for:

- Grade boundaries:
  - `82 -> A`
  - `75 -> B`
  - `65 -> C`
  - `55 -> D`
  - `40 -> F`
- Invalid marks:
  - `105 -> Error`
  - `-5 -> Error`
- Student creation
- Subject creation
- Mark creation
- Duplicate marks
- Student report

Test command:

```bash
python3 -m unittest test_gradebook.py
```

Windows:

```bash
python.exe -m unittest test_gradebook.py
```

## Demonstration

Main workflow:

```text
ADD STUDENT S01 Ravi
ADD SUBJECT PYTHON Python
ADD MARK S01 PYTHON 82
REPORT S01
```

Important result:

```text
Student: Ravi
Subject: Python
Marks: 82
Grade: A
```

Official shorthand test case:

```text
ADD S01 Ravi Python 82
```

Output:

```text
A
```

## Conclusion

This project meets the required functionality with a small, readable, and testable design. The implementation focuses on correctness, validation, persistence, and ease of explanation rather than unnecessary complexity.
