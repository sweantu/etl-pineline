import psycopg2

# export PYTHONPATH=$PYTHONPATH:$(pwd)
from app.config.config import DATABASE_CONFIG


def create_tables():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather_data (
        id SERIAL PRIMARY KEY,
        city VARCHAR(50),
        temperature FLOAT,
        humidity INT,
        wind_speed FLOAT,
        date_time TIMESTAMP
    );
    """

    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()
