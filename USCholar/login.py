#coding:utf-8


from flask import Flask, jsonify, request, session
from flask.ext.sqlalchemy import SQLAlchemy
from USCholar.model import *
from USCholar import *

@uscApp.route('/')
def hello():
    return jsonify(login='login?user_mail=XXX&password=XXX', logout='logout',
            GetCourse='GetCourceByID?student_id=5345346093',
            GetEventByDay='GetEventByDay?student_id=X&day=150120',
            GetEventByWeek='GetEventByWeek?student_id=&week=150120-150127',
            GetEventByMonth='GetEventByMonth?student_id=XX&month=1-3',
            )

'Hello World!'

@uscApp.route('/login', methods=['GET'])
def login():
    
    _id = request.args.get('user_email')
    _pass = request.args.get('password')

    if _id == "chenlong@usc.edu" and _pass == "usc":
        return jsonify(status = 1, info = 'Login Successfully')
    else:
        return jsonify(info = 'Login fails', 
                user_email = 'chenlong@usc.edu', password = 'usc' )

@uscApp.route("/logout", methods=['GET'])
def logout():
    return jsonify(status = 0, info = 'Logout complete')


@uscApp.route("/GetCourseByID", methods=['GET'])
def GetCourseByID():

    _studentID = request.args.get('student_id')
    if _studentID == "5345346093":
        return jsonify(course1 = 'CSCI571', course2 = 'CSCI544', course3 = 'Math5441a')
    else:
        return jsonify(status = '4', infor = 'user session failed')

