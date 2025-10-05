import requests
import folium
import time
import webbrowser
import os

def get_iss_position(timeout = 10):
    url = "https://api.wheretheiss.at/v1/satellites/25544"
    try:
        # use the timeout you passed in
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # raises for 4xx/5xx so we hit except
        data = response.json()
        # make sure keys exist; return as floats
        return float(data.get('latitude')), float(data.get('longitude'))
    except Exception as e:
        print("Error fetching ISS position:", e)
        return None, None

        

def create_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=3)
    folium.Marker([lat, lon], tooltip ="ISS Location").add_to(m)
    m.save("iss.map.html")
    webbrowser.open(f"file://{os.path.abspath('iss.map.html')}")

if __name__ == "__main__":
    lat, lon = get_iss_position()
    if lat is None or lon is None:
        print("Could not retrieve ISS position.")
    else:
        print(f"ISS current position: Latitude {lat}, Longitude {lon}")
        create_map(lat, lon)

