import requests
import time 

headers={
			'Accept': 'application/json',
			'X-Authorization':  'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiI3MzNmMjI0MC0xYmI1LTExZWItOTA0MC0yMTU2YjMzMGFhN2QiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiNzJiYTYxZTAtMWJiNS0xMWViLTkwNDAtMjE1NmIzMzBhYTdkIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjA0NTQxNDk4LCJleHAiOjE2MDQ1NTA0OTh9.ZVJ5GAWLRYQqaZ7PxED-n4WlQPVJpCE7mc73MLZdNA4udWaG2SAKNPvHZ12VpKi5ly81b2mCvIq2FWIEtyzRMA'
			}


def send_req(ids):
	for item in ids:

		# print(*requests.get('http://localhost:8080/api/plugins/telemetry/DEVICE/'+item+'/values/timeseries',
		# 						 headers = headers).json())

		get_req = requests.get('http://localhost:8080/api/plugins/telemetry/DEVICE/'+item+'/values/timeseries',
		 						 headers = headers).json()

		print(get_req)
		
		# for key in get_req:
		# 	print(key+': '+get_req[key][0]['value'])

SmAl_id=["e48d1be0-1f80-11eb-baed-6de80ac85462","c2fd0990-1f80-11eb-baed-6de80ac85462", "096d6aa0-1f81-11eb-baed-6de80ac85462", "26ecafa0-1f81-11eb-baed-6de80ac85462", "3eaa6a10-1f81-11eb-baed-6de80ac85462","58a1c0d0-1f81-11eb-baed-6de80ac85462", "741d94b0-1f81-11eb-baed-6de80ac85462", "8b4cf1d0-1f81-11eb-baed-6de80ac85462", "a1ddec10-1f81-11eb-baed-6de80ac85462", "bd8cdde0-1f81-11eb-baed-6de80ac85462"]
Dest_id=["1e4aa4f0-1f82-11eb-baed-6de80ac85462", "3d35d600-1f82-11eb-baed-6de80ac85462","60cf4ce0-1f82-11eb-baed-6de80ac85462", "7fe892d0-1f82-11eb-baed-6de80ac85462", "b8f69770-1f82-11eb-baed-6de80ac85462", "e7fc6720-1f82-11eb-baed-6de80ac85462", "03316e00-1f83-11eb-baed-6de80ac85462", "1b883420-1f83-11eb-baed-6de80ac85462", "32e07600-1f83-11eb-baed-6de80ac85462", "4973ba30-1f83-11eb-baed-6de80ac85462"]
Cap_id=["7c8c5300-1f83-11eb-baed-6de80ac85462", "b9848a20-1f83-11eb-baed-6de80ac85462", "e8b93200-1f83-11eb-baed-6de80ac85462", "1248d800-1f84-11eb-baed-6de80ac85462", "33001680-1f84-11eb-baed-6de80ac85462", "506061d0-1f84-11eb-baed-6de80ac85462", "5cede210-1f84-11eb-baed-6de80ac85462","845ec6c0-1f84-11eb-baed-6de80ac85462", "9e3723d0-1f84-11eb-baed-6de80ac85462", "c0e30660-1f84-11eb-baed-6de80ac85462"]


# while True:

# 	send_req(SmAl_id)
# 	send_req(Dest_id)

	# if (requests.get('http://localhost:8080/api/v1/LOJIq1vNysAcFhGYzzn1/attributes?clientKeys=clearTs',
	# 	 						 headers = headers).json()["client"]["clearTs"] != 0):
	# 	print("Alarm off")
	# else:
	# 	print("Alarm on")


# 	time.sleep(5)