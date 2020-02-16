from socket import *
import pymongo
import random
import os
import time
import numpy as np
conn=pymongo.MongoClient(host="localhost",port=27017)

def connect_mongodb():
    #For db with password, https://blog.csdn.net/a540366413/article/details/60142462
    user = 'root'
    pwd = '12345'
    host = 'localhost' #To test, this is local
    port = 27017

    conn = pymongo.MongoClient(host = host, port = port)
    # db = conn[db_name]
    return conn


def save_data(condition, time_parking):
    db_name = 'Parking'
    conn = connect_mongodb()
    db = conn[db_name]
    collection_name = 'Parking'
    collection = db[collection_name]
    condition = 'Parked' if condition == '1' else 'Unparked'
    time_changed = time_parking
    data = {
        'State': condition,
        'Time_Changed': time_changed
    }
    try:
        result = collection.insert(data)
        print(result)
    except Exception as e:
        print(e)
    else:
        print('Insert successful')
        conn.close()

def get_data():
    s = socket(AF_INET, SOCK_STREAM)
    host = ''
    port = 12345
    s.bind((host, port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        if not data:
            break
        data_byte = data.decode().split(',')
        condition = data_byte[0]
        time_parking = data_byte[1]
        print(condition, time_parking)
        save_data(condition, time_parking)

    conn.close()


if __name__ == '__main__':
    get_data()