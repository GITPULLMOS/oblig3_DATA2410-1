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
@app.route('/api/students', methods=['GET'])

# Endpoint 2: GET student by ID
@app.route('/api/students/{id}', methods=['GET'])

# Endpoint 3: POST new student
@app.route('/api/students', methods=['POST'])

# Endpoint 4: PUT update student
@app.route('/api/students/{id}', methods=['PUT'])

# Endpoint 5: DELETE student
@app.route('/api/students/{id}', methods=['DELETE'])

# Endpoint 6: POST calculate grade for student
@app.route('/api/students/calculate-grades', methods=['POST'])

# Endpoint 7: GET report of courses and average grades
@app.route('/api/students/report', methods=['GET'])

# Endpoint 8: GET health check
@app.route('/health', methods=['GET'])