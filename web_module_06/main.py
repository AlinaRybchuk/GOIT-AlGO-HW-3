import logging
from psycopg2 import DatabaseError
from faker import Faker
import random
import psycopg2

fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(host='127.0.0.1', database='test', user='posrgres', password='123045')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''
CREATE TABLE groups (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);
''')

cursor.execute('''
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);
''')

cursor.execute('''
CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade DECIMAL(3, 2),
    date DATE,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
);
''')

# Заповнення таблиці груп
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (%s)", (group,))

# Заповнення таблиці викладачів
teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (%s)", (teacher,))

# Заповнення таблиці предметів
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
for subject in subjects:
    teacher_id = random.randint(1, len(teachers))
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (subject, teacher_id))

# Заповнення таблиці студентів
students = []
for _ in range(30):
    name = fake.name()
    group_id = random.randint(1, len(groups))
    cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s)", (name, group_id))
    students.append((name, group_id))

# Заповнення таблиці оцінок
for student_id in range(1, 31):
    for subject_id in range(1, len(subjects) + 1):
        for _ in range(random.randint(1, 20)):  # до 20 оцінок
            grade = round(random.uniform(2, 5), 2)  # оцінки від 2.0 до 5.0
            date = fake.date_between(start_date='-2y', end_date='today')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)",
                        (student_id, subject_id, grade, date))

try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
   # Закриття підключення
   cursor.close()
   conn.close()

    