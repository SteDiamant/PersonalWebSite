import requests

def get_longitude_latitude(address):
    base_url = "https://nominatim.openstreetmap.org/search"

    # Set up the parameters for the API request
    params = {
        "q": address,
        "format": "json",
    }

    try:
        # Send the API request
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the API call was successful and returned results
        if data:
            # Extract the latitude and longitude from the API response
            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])
            return latitude, longitude
        else:
            print("Geocoding API call failed or returned no results.")
            return None, None

    except requests.exceptions.RequestException as e:
        # If there was an error making the API request
        print(f"Error making the API request: {e}")
        return None, None