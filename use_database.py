# connect_database.py
import connect_database
# to not overload moosh requests
import time
import subprocess


def call_moosh(firstname):
    # Define the arguments
    #arg1 = "auth-list"

    # Call the bash script with the arguments
    #result = subprocess.run(['./moosh.sh', arg1], capture_output=True, text=True)
    # Command using an argument
    result = subprocess.run(['echo', firstname], capture_output=True, text=True)

    # Check the return code and print the output
    if result.returncode == 0:
        print("Script executed successfully")
        print("Output:", result.stdout)
    else:
        print("Script failed")
        print("Error:", result.stderr)

def process_data():
    # Connect to the database
    connection = connect_database.connect_to_database()

    # Fetch data from the database
    data = connect_database.fetch_data_from_database(connection)

    # Process and print the data
    j = 0
    for row in data:
        firstname = row[1]
        # Process each entry
        print(firstname)
        j += 1
        #time.sleep(3)
        call_moosh(firstname)
        if (j >= 1): break


    # Close the database connection
    connection.close()

if __name__ == "__main__":
    process_data()