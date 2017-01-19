import json, time
from datetime import datetime
from urllib2 import Request, urlopen, URLError# update to use requests module?

class CurrentWeather(object):
    """A class for getting the current US weather using the OpenWeatherMap API."""
    def __init__(self, zipcode, api_key):
        self.zipcode = zipcode
        self.api_key = api_key
    
    def connect(self):# may need to add more try/except statments; API results seem to deviate from documentation
        """Connect to OpenWeatherMap server and pull weather data."""
        request = Request('http://api.openweathermap.org/data/2.5/weather?zip='+self.zipcode+',us&APPID='+self.api_key)
        try:
            data = urlopen(request).read()
        except URLError:
            print("Could not connect to API server. Is your key correct?")
        self.decoded_string = json.loads(data)
        self.data_collection_time = self.decoded_string.get('dt', 'unknown')
        self.cloud_cover = self.decoded_string.get('clouds', 'unknown').get('all', 'unknown')
        self.city_name = self.decoded_string.get('name', 'unknown')
        self.longitude = self.decoded_string.get('coord', 'unknown').get('lon', 'unknown')
        self.latitude = self.decoded_string.get('coord', 'unknown').get('lat', 'unknown')
        self.country = self.decoded_string.get('sys', 'unknown').get('country', 'unknown')
        self.sunset_time = self.decoded_string.get('sys', 'unknown').get('sunset', 'unknown')
        self.sunrise_time = self.decoded_string.get('sys', 'unknown').get('sunrise', 'unknown')
        self.weather_cond_id = self.decoded_string.get('weather', 'unknown')[0].get('id', 'unknown')# multiple weather conditions can be included here. 
        self.weather_group = self.decoded_string.get('weather', 'unknown')[0].get('main', 'unknown')# currently, we'll just get the primary.
        self.weather_description = self.decoded_string.get('weather', 'unknown')[0].get('description', 'unknown')
        try:
            self.rain_3h = self.decoded_string.get('rain', 'unknown').get('3h', 'unknown')
        except:
            self.rain_3h = 0
        self.pressure = self.decoded_string.get('main', 'unknown').get('pressure', 'unknown')
        self.temp_min = self.decoded_string.get('main', 'unknown').get('temp_min', 'unknown')
        self.temp_max = self.decoded_string.get('main', 'unknown').get('temp_max', 'unknown')
        self.temp = self.decoded_string.get('main', 'unknown').get('temp', 'unknown')
        self.humidity = self.decoded_string.get('main', 'unknown').get('humidity', 'unknown')
        self.city_id = self.decoded_string.get('id', 'unknown')
        self.wind_speed = self.decoded_string.get('wind', 'unknown').get('speed', 'unknown')
        self.wind_gust = self.decoded_string.get('wind', 'unknown').get('gust', 'unknown')
        self.wind_direction = self.decoded_string.get('wind', 'unknown').get('deg', 'unknown')
        
    def record_data(self, interval, filename, max_data_points):
        """periodically connect to API and write results to CSV file."""
        file = open(filename, 'w')
        file.write("zipcode,data_collection_time,cloud_cover,weather_group,weather_description,pressure,temp,humidity,wind_speed,wind_direction\n")
        for i in range(max_data_points):
            self.connect()
            file.write(str(self.zipcode)+","+str(self.data_collection_time)+","+str(self.cloud_cover)+","+str(self.weather_group)+","+str(self.weather_description)+","+str(self.pressure)+","+
            str(self.temp)+","+str(self.humidity)+","+str(self.wind_speed)+","+str(self.wind_direction)+"\n")
            print("Data point {0} recorded").format(str(i+1))
            if i < (max_data_points-1):
                time.sleep(interval*60)
        file.close()
        
        
    def parse(self, data):# for directly parsing data string
        """Parse data directly from a string."""
        self.decoded_string = json.loads(data)
        self.data_collection_time = self.decoded_string.get('dt', 'unknown')
        self.cloud_cover = self.decoded_string.get('clouds', 'unknown').get('all', 'unknown')
        self.city_name = self.decoded_string.get('name', 'unknown')
        self.longitude = self.decoded_string.get('coord', 'unknown').get('lon', 'unknown')
        self.latitude = self.decoded_string.get('coord', 'unknown').get('lat', 'unknown')
        self.country = self.decoded_string.get('sys', 'unknown').get('country', 'unknown')
        self.sunset_time = self.decoded_string.get('sys', 'unknown').get('sunset', 'unknown')
        self.sunrise_time = self.decoded_string.get('sys', 'unknown').get('sunrise', 'unknown')
        self.weather_cond_id = self.decoded_string.get('weather', 'unknown')[0].get('id', 'unknown')
        self.weather_group = self.decoded_string.get('weather', 'unknown')[0].get('main', 'unknown')
        self.weather_description = self.decoded_string.get('weather', 'unknown')[0].get('description', 'unknown')
        try:
            self.rain_3h = self.decoded_string.get('rain', 'unknown').get('3h', 'unknown')
        except:
            self.rain_3h = None
        self.pressure = self.decoded_string.get('main', 'unknown').get('pressure', 'unknown')
        self.temp_min = self.decoded_string.get('main', 'unknown').get('temp_min', 'unknown')
        self.temp_max = self.decoded_string.get('main', 'unknown').get('temp_max', 'unknown')
        self.temp = self.decoded_string.get('main', 'unknown').get('temp', 'unknown')
        self.humidity = self.decoded_string.get('main', 'unknown').get('humidity', 'unknown')
        self.city_id = self.decoded_string.get('id', 'unknown')
        self.wind_speed = self.decoded_string.get('wind', 'unknown').get('deg', 'unknown')
        self.wind_gust = self.decoded_string.get('wind', 'unknown').get('gust', 'unknown')
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
        return (self.rain_3h, "cm")
        
    def get_pressure(self):
        """returns the current barometric pressure as tuple (value, unit)"""
        return (self.pressure, "mmHg")
    
    def get_temp(self):
        """returns the current temperature as tuple (value, unit)"""
        return (self.temp, "K")
    
    def get_humidity(self):
        """returns the current humidity as tuple (value, unit)"""
        return (self.humidity, "%")
    
    def get_wind_speed(self):
        """returns the current wind speed as tuple (value, unit)"""
        return (self.wind_speed, "meters/second")
    
    def get_wind_direction(self):
        """returns the current wind direction as tuple (direction in degrees, cardinal direction)"""
        def cardinal_direction(degrees):# OWM API should technically supply cardinal values, but in case it doesn't, we'll calculate them here.
            if (degrees <= 360.0 and degrees > 337.5) or (degrees <= 22.5 and degrees > 0.0):
                return 'N'
            elif degrees <= 67.5 and degrees > 22.5:
                return 'NE'
            elif degrees <= 112.5 and degrees > 67.5:
                return 'E'
            elif degrees <= 157.5 and degrees > 112.5:
                return 'SE'
            elif degrees <= 202.5 and degrees > 157.5:
                return 'S'
            elif degrees <= 247.5 and degrees > 202.5:
                return 'SW'                
            elif degrees <= 292.5 and degrees > 247.5:
                return 'W'
            elif degrees <= 337.5 and degrees > 292.5:
                return 'NW'
            else:
                'Unknown'
                
        return (self.wind_direction, cardinal_direction(int(self.wind_direction)))
        
    def get_co(self):# these functions below are still not finished!
        pass
        request = Request('http://api.openweathermap.org/pollution/v1/co/0.0,10.0/current.json?appid={0}').format(self.api_key)
        try:
            data = urlopen(request).read()
        except URLError:
            print("Could not connect to API server. Is your key correct?")
        self.decoded_string = json.loads(data)
        
    def get_o3(self):
        pass
        request = Request('http://api.openweathermap.org/pollution/v1/o3/0.0,10.0/current.json?appid={0}').format(self.api_key)
        try:
            data = urlopen(request).read()
        except URLError:
            print("Could not connect to API server. Is your key correct?")
        self.decoded_string = json.loads(data)
        
    def get_so2(self):
        pass
        request = Request('http://api.openweathermap.org/pollution/v1/so2/0.0,10.0/current.json?appid={0}').format(self.api_key)
        try:
            data = urlopen(request).read()
        except URLError:
            print("Could not connect to API server. Is your key correct?")
        self.decoded_string = json.loads(data)
        
    def get_no2(self):
        pass
        request = Request('http://api.openweathermap.org/pollution/v1/no2/0.0,10.0/current.json?appid={0}').format(self.api_key)
        try:
            data = urlopen(request).read()
        except URLError:
            print("Could not connect to API server. Is your key correct?")
        self.decoded_string = json.loads(data)

if __name__ == '__main__':
    print("Suggested uses: Import as a module, or run in an IDE.")
