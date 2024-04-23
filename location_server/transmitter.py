from flask import Flask, jsonify
import requests
import subprocess

app = Flask(__name__)

def get_current_time():
    try:
        # Execute the 'date' command using subprocess and capture its output
        time_output = subprocess.check_output(['date']).decode().strip()
        return time_output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

def get_location_from_ip():
    # Using a free IP-based geolocation service
    response = requests.get('https://ipinfo.io/json')
    data = response.json()
    # Extract latitude, longitude, and region from the response
    location = data.get('loc', '').split(',')
    region = data.get('region', '')
    if len(location) == 2:
        latitude, longitude = location
        return {'latitude': float(latitude), 'longitude': float(longitude), 'region': region}
    else:
        return None

@app.route('/get_location')
def get_location():
    # Get location from the geolocation-db.com API
    location_data = get_location_from_ip()
    if location_data:
        # Get current time
        current_time = get_current_time()
        if current_time:
            location_data['current_time'] = current_time
        return jsonify(location_data)
    else:
        return jsonify({'error': 'Failed to retrieve location'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567) 
