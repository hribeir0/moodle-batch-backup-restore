# connect_database.py
import mysql.connector
import sys

def connect_to_database():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='moodledude',
            password='correio',
            database='moodle401'
        )

        if connection.is_connected():
            print("Connected to the database")
            return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

def fetch_data_from_database(connection):
    sql = """SELECT id, intro FROM mdl_label
        """
    try:
        cursor = connection.cursor()
        # Execute the query
        cursor.execute(sql)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        return rows

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

def main():
    connection = connect_to_database()
    data = fetch_data_from_database(connection)
    print(data)
    # Process and print the data
    for row in data:
        # Process each entry
        print(row)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
