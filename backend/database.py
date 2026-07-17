import psycopg2
def get_connection():
    return psycopg2.connect(host="localhost",database="smart_parking_db",user="postgres",password="Hari@2328",port="5432")
