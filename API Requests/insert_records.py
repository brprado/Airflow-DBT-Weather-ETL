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


def insert_records():
    pass

if __name__ == "__main__":
    conn = connect_to_db()
    create_table(conn=conn)

