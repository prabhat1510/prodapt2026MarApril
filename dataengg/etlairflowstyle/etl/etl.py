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
CITIES = [
    {"name": "London", "lat_long": "51.5074,-0.1278"},
    {"name": "Paris", "lat_long": "48.8566,2.3522"},
    {"name": "New York", "lat_long": "40.7128,-74.0060"}
]

# Weather API Calls
def get_weather_dataset():
    weather_df = pd.DataFrame()
    for city in CITIES:
        print(f"Fetching Results for City - {city['name']} :: ")
        querystring = {"q": city['lat_long']}
        
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            data = response.json()
            flat_response = pd.json_normalize(data)
            
            city_df = flat_response[[
                'location.name', 'location.region', 'location.country', 
                'location.lat', 'location.lon', 'location.tz_id', 
                'current.temp_c', 'current.temp_f', 'current.condition.text', 
                'current.condition.icon', 'current.wind_kph', 'current.pressure_in', 
                'current.precip_in', 'current.humidity', 'current.cloud', 
                'current.last_updated_epoch'
            ]]
            weather_df = pd.concat([weather_df, city_df], ignore_index=True)
        except Exception as e:
            logging.error(f"Error fetching weather for {city['name']}: {e}")

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
print(f"Loading {len(temp_df)} records...")

for idx, row in temp_df.iterrows(): 
    db.execute_query(config.weather_insert_query, list(row))

db.connection_close()
logging.info("Script Executed Successfully")