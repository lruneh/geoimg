import os
import requests
#import GPS

def get_location(lat, long):
    newUri = 'https://nominatim.openstreetmap.org/search.php?q=%s,%s&polygon_geojson=1&format=jsonv2&addressdetails=1' % (lat, long)
    headers = {}
    response = requests.get(newUri, headers=headers)
    try:
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as e:
        #print(str(e))
        return {}