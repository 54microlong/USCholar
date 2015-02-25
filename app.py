#coding:utf-8

import os

from USCholar import uscApp
## when deploy to heroku please comment this line
from config import *

if __name__ == "__main__":
    uscApp.config.from_object(__name__)
    # [Heroku]load DB environment from env
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    uscApp.run(port=PORT,host=HOST)
