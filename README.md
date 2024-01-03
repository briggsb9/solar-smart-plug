# Solar Power (SolarEdge) and Smart Plug (D-Link W115) Automation (Work In Progress)

## Overview

This Python script integrates solar power monitoring and smart plug control with a view to optimize energy usage. It fetches real-time solar power data from the SolarEdge API and utilizes the information to manage the D-LINK W115 smart plug. The goal is to automate the plug's state based on solar power levels, enhancing energy efficiency and sustainability.


> **Note:**
> For more a more manual approach, I've also created a Solar Production Forecast Advisor to notify residents of the best time of day to use/charge electrical devices, see [solarProductionAdvisor/README.md](solarProductionAdvisor/README.md)

## Features

- **Solar Power Monitoring:**
  - Fetches current solar power data from the SolarEdge API.
  - Logs data and status to a specified log file for future analysis.

- **Smart Plug Automation:**
  - Controls a smart plug based on the retrieved solar power information.
  - Adjusts the plug's state (on/off) according to predefined thresholds.

## Configuration

- Configure solar monitoring parameters in the `config.py` file, including API key and endpoint.
- Customize smart plug settings, such as IP address, PIN code, and model, within the script.

## Requirements

- Python 3.x
- Requests library for HTTP requests (`pip install requests`)
- SolarEdge Solar System and access to [monitoring API](https://developers.solaredge.com/docs/monitoring/e9nwvc91l1jf5-getting-started-with-monitoring-api)
- D-LINK DSP W115 Smart Plug (other models may work with minor modifications)
- Local connectivity to the smart plug (e.g., same WiFi network)

## Usage

1. **Obtain API Key:**
   - See [here](https://www.suntribetrading.com/how-to/get-solaredge-api-siteid-and-key) for info on how to get a SolarEdge API key. Configure it in `config.py` to give the script access to your current solar output.

2. **Configure Smart Plug:**
   - See the guide [here](https://github.com/jonassjoh/dspW245) for instructions on how to configure the smart plug. Use PIN only method.
   - Adjust smart plug parameters in 'config.py' , including IP, PIN, and model.

3. **Schedule the Script:**
   - Schedule the execution of `solar_power_query.py` to fetch solar power data and control the smart plug. The server hosting the script must have local connectivity to the D-LINK smart plug.

   For example, use cron to run the script every 5 minutes:
   ```
    */30 8-19 * * * /usr/bin/python3 /home/pi/solar-smart-plug/solarsmartplug.py
   ```

## Notes

- This integration is intended to be run on the same network as the D-Link smart plug. Certain SSL checks in the dspW245 module have been bypassed to allow direct access to the D-LINK smart plug via a local connection, preventing the need for a home automation cloud service. Attempting to connect over the internet is not recommended for security reasons. See lines 199-206 in dspW245.py for code changes.
- Review and adjust the power threshold in config.py to control when the smart plug is turned on/off.


## Acknowledgments

This project is built upon a modified version of the [dspW245](https://github.com/jonassjoh/dspW245) project by Jonas Johansson. The original project provides a Python interface for interacting with DSP-W245 smart plugs. Many thanks to Jonas Johansson for most of the hard work.
