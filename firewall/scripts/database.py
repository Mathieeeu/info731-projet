import MySQLdb

def fetch_firewall_logs():
    try:
        # Connexion à la base de données
        connection = MySQLdb.connect(
            host='5.6.1.2',
            user='root',
            passwd='password',
            db='firewall_logs'
        )

        cursor = connection.cursor()
        cursor.execute("USE firewall_logs")
        cursor.execute("SELECT * FROM http_requests")

        rows = cursor.fetchall()
        print("Total number of rows in http_requests: ", cursor.rowcount)

        print("\nFetching each row")
        for row in rows:
            print("ID =", row[0])
            print("Timestamp =", row[1])
            print("Source IP =", row[2])
            print("Curl Content =", row[3])
            print("Allowed =", row[4], "\n")

    except MySQLdb.Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    fetch_firewall_logs()
