# connect_database.py
import connect_database
# to not overload moosh requests
#import time

def process_data():
    # Connect to the database
    connection = connect_database.connect_to_database()

    # Fetch data from the database
    data = connect_database.fetch_data_from_database(connection)

    # Process and print the data
    for row in data:
        # Process each entry
        print(row)
        #time.sleep(1)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    process_data()