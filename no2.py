import json

data = """{"time":"2017-01-17T13:38:57Z",
"location":{"latitude":0.0773,"longitude":10.0566},
"data":{"no2":{"precision":1.766496829177856e+15,
"value":2.92424727396352e+15},
"no2_strat":{"precision":2.00000000753664e+14,
"value":1.869643153145856e+15},
"no2_trop":{"precision":1.842488759287808e+15,"value":1.0546040537088e+15}}}"""

data_dict = json.loads(data)

