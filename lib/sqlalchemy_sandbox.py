#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection
engine = create_engine('sqlite:///students.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    # Create the database tables
    Base.metadata.create_all(engine)

    # Example: Add a student to the database
    new_student = Student(name="John Doe")
    session.add(new_student)
    session.commit()

    # Query the database
    students = session.query(Student).all()
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}")

    # Close the session
    session.close()
