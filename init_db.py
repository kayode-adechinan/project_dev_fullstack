from mysql.connector import connect

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


def create_db():
    # establishing the connection
    conn = connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
    )

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    create_db_query = "CREATE DATABASE IF NOT EXISTS " + DB_NAME

    cursor.execute(create_db_query)

    # Closing the connection
    conn.close()


def create_table():
    # establishing the connection
    conn = connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
    )

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    create_records_table_query = """
    CREATE TABLE IF NOT EXISTS records(
        id INT AUTO_INCREMENT PRIMARY KEY,
        speed VARCHAR(8),
        duration VARCHAR(8),
        latitude VARCHAR(12),
        longitude VARCHAR(12),
        datetime  VARCHAR(28)
    )
    """
    cursor.execute(create_records_table_query)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()


if __name__ == "__main__":
    create_db()
    create_table()
