import subprocess
import requests
import time

def get_location():
    # Use ipconfig or any other method to get Device B's IP address
    # Replace 'DEVICE_B_IP' with the actual IP address of Device B
    device_b_ip = '192.168.1.106' #replace by any local ip address
    ping_response = subprocess.run(['ping', '-c', '1', device_b_ip], capture_output=True)
    if ping_response.returncode == 0:
        # Ping successful, send a request to Device B for location
        response = requests.get(f'http://{device_b_ip}:4567/get_location')
        if response.status_code == 200:
            location_data = response.json()
            print("Location:", location_data)
        else:
            print("Failed to get location from Device B")
    else:
        print("Device B is not reachable")

while True:
    get_location()
    time.sleep(2)  # Ping every 10 seconds
