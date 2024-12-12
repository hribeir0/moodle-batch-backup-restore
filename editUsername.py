import sys, subprocess, csv
file = sys.argv[1] #Use an argument to call the file

moodle_path = '/var/www/html/moodledev'

def editUsername(username: str, email: str):
    """Moosh command to update user changing username to match the email

    Args:
        username (str): Username that we want to change
        email (str): Email to change the username into

    Returns:
        str: Moosh command
    """
    command = f'moosh -n user-mod --username {email} {username}'
    return command

def readList(file):
    """Reads a csv file and adds users to a list

    Args:
        file str: File path

    Returns:
        list: List of users, each with a list of fields according to the csv header position
    """
    users = []
    with open(file, 'r') as csvfile:
        # csvreader gets each row as a list
        csvreader = csv.reader(csvfile)
        next(csvreader) #Skip CSV header
        for row in csvreader:
            users.append(row)
    return users

users = readList(file)

for user in users:
    command = editUsername(user[0], user[1])
    print (editUsername(user[0], user[1]))
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=moodle_path)
        print(f"Status:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Failed username: {user[1]}.")
        print(f"Error Output:\n{e.stderr}")
        print(f"Return Code: {e.returncode}")