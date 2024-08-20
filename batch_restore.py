import os, subprocess
import re

# Moodle destination path
moodle_path = '/var/www/html/moodle401'
# Folder where MBZ files are stored
backups_path = '/var/www/moodledatas/backupsdev/'
# Moosh Command
mooshCommand = 'moosh -n course-restore --ignore-warnings'

# Get destiny category from the mbz file
def extract_number(input_string):
    # Use a regular expression to match 'cat' followed by one or more digits, and then a hyphen
    match = re.search(r'cat(\d+)-', input_string)

    # If a match is found, return the number (group 1)
    if match:
        return match.group(1)
    else:
        return None

for file in os.listdir(backups_path):
    if file.endswith('mbz'):
        # Get category destination
        targetCat = (extract_number(file))
        # Build the command with the correct path and arguments
        restoreCommand = f'{mooshCommand} {backups_path}{file} {targetCat}'
        try:
            result = subprocess.run(restoreCommand, shell=True, check=True, capture_output=True, text=True, cwd=moodle_path)
            print(f"Successfully restored file: {file} to category: {targetCat}")
        except subprocess.CalledProcessError as e:
            print(f"Failed on file: {file}")
            print(f"Error Output:\n{e.stderr}")
            print(f"Return Code: {e.returncode}")

