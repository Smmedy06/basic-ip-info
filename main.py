import requests
import ipaddress
import tkinter as tk
from tkinter import messagebox

# Function to check if an IP is private
def is_private_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False

# Function to get IP information using the ip-api.com API
def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            return {
                "IP": data["query"],
                "City": data["city"],
                "Region": data["regionName"],
                "Country": data["country"],
                "Timezone": data["timezone"],
                "ISP": data["isp"],
                "Latitude": data["lat"],
                "Longitude": data["lon"]
            }
        else:
            return None
    except Exception as e:
        return None

# Function called when "Get Info" button is clicked
def on_get_info():
    ip = ip_entry.get().strip()

    if not ip:
        messagebox.showwarning("Input Error", "Please enter an IP address.")
        return

    # Check if private
    if is_private_ip(ip):
        result_text.set(f"🔒 {ip} is a PRIVATE IP address.\nDetails not available.")
        return

    info = get_ip_info(ip)
    if info:
        output = "\n".join(f"{key}: {value}" for key, value in info.items())
        result_text.set(output)
    else:
        result_text.set("⚠️ Could not fetch IP information.\nPlease check the IP or try again later.")

# Auto detect user IP using https://api.ipify.org
def auto_detect_ip():
    try:
        response = requests.get("https://api.ipify.org")
        ip_entry.delete(0, tk.END)
        ip_entry.insert(0, response.text)
    except:
        messagebox.showerror("Error", "Failed to detect public IP")

# GUI Setup
window = tk.Tk()
window.title("Basic IP Info")
window.geometry("500x400")
window.resizable(False, False)
window.config(bg="#f0f4f7")

title_label = tk.Label(window, text="🔍 IP Information Tool", font=("Arial", 18, "bold"), bg="#f0f4f7")
title_label.pack(pady=10)

ip_entry = tk.Entry(window, font=("Arial", 14), width=30)
ip_entry.pack(pady=5)

button_frame = tk.Frame(window, bg="#f0f4f7")
button_frame.pack()

detect_button = tk.Button(button_frame, text="Detect My IP", command=auto_detect_ip, bg="#d9e6f2")
detect_button.pack(side="left", padx=5)

get_button = tk.Button(button_frame, text="Get Info", command=on_get_info, bg="#c1e1c1")
get_button.pack(side="left", padx=5)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 12), justify="left", wraplength=450, bg="#f0f4f7")
result_label.pack(pady=20)

footer = tk.Label(window, text="Project by Group 09", font=("Arial", 10), bg="#f0f4f7", fg="gray")
footer.pack(side="bottom", pady=10)

window.mainloop()
