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
    
    # SQL Queries
    weather_create_query: str = """
    CREATE TABLE IF NOT EXISTS weather_data (
        city_name VARCHAR(255),
        region VARCHAR(255),
        country VARCHAR(255),
        lat DECIMAL(15, 10),
        lon DECIMAL(15, 10),
        tz_id VARCHAR(100),
        temp_c DECIMAL(10, 2),
        temp_f DECIMAL(10, 2),
        condition_text VARCHAR(255),
        condition_icon VARCHAR(255),
        wind_kph DECIMAL(10, 2),
        pressure_in DECIMAL(10, 2),
        precip_in DECIMAL(10, 2),
        humidity INT,
        cloud INT,
        last_updated_epoch BIGINT
    )
    """
    weather_insert_query: str = """
    INSERT INTO weather_data (
        city_name, region, country, lat, lon, tz_id, temp_c, temp_f, 
        condition_text, condition_icon, wind_kph, pressure_in, 
        precip_in, humidity, cloud, last_updated_epoch
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    model_config = SettingsConfigDict(env_file=".env", extra="allow")

settings = Settings()