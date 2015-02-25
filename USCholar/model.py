#models

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref


db = SQLAlchemy()

"""
association table define
"""
association_student_section = db.Table('student_section', 
            Column('student_id', Integer, ForeignKey('student.student_id')),
                Column('section_id', Integer, ForeignKey('section.section_id'))
                )



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True) 
    student_id = db.Column(db.String(20), unique=True)
    password= db.Column(db.String(80))
    major=db.Column(db.String(80))
    description=db.Column(db.String(80))

    def __init__(self, name, email, student_id, password,
            major = '', description = ''):
        
        self.name = name
        self.email = email
        self.student_id = student_id
        self.password = password
        self.description = description
        self.major = major

        
    
    @property
    def serialize(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'student_id':self.student_id,
            'major':self.major,
            'description': self.description,
        }

class Student(db.Model):
    __tablename__ = "student"

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    school = db.Column(db.String(64))
    department = db.Column(db.String(64))
    degree = db.Column(db.String(64))
    data_birth = db.Column(db.DateTime)
    data_entrance = db.Column(db.DateTime)
    data_graduate = db.Column(db.DateTime)
   
    # Many to Many relationship
    sections = db.relationship('Section', secondary =
            association_student_section)

    def __init__(self, first_name, last_name, email, school, department, degree):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.school = school
        self.department = department
        self.degree = degree

    def GetSections(self, condition):
        return [sect.serialize for sect in self.sections]

    @property
    def serialize(self):

        return {
            'student_id' : self.student_id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'email' : self.email,
            'school' : self.school,
            'department' : self.department,
            'degree' : self.degree }

class Section(db.Model):
    __tablename__ = "section"

    section_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(64), unique=True)
    course_name = db.Column(db.String(64))
    section_number = db.Column(db.String(64))
    max_unit = db.Column(db.Integer)
    min_unit = db.Column(db.Integer)
    course_type = db.Column(db.String(64))
    begin_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    day = db.Column(db.String(64))
    instructor = db.Column(db.String(64))
    location = db.Column(db.String(64))
    website = db.Column(db.String(256))
    syllabus_link = db.Column(db.String(256))
    sis_course_id = db.Column(db.Integer)

    #many to many relationship
    students = db.relationship('Student', secondary =
            association_student_section)
    
    #foreign key
    session_id = db.Column(db.Integer, unique=True) 
    term_code = db.Column(db.String(64))

    def __init__(self, course_id, course_name, section_number):

        self.course_id = course_id
        self.course_name = course_name
        self.section_number = section_number
    
    def GetStudents(self, condition):
        return [stud.serialize for stud in self.students]

    @property
    def serialize(self):

        return {
            'section_id' : self.section_id,
            'course_id' : self.course_id,
            'section_number' : self.section_number
            }
            ##'first_name' : self.first_name,
            ##'last_name' : self.last_name,
            ##'email' : self.email,
            ##'school' : self.school,
            ##'department' : self.department,









