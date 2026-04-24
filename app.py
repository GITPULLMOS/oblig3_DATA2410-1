# Import
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'students.db'

# Skala over karakterer
def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'D'

# VVV Database innhold her VVV

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    # Opprett tabell for studenter
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT    NOT NULL,
            course TEXT    NOT NULL DEFAULT 'DATA2410',
            marks  INTEGER NOT NULL,
            grade  TEXT
        )

    ''')
    conn.commit()
    conn.close()

# AAA Database innhold her AAA

# Endpoint 1: GET all students
@app.route('/api/students', methods=['GET'])
def get_all_students():
    conn = get_db()
    rows = conn.execute('SELECT * FROM Students').fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows]), 200
    

# Endpoint 2: GET student by ID
@app.route('/api/students/{id}', methods=['GET'])
def get_students(id):
    conn = get_db()
    row = conn.execute('SELECCT * FROM Students WHERE id = ?', (id,)).fetchone()
    conn.close()
    if row is None:
        return jsonify({'error': 'Student ikke funnet'}), 404
    return jsonify(dict(row)), 200

# Endpoint 3: POST new student
@app.route('/api/students', methods=['POST']) 
def create_student():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body må være JSON'}), 400
 
    name   = data.get('name')
    course = data.get('course', 'DATA2410')
    marks  = data.get('marks')

    if name is None or marks is None:
        return jsonify({'error': 'name og marks er påkrevd'}), 400
 
    conn = get_db()
    cursor = conn.execute(
        'INSERT INTO Students (name, course, marks) VALUES (?, ?, ?)',
        (name, course, marks)
    )
    conn.commit()
    new_student = conn.execute(
        'SELECT * FROM Students WHERE id = ?', (cursor.lastrowid,)
    ).fetchone()
    conn.close()
    return jsonify(dict(new_student)), 201

# Endpoint 4: PUT update student
@app.route('/api/students/{id}', methods=['PUT'])
def update_student(id):
    conn = get_db()
    row = conn.execute('SELECT * FROM Students WHERE id = ?', (id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({'error': 'Student ikke funnet'}), 404
 
    data   = request.get_json()
    name   = data.get('name',   row['name'])
    course = data.get('course', row['course'])
    marks  = data.get('marks',  row['marks'])
 
    conn.execute(
        'UPDATE Students SET name = ?, course = ?, marks = ? WHERE id = ?',
        (name, course, marks, id)
    )
    conn.commit()
    conn.close()
    return '', 204

# Endpoint 5: DELETE student
@app.route('/api/students/{id}', methods=['DELETE'])
def delete_student(id):
    conn = get_db()
    row = conn.execute('SELECT * FROM Students WHERE id = ?', (id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({'error': 'Student ikke funnet'}), 404
 
    conn.execute('DELETE FROM Students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return '', 204

# Endpoint 6: POST calculate grade for student
@app.route('/api/students/calculate-grades', methods=['POST'])

# Endpoint 7: GET report of courses and average grades
@app.route('/api/students/report', methods=['GET'])

# Endpoint 8: GET health check
@app.route('/health', methods=['GET'])
def health_check():
    # Midlertidig for å ikke få feilmelding, skal implementeres senere
    return 'OK', 200


# Verdier for å fylle opp databasen
def fyll_db():
    students = [
        ('Syver', 'DATA2410', 85),
        ('Omran', 'DATA2410', 92),
        ('Sjur', 'DATA2410', 90),
        ('Vetle', 'DATA2410', 88),
        ('Syver', 'DATA2410', 85),
        ('Omran', 'DATA2410', 92),
        ('Sjur', 'DATA2410', 90),
        ('Vetle', 'DATA2410', 88),
    ]
    # Må legger verdier inn i databasen her

if __name__ == '__main__':
    init_db()
    fyll_db()
    app.run(debug=True)