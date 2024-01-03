# Solar Advisor - Daily Solar Production Estimates based on weather and panel orientation

The Solar Advisor is a Python integration script designed to fetch solar production estimates and send relevant information to a Telegram group chat. It leverages the [Forecast Solar API](https://doc.forecast.solar/api:estimate) to estimate solar power production based on geographical coordinates, azimuth, tilt, and capacity.

In the absence of detailed realtime monitoring, this approach could also be used to automate the operation of electrical devices (e.g., pool pumps, electric vehicle charging) to maximise the use of solar power.

## Features

- Fetches solar production estimates from the Forecast Solar API.
- Identifies the optimal time window with the highest cumulative solar output for the current day and sends a daily message to a Telegram group chat.
- Checks if the current actual power output is greater than or equal to the expected peak power output and sends a message if it is.

## Prerequisites

Before using the script, ensure you have the following:

- Python 3.x installed
- Required Python packages (install with `pip install -r requirements.txt`)
- SolarEdge API access. Create using this guide https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf
- Telegram App installed registered on your mobile device https://telegram.org/apps
- Telegram group chat and bot. Create using this guide https://core.telegram.org/bots#6-botfather

## Configuration

Create an `advisorConfig.py` file to include your API keys, Telegram bot details, and other necessary configuration parameters. See example-advisorConfig.py for an example.

## Usage

Schedule the script using CRON at 15min intervals between useful hours (7am - 7pm) to ensure the optimal time window is identified as early as possible. For example:

``` cron
*/15 7-19 * * * /path/to/python3 /path/to/solarAdvisor.py
```

Replace /path/to/python3 with the actual path to your Python interpreter (e.g., /usr/bin/python3), and replace /path/to/solarAdvisor.py with the full path to your Python script.

Could also be used in an Azure Function or similar for serverless operation.
