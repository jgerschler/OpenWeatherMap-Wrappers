import json

data = """{"time":"2017-01-10T01:04:11Z","location":{"latitude":0,"longitude":9.9822},"data":[{"precision":-4.999999987376214e-07,"pressure":1000,"value":9.546999990561744e-08},{"precision":-4.999999987376214e-07,"pressure":681.2920532226562,"value":1.0990000021138258e-07},{"precision":-4.999999987376214e-07,"pressure":464.15887451171875,"value":1.0600000166505197e-07},{"precision":4.526847519059629e-08,"pressure":316.2277526855469,"value":1.3231635875854408e-07},{"precision":2.0217363783103792e-08,"pressure":215.44346618652344,"value":1.1148824086149034e-07},{"precision":1.3288406819356169e-08,"pressure":146.77992248535156,"value":8.456179045879253e-08},{"precision":1.1692041113064988e-08,"pressure":100,"value":5.3665136334757335e-08},{"precision":1.0279908480015365e-08,"pressure":68.12920379638672,"value":1.694614937264305e-08},{"precision":8.678213703205984e-09,"pressure":46.415889739990234,"value":9.432620018401394e-09},{"precision":8.971908549426644e-09,"pressure":31.62277603149414,"value":1.2265934046240545e-08},{"precision":9.82157910556225e-09,"pressure":21.544347763061523,"value":7.694524462031893e-10},{"precision":1.2444655972387864e-08,"pressure":14.677992820739746,"value":6.4492882145827934e-09},{"precision":1.5417136012274568e-08,"pressure":10,"value":6.544960573506842e-09},{"precision":2.1918694415035134e-08,"pressure":6.812920570373535,"value":3.946762205941923e-08},{"precision":2.9209511254180143e-08,"pressure":4.6415886878967285,"value":1.4523875435656919e-08},{"precision":3.885616450816087e-08,"pressure":3.1622776985168457,"value":2.7898131804704462e-08},{"precision":5.472273301165842e-08,"pressure":2.1544346809387207,"value":2.2240324859534866e-10},{"precision":7.281767722133736e-08,"pressure":1.4677993059158325,"value":-1.942797922538375e-08},{"precision":9.689556179637293e-08,"pressure":1,"value":1.4705474882248382e-07},{"precision":1.4549777915817685e-07,"pressure":0.6812920570373535,"value":6.282193254492086e-08},{"precision":2.0660723976106965e-07,"pressure":0.46415889263153076,"value":6.399192287176447e-09},{"precision":2.8975875920878025e-07,"pressure":0.3162277638912201,"value":3.803027581739116e-08},{"precision":4.3011291950278974e-07,"pressure":0.2154434621334076,"value":-9.357850672131462e-08},{"precision":6.292416401265655e-07,"pressure":0.14677992463111877,"value":1.1690600558722508e-06},{"precision":7.059745144033513e-07,"pressure":0.10000000149011612,"value":-4.77894445793936e-07},{"precision":9.995542313845363e-07,"pressure":0.04641588777303696,"value":1.829119128160528e-06},{"precision":1.7970882026929758e-06,"pressure":0.02154434658586979,"value":1.0129482461707084e-06},{"precision":3.603179720812477e-06,"pressure":0.009999999776482582,"value":3.0716748824488604e-06},{"precision":6.4055152506625745e-06,"pressure":0.004641588777303696,"value":9.00080158316996e-06},{"precision":-1.0146035492653027e-05,"pressure":0.002154434798285365,"value":8.90406226972118e-06},{"precision":-1.5763809642521665e-05,"pressure":0.0010000000474974513,"value":1.7518750610179268e-05},{"precision":-1.9999999494757503e-05,"pressure":0.00046415888937190175,"value":1.1770000128308311e-05},{"precision":-1.9999999494757503e-05,"pressure":0.00021544346236623824,"value":1.1770000128308311e-05},{"precision":-1.9999999494757503e-05,"pressure":9.999999747378752e-05,"value":1.1770000128308311e-05},{"precision":-1.9999999494757503e-05,"pressure":4.641588748199865e-05,"value":1.1770000128308311e-05},{"precision":-1.9999999494757503e-05,"pressure":2.1544346964219585e-05,"value":1.1770000128308311e-05},{"precision":-1.9999999494757503e-05,"pressure":9.999999747378752e-06,"value":1.1770000128308311e-05}]}"""



data_dict = json.loads(data)
if data_dict.get('message') == 'not found':
    print("Data unavailable")
try:
    co = []
    for entry in data_dict['data']:
        co.append((entry['pressure'], entry['value'], entry['precision']))
except:
    co = None
co_location = (data_dict.get('location').get('latitude'), data_dict.get('location').get('longitude'))
co_datetime = data_dict.get('time')

