import requests
import logging
from datetime import datetime, timedelta
import advisorConfig  # Import all variables from the config module
import json

# Set up logging
logging.basicConfig(filename=advisorConfig.logfile, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_solar_production(test_json_path=None):
    """
    Fetch solar production estimates from the Forecast Solar API or use data from a test JSON file.
    """
    if advisorConfig.use_test_data:
        test_json_path = advisorConfig.test_json_path
        try:
            with open(test_json_path, 'r') as file:
                solar_data = json.load(file)
            return solar_data
        except Exception as e:
            logging.error(f"Error reading test JSON file: {e}")
            return None

    try:
        response = requests.get(advisorConfig.solar_forecast_endpoint)
        response.raise_for_status()
        solar_data = response.json()["result"]
        return solar_data
    except Exception as e:
        logging.error(f"Error fetching solar production: {e}")
        return None

def analyze_solar_data(solar_data):

    current_date = datetime.now().strftime('%Y-%m-%d')
    today_data = {key: value for key, value in solar_data['result'].items() if key.startswith(current_date)}

    if not today_data:
        # If there is no data for today, return None for all values
        return None, None, None, None

    peak_hour = max(today_data, key=today_data.get)
    peak_power = today_data[peak_hour]

    window_start = peak_hour
    window_end = peak_hour

    # Specify the number of hours before the peak to include in the window
    build_up_hours = 2

    # Find the start of the window, ensuring a build-up to peak power
    for i in range(build_up_hours + 1):
        current_hour = (datetime.strptime(peak_hour, '%Y-%m-%d %H:%M:%S') - timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S')
        if current_hour in today_data and today_data[current_hour] >= 0.8 * peak_power:
            window_start = current_hour
        else:
            break

    # Find the end of the window, ensuring a decrease in power after peak
    for i in range(1, len(today_data)):
        current_hour = (datetime.strptime(peak_hour, '%Y-%m-%d %H:%M:%S') + timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S')
        if current_hour in today_data and today_data[current_hour] >= 0.8 * peak_power:
            window_end = current_hour
        else:
            if today_data[current_hour] < 0.8 * peak_power:
                break

    return peak_hour, peak_power, window_start, window_end

def send_telegram_message(peak_hour, peak_power, optimal_period_start, optimal_period_end):
    """
    Send a summary message to a Telegram channel with the identified optimal solar output period.
    """
    if optimal_period_start and optimal_period_end:
        message = f"Optimal solar output period for today:\nPeak Hour: {peak_hour}\nPeak Power Output: {peak_power}\nStart Time: {optimal_period_start}\nEnd Time: {optimal_period_end}"
        logging.info("Sending message to Telegram channel.")
        send_message_to_telegram(message)
    else:
        logging.warning("No message sent to Telegram channel.")

def send_message_to_telegram(message):
    """
    Send a message to the configured Telegram channel.
    """
    try:
        telegram_url = f'https://api.telegram.org/bot{advisorConfig.token}/sendMessage'
        tg_params = {'chat_id': advisorConfig.chat_id, 'text': message}
        response = requests.post(telegram_url, params=tg_params)
        response.raise_for_status()
        logging.info('Message sent to Telegram channel.')
    except Exception as e:
        logging.error(f"Error sending message to Telegram channel: {e}")

def main():

    solar_data = fetch_solar_production()

    if solar_data is not None:
        peak_hour, peak_power, optimal_period_start, optimal_period_end = analyze_solar_data(solar_data)
        
        if peak_hour is not None:
            send_telegram_message(peak_hour, peak_power, optimal_period_start, optimal_period_end)
        else:
            logging.warning("No peak hour found.")
    else:
        logging.warning("No solar data available.")

if __name__ == "__main__":
    main()
