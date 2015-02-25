# app.__init__

from flask import Flask, Response, json
from model import *

# create flask application object
uscApp= Flask(__name__)
db.init_app(uscApp)


# Register handlers
# must after application object is created
import USCholar.db
import USCholar.login
#import app.database
# import app.login
# import app.event
# import app.profile
# import app.push
# import app.views
