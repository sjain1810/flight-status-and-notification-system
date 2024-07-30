import psycopg2

conn = psycopg2.connect(
    dbname="flight_status_database",
    user="YourUsername",
    password="YourPassword",
    host="localhost"
)

cursor = conn.cursor()
