from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool
    DATABASE_URL: str
    LOG_LEVEL: str
    RAPID_API_HOST: str
    RAPID_API_KEY: str
    CITIES: str = "London,Paris" # Default cities
    
    # MySQL specific settings (for manual client)
    DB_HOST: str = "localhost"
    DB_NAME: str = "etl_db"
    DB_USER: str = "root"
    DB_PASS: str = "password"
    DB_PORT: int = 3306
    
    weather_create_query: str = """
CREATE TABLE IF NOT EXISTS weather (
            name VARCHAR(255) NOT NULL,
            region VARCHAR(255),
            country VARCHAR(255),
            lat DECIMAL(9, 6),
            lon DECIMAL(9, 6),
            timezone VARCHAR(255),
            temp_c DECIMAL(5, 2),
            temp_f DECIMAL(5, 2),
            condition_text VARCHAR(255),
            condition_icon VARCHAR(255),
            wind_kph DECIMAL(5, 2),
            pressure_in DECIMAL(5, 2),
            precipitation_in DECIMAL(5, 2),
            humidity DECIMAL(5, 2),
            cloud DECIMAL(5, 2),
            last_updated_epoch BIGINT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
    weather_insert_query: str = """
INSERT INTO weather (name, region, country, lat, lon, timezone, temp_c, temp_f, 
    condition_text, condition_icon, wind_kph, pressure_in, precipitation_in, humidity, 
    cloud, last_updated_epoch) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

    model_config = SettingsConfigDict(env_file=".env", extra="allow")

settings = Settings()