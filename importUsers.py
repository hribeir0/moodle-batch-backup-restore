import sys, subprocess, csv
file = sys.argv[1] #Use an argument to call the file

moodle_path = '/var/www/html/moodledev'

def addUser(password: str, email: str, country: str, department: str, firstname: str, lastname: str, username: str):
    command = f'moosh -n user-create --password {password} --email {email} --country {country} --department {department} --firstname \'{firstname}\' --lastname {lastname} {username}'
    return command

def readList(file):
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
    command = addUser(user[5], user[4], user[6], user[7], user[2], user[3], user[1])
    print (addUser(user[5], user[4], user[6], user[7], user[2], user[3], user[1]))
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=moodle_path)
        print(f"Command: {command}.")
        print(f"Backup Path:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Failed username: {user[1]}.")
        print(f"Error Output:\n{e.stderr}")
        print(f"Return Code: {e.returncode}")