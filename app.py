# Import
from flask import Flask
import sqlite3

app = Flask(__name__)
DATABASE = 'students.db'

# Skala over karakterer
def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

# VVV Database innhold her VVV


# AAA Database innhold her AAA

# Endpoint 1: GET all students

# Endpoint 2: GET student by ID

# Endpoint 3: POST new student

# Endpoint 4: PUT update student

# Endpoint 5: DELETE student

# Endpoint 6: POST calculate grade for student

# Endpoint 7: GET report of courses and average grades

# Endpoint 8: GET health check