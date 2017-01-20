import json

data = """{"time":"2017-01-17T13:38:57Z",
"location":{"latitude":0.0773,"longitude":10.0566},
"data":{"no2":{"precision":1.766496829177856e+15,
"value":2.92424727396352e+15},
"no2_strat":{"precision":2.00000000753664e+14,
"value":1.869643153145856e+15},
"no2_trop":{"precision":1.842488759287808e+15,"value":1.0546040537088e+15}}}"""


def get_data(data):
    data_dict = json.loads(data)

    if data_dict['message']:
        return "Data unavailable"

    try:
        no2_trop = (data_dict.get('data').get('no2_trop').get('value',0), data_dict.get('data').get('no2_trop').get('precision',0))
    except:
        no2_trop = None
    try:
        no2_strat = (data_dict.get('data').get('no2_strat').get('value',0), data_dict.get('data').get('no2_strat').get('precision',0))
    except:
        no2_strat = None
    try:
        no2 = (data_dict.get('data').get('no2').get('value',0), data_dict.get('data').get('no2').get('precision',0))
    except:
        no2 = None
    no2_location = (data_dict.get('location').get('latitude'), data_dict.get('location').get('longitude'))
        

    no2_datetime = data_dict.get('time')
    print("got it all")
