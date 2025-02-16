import psycopg2

from app.config.config import DATABASE_CONFIG
from app.scripts.transform import transform_data


def load_data():
    df = transform_data()
    if df is None or df.empty:
        print("❌ No data to insert")
        return

    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()

    insert_query = """
    INSERT INTO weather_data (city, temperature, humidity, wind_speed, date_time)
    VALUES (%s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cur.execute(
            insert_query,
            (row.city, row.temperature, row.humidity, row.wind_speed, row.date_time),
        )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data inserted successfully!")


if __name__ == "__main__":
    load_data()
