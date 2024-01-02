import requests
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

# Load all configuration from config.py
from advisorConfig import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        RotatingFileHandler(logfile, maxBytes=10*1024*1024, backupCount=5),
        logging.StreamHandler()
    ]
)

def fetch_solar_production(api_url):
    """
    Fetches solar production information from the API.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        solar_data = response.json()["result"]["watt_hours_day"]
        return solar_data
    except Exception as e:
        logging.error(f"Error fetching solar production: {e}")
        return {}

def find_highest_solar_window(solar_data):
    """
    Finds the time window with the highest cumulative solar output.
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_day_data = {time: value for time, value in solar_data.items() if time.startswith(current_date)}

    if current_day_data:
        max_window_start, max_window_end, max_window_output = max(
            (window_start, window_end, sum(values))
            for (window_start, values), (_, window_end) in zip(current_day_data.items(), current_day_data.items())
        )

        return max_window_start, max_window_end, max_window_output
    else:
        return None, None, None

def send_telegram_message(token, chat_id, message):
    """
    Sends a text message to a Telegram chat.
    """
    try:
        telegram_url = f'https://api.telegram.org/bot{token}'
        send_message_url = f'{telegram_url}/sendMessage'
        
        tg_params = {'chat_id': chat_id, 'text': message}
        response = requests.post(send_message_url, params=tg_params)
        response.raise_for_status()
        logging.info('Message sent')
    except Exception as e:
        logging.error(f"Error sending Telegram message: {e}")

def main():
    # Fetch solar production data
    solar_data = fetch_solar_production(solar_forecast_endpoint)

    # Find the time window with the highest cumulative solar output
    max_window_start, max_window_end, max_window_output = find_highest_solar_window(solar_data)

    if max_window_start is not None:
        # Format the times for better readability
        max_window_start_formatted = datetime.strptime(max_window_start, "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S")
        max_window_end_formatted = datetime.strptime(max_window_end, "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S")

        # Prepare the message
        message = f"The time window with the highest cumulative solar output today is from {max_window_start_formatted} to {max_window_end_formatted} with {max_window_output} watt-hours."

        # Send the message to Telegram
        send_telegram_message(token, chat_id, message)
    else:
        logging.info('No solar output data available for the current day.')

if __name__ == "__main__":
    main()
