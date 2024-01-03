# Solar Advisor - Daily Solar Production Estimates based on weather and panel orientation

The Solar Advisor is a Python integration script designed to fetch solar production estimates and send relevant information to a Telegram group chat. It leverages the [Forecast Solar API](https://doc.forecast.solar/api:estimate) to estimate solar power production based on geographical coordinates, azimuth, tilt, and capacity.

In the absense of detailed realtime monitoring, this approach could be used to automate the operation of electrical devices (e.g., pool pumps, electric vehicle charging) to maximise the use of solar power.

## Features

- Fetches solar production estimates from the Forecast Solar API.
- Identifies the optimal time window with the highest cumulative solar output for the current day.
- Sends a summary message to a Telegram group chat with the identified optimal solar output period.

## Prerequisites

Before using the script, ensure you have the following:

- Python 3.x installed
- Required Python packages (install with `pip install -r requirements.txt`)
- Telegram App installed registered on your mobile device https://telegram.org/apps
- Telegram group chat and bot. Create using this guide https://core.telegram.org/bots#6-botfather

## Configuration

Create an `advisorConfig.py` file to include your API keys, Telegram bot details, and other necessary configuration parameters. See example-advisorConfig.py for an example.

## Usage

Schedule the script using CRON to send a message each day so residents know the best time to operate/charge electrical devices manually.

``` cron
0 8 * * * /path/to/python3 /path/to/solarAdvisor.py
```

Replace /path/to/python3 with the actual path to your Python interpreter (e.g., /usr/bin/python3), and replace /path/to/solarAdvisor.py with the full path to your Python script.

Could also be used in an Azure Function or similar for serverless operation.
