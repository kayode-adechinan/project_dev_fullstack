import socket
from mysql.connector import connect


from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


db_conn = connect(
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
    autocommit=True,
)

cursor = db_conn.cursor()

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


insert_records_query = """
INSERT INTO records (speed, duration, latitude, longitude, datetime)
VALUES
    (%s, %s, %s, %s, %s)
"""


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # conn.sendall(data)
            line = data.decode()
            line = bytes.fromhex(line).decode("utf-8")
            # print(data.decode())
            # line = data.decode()
            print(line)
            line = line.split(",")
            line = [item.strip() for item in line]
            line = tuple(line)
            print(line)
            cursor.execute(
                insert_records_query,
                line,
            )
            # db_conn.commit()
