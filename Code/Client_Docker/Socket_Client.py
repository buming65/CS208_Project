from socket import *
import pymongo
import random
import os
import time
import numpy as np

ip_client = gethostname()  # get ip of this node

def send_data(data):
    s = socket(AF_INET, SOCK_STREAM)
    # host = gethostname() #set to the server host, now just use this computer as both the server and client
    host = '192.168.1.2'
    # host =  #set host here
    port = 12345 #set port
    s.connect((host, port))
    data_byte = data.encode() #encode the data
    s.send(data_byte)
    s.close()

def generate_random():
    filename = os.path.abspath(os.path.dirname(os.getcwd())) + '/Data/' + ip_client + '.txt'
    print(filename)

    condition = random.randint(0,1)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(str(condition) + ',' + now)
            # f.write("\n")
    else:
        with open(filename, 'r') as f:
            lines = f.readlines()
            # print(lines)
            last_condition = lines[-1].split(',')[0]
        # print(last_condition)
        with open(filename, 'a') as f:
            condition = 1 if last_condition == '0' else 0
            f.write('\n' + str(condition)+ ',' + now)
    return condition, now

if __name__ == '__main__':
    # condition, time_now = generate_random()
    # print(condition, time_now)

    times = np.random.randint(10,size=2)
    times = times.tolist() #send the last condition
    times.append(0)
    print(times)
    #

    for i in times:
        condition, time_now = generate_random()
        send_data(str(condition) + ',' + time_now)
        time.sleep(i)
