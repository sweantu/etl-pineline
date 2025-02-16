import pandas as pd

from app.scripts.extract import extract_data


def transform_data():
    raw_data = extract_data()
    if not raw_data:
        return None

    hourly_data = raw_data["hourly"]
    df = pd.DataFrame(
        {
            "city": "New York",
            "temperature": hourly_data["temperature_2m"],
            "humidity": hourly_data["relative_humidity_2m"],
            "wind_speed": hourly_data["wind_speed_10m"],
            "date_time": hourly_data["time"],
        }
    )

    df["date_time"] = pd.to_datetime(df["date_time"])
    return df


if __name__ == "__main__":
    df = transform_data()
    print(df.head())
