import json

data = """{"time":"2017-01-12T13:20:28Z","location":{"latitude":0.0435,"longitude":9.8746},"data":266.7435302734375}"""



data_dict = json.loads(data)
if data_dict.get('message') == 'not found':
    print("Data unavailable")
try:
    o3 = data_dict.get('data')
    o3_location = (data_dict.get('location').get('latitude'), data_dict.get('location').get('longitude'))
    o3_datetime = data_dict.get('time')
except:
    o3, o3_location, o3_datetime = None, None, None
