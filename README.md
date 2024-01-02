# Solar Power (SolarEdge) and Smart Plug (D-Link W115) Automation (Work In Progress)

## Overview

This Python script integrates solar power monitoring and smart plug control to optimize energy usage. The script fetches real-time solar power data from the SolarEdge API and utilizes the information to intelligently manage a smart plug. The goal is to automate the plug's state based on solar power levels, enhancing energy efficiency and sustainability.

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
- Currently only configured to support SolarEdge Solar Systems via their API
- D-LINK DSP W115 Smart Plug (other models may work with minor modifications)

## Usage

1. **Obtain API Key:**
   - Sign up for a SolarEdge API key and configure it in `config.py`.

2. **Configure Smart Plug:**
   - Adjust smart plug parameters in the script, including IP, PIN, and model.

3. **Run the Script:**
   - Schedule the execution of `solar_power_query.py` to fetch solar power data and control the smart plug.

## Notes

- Ensure proper security practices, especially when dealing with API keys and device configurations.
- Review and adjust thresholds and settings based on your specific requirements.


## Acknowledgments

This project is built upon a modified version of the [dspW245](https://github.com/jonassjoh/dspW245) project by Jonas Johansson. The original project provides a Python interface for interacting with DSP-W245 smart plugs.

- Original Author: Jonas Johansson
- Original Repository: [dspW245](https://github.com/jonassjoh/dspW245)
- License: [MIT License](https://opensource.org/licenses/MIT)

We express our gratitude to Jonas Johansson for the foundation provided by the dspW245 project.
