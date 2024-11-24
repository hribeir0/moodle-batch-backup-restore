import sys, subprocess
import pandas as pd

file = sys.argv[1]
df = pd.read_csv(file)
moodle_path = '/var/www/html/moodledev/'

data = df.groupby('course')['useridnumber'].apply(list).to_dict()

# Initialize a list to store the resulting strings
result_strings = []

for course, user_ids in data.items():
    result = f"{course} " + " ".join((user_ids))
    result_strings.append(result)

for result in result_strings:
    command = 'moosh -n course-enrol ' + result
    # print (command)
    try:
        call = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=moodle_path)
        print(f"Command: {command}")
       # print(f"Backup Path:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Failed course: {course}.")
        print(f"Error Output:\n{e.stderr}")
        print(f"Return Code: {e.returncode}")