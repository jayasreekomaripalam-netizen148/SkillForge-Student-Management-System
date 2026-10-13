# Student Management System

A Python command-line application for managing student records.

## Features
- Add new student records
- View all students
- Search by student ID or name
- Update existing student details
- Delete records with confirmation
- Store data persistently in JSON format

## Requirements
- Python 3.8 or newer
- No external packages required

## Run the application

```bash
python main.py
```

## Storage
Student records are stored in `data/students.json`.

## Project Structure

```text
student-management-system/
├── main.py
├── README.md
├── requirements.txt
├── data/
│   └── students.json
└── screenshots/
```

## Learning Outcomes
Python functions, dictionaries, loops, conditional statements,
exception handling, JSON serialization, and file handling.

## Internship
SkillForge Python Internship - Project 1

## Automated Tests

Run the test suite using:

```bash
python -m unittest discover -s tests -v
```

The tests cover student creation, duplicate ID prevention, searching,
deletion, and persistent JSON storage.
