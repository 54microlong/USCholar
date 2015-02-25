#@ Database of USC application
#@ author Long Chen
#@ Date 2015-02-13

from flask import Flask, jsonify, request, session
from flask.ext.sqlalchemy import SQLAlchemy
from USCholar import *
from USCholar.model import *

@uscApp.route("/initdb")
# @requires_auth
def InitDB():
    db.drop_all()
    db.create_all()
    longchen = User('Long Chen', 'chenlong@usc.edu','5345346091','usc')
    pablo = User('pablo', 'bob@example.com','5345356789','usc')
    zihan = User('zihanTong', 'zihantong@example.com','4343245566','usc')
    david = User('david', 'david@example.com','4','44')
    # title, description, capacity, available, price, location, destination, event_date
    db.session.add(longchen)
    db.session.add(pablo)
    db.session.add(zihan)
    db.session.add(david)
    db.session.commit()
    return 'OK'

@uscApp.route("/listdb")
def ShowDB():
    l = [item.serialize for item in User.query.all()]
    #e = [item.serialize for item in Event.query.all()]
    #return jsonify(user = l, event = e)
    return jsonify(user = l)

@uscApp.route("/StudentsTest")
def testStudent():
    db.drop_all()
    db.create_all()

    stu_long = Student('Long', 'Chen', 'chenlong@usc.edu',
            'Viterbi', 'Computer Science', 'Master')
    sec_570 = Section('CSCI 570', 'Algorithms', '34532D')
    sec_561 = Section('CSCI 561', 'Artifical Intelligence', '34532D')
    sec_544 = Section('CSCI 544', 'Algorithms', '34534D')
    
    db.session.add(stu_long)
    db.session.add(sec_570)
    db.session.add(sec_561)
    db.session.add(sec_544)
 
    stu_long.sections.append(sec_570)
    stu_long.sections.append(sec_561)
    stu_long.sections.append(sec_544)

    db.session.commit()
    return "OK!"




