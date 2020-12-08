import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime

ACCESS_TOKEN="rtuKJXx75nKESceUa3eH"                 #Token of your device
broker="demo.thingsboard.io"   			    #host name
port=1883 					    #data listening port

def on_connect(client,userdata,flags,rc):
  print("Connection result:"+str(rc)+"\n")

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard, code:\n" )
    pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client1.connect(broker,port,keepalive=60)
client1.on_connect=on_connect           #establish connection

while True:
  
   data = {
        "id": "1",
        "name": "SmokeAlarm",     #получение значения из имени файла
        "smoke": "1"
    }

   payload=json.dumps(data)
   ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
   print("Please check LATEST TELEMETRY field of your device")
   print(payload)
   time.sleep(5)
