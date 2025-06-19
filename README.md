# 🛰️ IP-INFORMATION-TOOL

*Quickly Retrieve IP Address Details with an Intuitive Python GUI*

![last commit](https://img.shields.io/github/last-commit/your-username/your-repo-name?style=flat&logo=git)
![python](https://img.shields.io/badge/python-100%25-blue?logo=python)
![languages](https://img.shields.io/badge/languages-1-informational)

---

## 🧰 Built With:

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/-Tkinter-FFCC00?style=flat&logo=python&logoColor=black)
![Requests](https://img.shields.io/badge/-Requests-20232a?style=flat&logo=python&logoColor=white)

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
