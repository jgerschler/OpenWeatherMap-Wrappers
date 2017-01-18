import json
from datetime import datetime

class CurrentWeather(object):
    def __init__(self):
        pass

    def json_decode(self, message):
        self.decoded_string = json.loads(message)
        self.data_collection_time = self.decoded_string.get('dt', 'unknown')
        self.cloud_cover = self.decoded_string.get('clouds', 'unknown').get('all', 'unknown')
        self.city_name = self.decoded_string.get('name', 'unknown')
        self.longitude = self.decoded_string.get('coord', 'unknown').get('lon', 'unknown')
        self.latitude = self.decoded_string.get('coord', 'unknown').get('lat', 'unknown')
        self.country = self.decoded_string.get('sys', 'unknown').get('country', 'unknown')
        self.sunset_time = self.decoded_string.get('sys', 'unknown').get('sunset', 'unknown')
        self.sunrise_time = self.decoded_string.get('sys', 'unknown').get('sunrise', 'unknown')
        self.weather_cond_id = self.decoded_string.get('weather', 'unknown').get('id', 'unknown')
        self.weather_group = self.decoded_string.get('weather', 'unknown').get('main', 'unknown')
        self.weather_description = self.decoded_string.get('weather', 'unknown').get('description', 'unknown')
        self.rain_3h = self.decoded_string.get('rain', 'unknown').get('3h', 'unknown')
        self.pressure = self.decoded_string.get('main', 'unknown').get('pressure', 'unknown')
        self.temp_min = self.decoded_string.get('main', 'unknown').get('temp_min', 'unknown')
        self.temp_max = self.decoded_string.get('main', 'unknown').get('temp_max', 'unknown')
        self.temp = self.decoded_string.get('main', 'unknown').get('temp', 'unknown')
        self.humidity = self.decoded_string.get('main', 'unknown').get('humidity', 'unknown')
        self.city_id = self.decoded_string.get('id', 'unknown')
        self.wind_speed = self.decoded_string.get('wind', 'unknown').get('deg', 'unknown')
        self.wind_direction = self.decoded_string.get('wind', 'unknown').get('deg', 'unknown')
        
    def get_data_collection_time(self):
        """returns data collection time as tuple (UTC UNIX time, UTC time)"""
        return (self.data_collection_time, datetime.fromtimestamp(int(self.data_collection_time)).strftime('%Y-%m-%d %H:%M:%S'))
        
    def get_cloud_cover(self):
        """returns cloud cover as tuple (value, unit)"""
        return (self.cloud_cover, "%")
        
    def get_location(self):
        """returns city and country as string"""
        return "{0}, {1}".format(self.city_name, self.country)
        
    def get_lat_lon(self):
        """returns latitude and longitude as tuple (latitude, longitude)"""
        return (self.latitude, self.longitude)
        
    def get_sunrise(self):
        """returns sunrise time as tuple (UTC UNIX time, UTC time)"""
        return (self.sunrise_time, datetime.fromtimestamp(int(self.sunrise_time)).strftime('%Y-%m-%d %H:%M:%S'))
        
    def get_sunset(self):
        """returns sunrise time as tuple (UTC UNIX time, UTC time)"""
        return (self.sunset_time, datetime.fromtimestamp(int(self.sunset_time)).strftime('%Y-%m-%d %H:%M:%S'))
        
    def get_weather(self):
        """returns a tuple: (weather group, weather description)"""
        return (self.weather_group, self.weather_description)
        
    def get_rain_3h(self):
        """returns the quantity of rain that has fallen in the last 3 hours as tuple (value, unit)"""
        return (self.rain_3h, "meter")
        
    