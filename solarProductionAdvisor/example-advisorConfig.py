#!/usr/bin/env python3

# .gitignore should include reference to config.py
# Example only. Rename this file to advisorConfig.py and fill in the variables below

# Logfile path
logfile = './solar-production-advisor-log.log'

# Variables for Solar production forecasting. Currently using: https://doc.forecast.solar/api:estimate 
solar_forecast_api_key = '' 
solar_forecast_endpoint = 'https://api.forecast.solar/estimate/watts/LAT/LONG/AZIMUTH/TILT/CAPACITY' # (lat, long, azimuth, tilt, capacity)
use_test_data = False # Use test data from test.json instead of API
test_json_path = './test.json'

# Variables for the Telegram bot
token = 'YOURTOKEN'
chat_id = 'YOURCHATID'