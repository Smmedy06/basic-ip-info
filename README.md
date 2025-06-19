# IP Information Tool

This is a simple desktop application built with Python and Tkinter that allows users to retrieve information about any public IP address. The tool uses the [ip-api.com](http://ip-api.com/) API to fetch geolocation and ISP details for the given IP address.

## Features
- **Detect My IP:** Automatically detects your public IP address.
- **Get Info:** Fetches details such as city, region, country, timezone, ISP, latitude, and longitude for any public IP address.
- **Private IP Detection:** Identifies and informs if the entered IP address is private (details are not fetched for private IPs).
- **User-Friendly GUI:** Simple and clean interface built with Tkinter.

## How to Use
1. **Install Requirements:**
   - Make sure you have Python 3 installed.
   - Install the required Python packages:
     ```bash
     pip install requests
     ```
2. **Run the Application:**
   - Execute the following command in your terminal:
     ```bash
     python main.py
     ```
3. **Using the Tool:**
   - Enter an IP address manually or click "Detect My IP" to auto-fill your public IP.
   - Click "Get Info" to fetch and display information about the IP address.

## Requirements
- Python 3.x
- requests
- tkinter (usually included with standard Python installations)

## Notes
- The tool does not fetch details for private IP addresses.
- Internet connection is required to fetch IP information.
- Data is fetched using the free tier of [ip-api.com](http://ip-api.com/), which may have request limits.

## License
This project is for educational purposes. 