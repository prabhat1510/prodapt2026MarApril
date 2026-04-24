import os
import sys
import pandas as pd
import requests
import logging

# Adding product root to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)
os.chdir(project_root)

from config.config import settings as config
from db.mysql_db import MySQLClient

logging.basicConfig(level=logging.INFO)
url = "https://weatherapi-com.p.rapidapi.com/current.json"
headers = {
	"X-RapidAPI-Key": config.RAPID_API_KEY,
	"X-RapidAPI-Host": config.RAPID_API_HOST
}

# Example cities format if not provided in config
cities = [
    {"name": "London", "lat_long": "51.5074,-0.1278"},
    {"name": "Paris", "lat_long": "48.8566,2.3522"},
    {"name": "New York", "lat_long": "40.7128,-74.0060"},
    {"name": "Tokyo", "lat_long": "35.6895,139.6917"},
    {"name": "Sydney", "lat_long": "-33.8688,151.2093"},
    {"name": "Rio de Janeiro", "lat_long": "-22.9068,-43.1729"},
    {"name": "Cairo", "lat_long": "30.0444,31.2357"},
    {"name": "Moscow", "lat_long": "55.7558,37.6173"},
    {"name": "Beijing", "lat_long": "39.9042,116.4074"},
    {"name": "Mumbai", "lat_long": "19.0760,72.8777"},
    {"name": "Berlin", "lat_long": "52.5200,13.4050"},
    {"name": "Rome", "lat_long": "41.9028,12.4964"},
    {"name": "Madrid", "lat_long": "40.4168,-3.7038"},
    {"name": "Toronto", "lat_long": "43.6532,-79.3832"},
    {"name": "Mexico City", "lat_long": "19.4326,-99.1332"},
    {"name": "Buenos Aires", "lat_long": "-34.6037,-58.3816"},
    {"name": "Seoul", "lat_long": "37.5665,126.9780"},
    {"name": "Bangkok", "lat_long": "13.7563,100.5018"},
    {"name": "Istanbul", "lat_long": "41.0082,28.9784"},
    {"name": "Amsterdam", "lat_long": "52.3676,4.9041"},
    {"name": "Vienna", "lat_long": "48.2082,16.3738"},
    {"name": "Prague", "lat_long": "50.0755,14.4378"},
    {"name": "Budapest", "lat_long": "47.4979,19.0402"},
    {"name": "Warsaw", "lat_long": "52.2297,21.0122"},
    {"name": "Dublin", "lat_long": "53.3498,-6.2603"},
    {"name": "Oslo", "lat_long": "59.9139,10.7522"},
    {"name": "Helsinki", "lat_long": "60.1699,24.9384"},
    {"name": "Lisbon", "lat_long": "38.7223,-9.1393"},
    {"name": "Athens", "lat_long": "37.9838,23.7275"},
    {"name": "Brussels", "lat_long": "50.8503,4.3517"},
    {"name": "Zurich", "lat_long": "47.3769,8.5417"},
    {"name": "Geneva", "lat_long": "46.2044,6.1444"},
    {"name": "Munich", "lat_long": "48.1351,11.5820"},
    {"name": "Hamburg", "lat_long": "53.5511,9.9937"},
    {"name": "Frankfurt", "lat_long": "50.1109,8.6821"},
    {"name": "Copenhagen", "lat_long": "55.6761,12.5683"},
    {"name": "Stockholm", "lat_long": "59.3293,18.0686"},
    {"name": "Kuala Lumpur", "lat_long": "3.1390,101.6869"},
    {"name": "Singapore", "lat_long": "1.3521,103.8198"},
    {"name": "Hong Kong", "lat_long": "22.3193,114.1694"},
    {"name": "Taipei", "lat_long": "25.0330,121.5654"},
    {"name": "Manila", "lat_long": "14.5995,120.9842"},
    {"name": "Jakarta", "lat_long": "-6.2088,106.8456"},
    {"name": "Ho Chi Minh City", "lat_long": "10.8231,106.6297"},
    {"name": "Hanoi", "lat_long": "21.0285,105.8542"},
    {"name": "Santiago", "lat_long": "-33.4489,-70.6693"},
    {"name": "Lima", "lat_long": "-12.0464,-77.0428"},
    {"name": "Bogota", "lat_long": "4.7110,-74.0721"},
    {"name": "Caracas", "lat_long": "10.4806,-66.9036"},
    {"name": "Montreal", "lat_long": "45.5017,-73.5673"},
    {"name": "Vancouver", "lat_long": "49.2827,-123.1207"},
    {"name": "Calgary", "lat_long": "51.0447,-114.0719"},
    {"name": "Edmonton", "lat_long": "53.5461,-113.4937"},
    {"name": "Ottawa", "lat_long": "45.4215,-75.6972"},
    {"name": "Quebec City", "lat_long": "46.8139,-71.2080"},
    {"name": "Winnipeg", "lat_long": "49.9001,-97.1384"},
    {"name": "Halifax", "lat_long": "44.6488,-63.5752"},
    {"name": "St. John's", "lat_long": "47.5615,-52.7128"},
    {"name": "Regina", "lat_long": "50.4452,-104.6187"},
    {"name": "Saskatoon", "lat_long": "52.1332,-106.6985"},
    {"name": "Thunder Bay", "lat_long": "48.3833,-89.2500"},
    {"name": "Sudbury", "lat_long": "46.4907,-80.9960"},
    {"name": "Kingston", "lat_long": "44.2312,-76.4859"}]
def get_weather_dataset():
    weather_df = pd.DataFrame()
    for city in cities:
        print(f"Fetching Results for City - {city['name']} :: ")
        querystring = {"q": city['lat_long']}
        
        response = requests.get(url, headers=headers, params=querystring)
        flat_response = pd.json_normalize(response.json())
        print(response.json())

        city_df = flat_response[['location.name', 'location.region', 'location.country', 'location.lat', 'location.lon', 'location.tz_id', 'current.temp_c', 'current.temp_f', 'current.condition.text', 'current.condition.icon', 'current.wind_kph', 'current.pressure_in', 'current.precip_in', 'current.humidity', 'current.cloud', 'current.last_updated_epoch']]
        weather_df = pd.concat([weather_df, city_df], ignore_index=True)

    print(len(weather_df))
    weather_df.to_csv('Weather_DF.csv', index=False)
    logging.info("Weather DF generated!")

# Run data collection
get_weather_dataset()

# Load Dataset in MySQL DB
logging.info("Running the ETL script - Loading to MySQL")
db = MySQLClient(
    host=config.DB_HOST,
    database=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASS,
    port=config.DB_PORT
)

print("Creating Table if not exists...")
db.execute_query(config.weather_create_query)

temp_df = pd.read_csv('Weather_DF.csv')
temp_df =temp_df.where(pd.notnull(temp_df), None)
print(f"Loading {len(temp_df)} records...")

for idx, row in temp_df.iterrows(): 
    db.execute_query(config.weather_insert_query, list(row))

db.connection_close()
logging.info("Script Executed Successfully")