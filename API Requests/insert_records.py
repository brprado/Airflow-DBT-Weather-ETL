from typing import final
from api_requests import mock_fetch_data
import psycopg2

def connect_to_db():
    print("Connecting to DB")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="db",
            user="postgres",
            password="postgres"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database Connection Failed: {e}")
        raise

def create_table(conn):
    print("Creating table if not exists...")

    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS dev;

        CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
            id SERIAL PRIMARY KEY,
            city TEXT,
            temperature FLOAT,
            weather_description TEXT,
            wind_speed FLOAT,
            time TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT NOW(),
            utc_offset TEXT
        );        
        """)
        conn.commit()

        print("The table dev.raw_weather_data Table was succesfully created!")
    except psycopg2.Error as e:
        print(f"There was an error while creating the table - {e}")


def insert_records(conn, data):
    """Insere dados climáticos na tabela raw_weather_data."""

    print("Inserting data into the table...")
    try:
        weather = data.get("current", {})
        location = data.get("location", {})

        query = """
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_description,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            )
            VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """

        values = (
            location.get("name"),
            weather.get("temperature"),
            weather.get("weather_descriptions", [None])[0],
            weather.get("wind_speed"),
            location.get("localtime"),
            location.get("utc_offset"),
        )

        with conn.cursor() as cursor:
            cursor.execute(query, values)

        conn.commit()
    except psycopg2.Error as e:
        print("Error inserting data into the table", e)

    print("Data inserted successfully.")

def main():
    try:
        data = mock_fetch_data()
        conn = connect_to_db()
        create_table(conn=conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error ocurred during execution: {e}")
    finally:
        if conn in locals():
            conn.close()
            print("DB connection closed")

main()