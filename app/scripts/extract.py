import requests

from app.config.config import API_URL


def extract_data(city="New York"):
    params = {
        "latitude": 40.71,  # New York City
        "longitude": -74.01,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "America/New_York",
    }
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Failed to fetch data")
        return None


if __name__ == "__main__":
    data = extract_data()
    print(data)
