from flask import Flask, jsonify
import requests
import subprocess
import json

app = Flask(__name__)

def get_current_time():
    time_output = subprocess.check_output(['date']).decode().strip()
    return time_output
    

def battery_status():
    batt_op = subprocess.check_output(['termux-battery-status'], universal_newlines=True)
        # Parse the output as JSON
    batt_op_json = json.loads(batt_op)
    return batt_op_json
    

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
        print('\n')
    else:
        return None

@app.route('/get_location')
def get_location():
    
    current_time = get_current_time()                 
    batt_status = battery_status()
    location_data = get_location_from_ip()
    if location_data:
        return jsonify( location_data, {'health': batt_status, 'time': current_time})

    
 #   else:
#        location_data["Health"]=batt_status                        location_data["Time"]=current_time
  #                                                                 return jsonify(location_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567)  
