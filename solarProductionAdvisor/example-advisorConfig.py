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
solar_data_file = './solar_data.json' # Path to save solar data to. Overwritten at 8pm every day.
analysis_data_file = './analysis_data.json' # Path to save analysis data to. Overwritten at each run.
ignore_time_constraint = False # Ignore time constraint for testing purposes

# Variables for SolarEdge monitoring
solar_edge_api_key = 'YOURAPIKEY' 
solar_edge_endpoint = 'https://monitoringapi.solaredge.com/site/YOURSIDEID/overview?'

# Variables for the Telegram bot
token = 'YOURTOKEN'
chat_id = 'YOURCHATID'