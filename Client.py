import time
import pymongo
import pickle
import socket

DISCONNECT_MESSAGE = "DISCONNECT"
HEADER = 5000
FORMAT = 'utf-8'
print('Please enter server IP address: ')
serverip = input()
print('Please enter server port: ')
serverPort = int(input())

ADDR = (serverip, serverPort)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("Connecting to " + serverip + " on port " + str(serverPort))

botton1Pressed = True
botton2Pressed = False

def send(msg):
    client.send(msg.encode(FORMAT))
while True:
    #if button is pressed
    if botton1Pressed:
        send("1")
        time.sleep(1)
        received = client.recv(8000)
        received = pickle.loads(received)
        buttonInfo = received[0]
        personalInfo = received[1]
        location = buttonInfo["location"]
        address = buttonInfo["address"]
        curr_user = buttonInfo["curr_user"]
        age = personalInfo["age"]
        gender = personalInfo["gender"]
        illness = personalInfo["potential illness"]
        emergency_email1 = personalInfo["emergency_contact1"]
        emergency_email2 = personalInfo["emergency_cantact2"]
        emergencyPhone = personalInfo["emergency_phone_call"]
        print(received[0])
        print(received[1])
        break
    if botton2Pressed:
        send("2")
        time.sleep(1)
        received = client.recv(8000)
        received = pickle.loads(received)
        buttonInfo = received[0]
        personalInfo = received[1]
        location = buttonInfo["location"]
        address = buttonInfo["address"]
        curr_user = buttonInfo["curr_user"]
        age = personalInfo["age"]
        gender = personalInfo["gender"]
        illness = personalInfo["potential illness"]
        emergency_email1 = personalInfo["emergency_cantact1"]
        emergency_email2 = personalInfo["emergency_cantact2"]
        emergencyPhone = personalInfo["emergency_phone_call"]
        print(received[0])
        print(received[1])
        break
        break
