from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import datetime, timedelta

from models import Base, Student, Group, Teacher, Subject, Grade

fake = Faker()
engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

# Створення груп
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(fullname=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

# Створення предметів
subjects = [Subject(name=fake.word(), teacher_id=random.choice(teachers).id) for _ in range(5)]
session.add_all(subjects)
session.commit()

# Створення студентів
students = []
for _ in range(30):
    group = random.choice(groups)
    student = Student(fullname=fake.name(), group_id=group.id)
    students.append(student)
session.add_all(students)
session.commit()

# Створення оцінок
for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 20)):
            grade = Grade(grade=random.uniform(5, 10), student_id=student.id, subject_id=subject.id,
                          date_received=datetime.now() - timedelta(days=random.randint(1, 365)))
            session.add(grade)
session.commit()