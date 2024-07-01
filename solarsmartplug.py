import requests
import logging
from config import *
from dspW245 import SmartPlug
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=logfile)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger('').addHandler(console_handler)

logger = logging.getLogger(__name__)

def turn_off_plug():
    sp = SmartPlug(smart_plug_ip, smart_plug_pin, model="W115")
    sp.set_socket(1, on=False)
    sp.keep_alive()
    sp.close()
    logger.info("Switched OFF the plug.")

def turn_on_plug():
    sp = SmartPlug(smart_plug_ip, smart_plug_pin, model="W115")
    sp.set_socket(1, on=True)
    sp.keep_alive()
    sp.close()
    logger.info("Switched ON the plug.")

# Get power output (limited to 300 requests per day)

def get_solar_power(api_url, api_key):
    try:
        params = {'api_key': api_key}
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad requests
        solar_data = response.json()

        # Extract current power information
        current_power = solar_data['overview']['currentPower']['power']

        return current_power

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from the API: {e}")
        return None

# Define the cutoff time (e.g., 18:00 or 6:00 PM)
cutoff_time = datetime.time(18, 0)

# Get the current time
now = datetime.datetime.now().time()

# Check if current time is past the cutoff time
if now >= cutoff_time:
    turn_off_plug()
else:
    # Call the function to get current solar power
    current_power = get_solar_power(solar_edge_endpoint, solar_edge_api_key)

    # Use the Solar power data to decide whether to switch on/off the plug
    if current_power is not None:
        logger.info(f"Current Solar Power: {current_power} watts")
        if current_power > threshold_power:
            # Switch on the plug
            turn_on_plug()
        else:
            # Switch off the plug
            turn_off_plug()
    else:
        logger.warning("Failed to retrieve solar power data.")