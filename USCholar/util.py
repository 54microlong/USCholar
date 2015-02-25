# app.utils

from datetime import datetime
import time

"""
Convert string date to datetime type
date_str format `1991-11-30 10:20:12`
"""
def String2Datetime(date_str):
    dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt_obj



if __name__ == "__main__":
    """ UniTest for util """
    stringData = datetime.now()
    dataString = stringData.__str__().split('.')[0] 
    print(dataString)
    print(String2Datetime(dataString))
