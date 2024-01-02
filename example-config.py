#!/usr/bin/env python3

# .gitignore should include reference to config.py
# Example only. Rename this file to config.py and fill in the variables below

# Logfile path
logfile = './solar-smart-plug.log'

# Thresholds (if solar power is above this value, switch on the plug)
threshold_power = 230

# Variables for Solar monitoring
solar_edge_api_key = 'APIKEY' 
solar_edge_endpoint = 'https://monitoringapi.solaredge.com/site/YOURSITEID/overview?'

# Variables for D-Link W115 Smart Plug
smart_plug_ip = '192.168.0.20'
smart_plug_pin = 'YOURPIN'


