import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import random
import time
from datetime import datetime
import testexport
from threading import Thread


#ACCESS_TOKENS for devices
SmAl_tokens = ["EUzim0WLqTlbksaZ8CKM","pjrSBdBuaRKD15f5A5Fg","U2YXcEGfE1EI80WbcvzQ", "8iWx3Vosoj26vTh2FKwo", "zOZmDxGorkjmQzXYPjK1", "yS3MEk7w0VQ3ENhwkQDA", "tXRLX6RDD08bXz9RbEX4", "UR8CsbDVf34luqHGpQV5", "nmpRMAMkqWUpFgVRx5qQ", "eTIXZa42g6M8aFKXy4Ar"]
Dest_tokens = ["Yl5XT3RuokftknhlONoq", "cgRUEWTh08nLUUanC84B", "czYW66xyICSQMrnpIaz8", "7tPbHyDbbbYDeBHXKl17", "9Mk2rFyReqKRgpMVQPZi", "e9HsuZ7yW9gisUHnWBYD", "ZUFW8ejdwstFiHH9pkCU", "kLdSDTOYy8rkx7VHnXAz", "kViU0vw1kTdMPzTb4XU4", "zZXOBsmQM5AaAS342nHO"]
Cap_tokens = ["6VHBW3EQYOve6oJBc7OG", "F0DAUushDcfKyz1cvLsX", "BvdD2LH2At2KRv9xDQb3", "QW2LjvEhVLLmushBFypX", "2fKZ2zRkQBh4VwO8NeBZ", "WHw6lmVm1LONQmoWnTrQ", "Gw2Zt60msU0ZHuDnczBN", "FFVUvOMvqo1FHTjYxznG", "p0kTvmd6t4gWv2w2ZKuF", "IjoH9tjeEQrAet2nwDlD"] 
																																																												
broker="localhost"   			   
port=1883 		
                                                      
def createJSON(name, _id, prop, val):
    data = {																	
        "id": _id,
        "name": name,     
        prop: val
    }

    #запись в файл
    return json.dumps(data) 


def on_publish(client,userdata,result):            
    print("Succsess\n")
    pass


def mqtt_connect(tokens, clients):
    for i in range(len(tokens)):
      clients.append(paho.Client(""))

    for client in clients:
       client.on_publish=on_publish
       client.username_pw_set(tokens[clients.index(client)])
       client.connect(broker,port,keepalive=60)
       client.loop_start()

def mqtt_publish(clients,name, prop, val):

    d = m = False

    for client in clients:

      if (val == 'd'):
        val = round(random.uniform(1,35), 3)
        d = True
        # print("val of "+str(clients.index(client))+": "+str(val))

      elif(val == 'm'):
        m = True
        val = random.randint(0,1)                  

      payload = createJSON(name, str(clients.index(client)), prop, val)
      ret = client.publish("v1/devices/me/telemetry",payload)
      
      if d == True:
        val = 'd'
      if m == True:
        val = 'm'

      #Debug
      print(name+": ", payload, ret)
      # print(payload)
      # print(ret)
      # print("\n")

#for SmokeAlarm
clients_SmAl = []

mqtt_connect(SmAl_tokens,clients_SmAl)

#for Destination
clients_Dest = []

mqtt_connect(Dest_tokens, clients_Dest)

#for Cap
clients_Cap = []
mqtt_connect(Cap_tokens, clients_Cap)


while True:
  
  #for SmokeAlam
  mqtt_publish(clients_SmAl,"SmokeAlarm",'smoke', '0') #сгенерировать единицу

  #for Destination
  mqtt_publish(clients_Dest, "Destination", 'destination', 'd')
  
  #for Cap
  mqtt_publish(clients_Cap, "Cap", 'move', 'm')

  # testexport.send_req(testexport.SmAl_id)
  # testexport.send_req(testexport.Dest_id)

  time.sleep(18)