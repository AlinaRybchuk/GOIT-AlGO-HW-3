from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    students = relationship('Student', back_populates='group')

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    
    subjects = relationship('Subject', back_populates='teacher')

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')

class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer, primary_key=True)
    grade = Column(Float, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    date_received = Column(Date)

    subject = relationship('Subject', back_populates='grades')
    student = relationship('Student', back_populates='grades')

DATABASE_URL = "sqlite:///mynotes.dbS"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

# Створення сесії для виконання запитів
Session = sessionmaker(bind=engine)
session = Session()

# Функції для додавання даних
def add_student(fullname, group_name):
    group = session.query(Group).filter_by(name=group_name).first()
    if not group:
        group = Group(name=group_name)
        session.add(group)
        session.commit()
    new_student = Student(fullname=fullname, group=group)
    session.add(new_student)
    session.commit()
    print(f"Student {fullname} added to group {group_name}.")

def add_teacher(fullname):
    new_teacher = Teacher(fullname=fullname)
    session.add(new_teacher)
    session.commit()
    print(f"Teacher {fullname} added.")

def add_subject(name, teacher_fullname):
    teacher = session.query(Teacher).filter_by(fullname=teacher_fullname).first()
    if not teacher:
        teacher = Teacher(fullname=teacher_fullname)
        session.add(teacher)
        session.commit()
    new_subject = Subject(name=name, teacher=teacher)
    session.add(new_subject)
    session.commit()
    print(f"Subject {name} added under teacher {teacher_fullname}.")

# Отримання та виведення всіх студентів
def get_all_students(session):
    students = session.query(Student).all()
    return students

if __name__ == "__main__":
    with Session() as session:
       students = get_all_students(session)
       for student in students:
          print(f"ID: {student.id}, Name: {student.fullname}, Group ID: {student.group_id}")

    