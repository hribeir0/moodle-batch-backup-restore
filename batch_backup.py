import sys, subprocess, csv

import re #secure strings to use in filename

# Clean strings to later write filenames
def secure_filename(input_string):
    # Replace invalid characters with underscores or remove them
    secure_str = re.sub(r'[\/:*?"<>|\'" "]', '_', input_string)

    # Optionally, remove leading/trailing spaces and dots to further secure the filename
    secure_str = secure_str.strip().strip('.')
    return secure_str


# Save files path
backup_folder = '/var/www/lms/moodledata/course_backups/' #'/var/www/moodledatas/backupsdev/'
#Expects a single argument identifying the category we want to process
category = sys.argv[1]
file = f'{backup_folder}category{category}.csv'

# Moodle Instalation path
moodle_path = '/var/www/lms/public_html'



def readList(file):
    courses = []
    with open(file, 'r') as csvfile:
        # csvreader gets each row as a list
        csvreader = csv.reader(csvfile)
        next(csvreader) #Skip CSV header
        for row in csvreader:
            courses.append(row)
    return courses

courses = readList(file)


def backup(courses):
    for course in courses:
        courseId = course[0]
        shortname = secure_filename(course[1])
        # Moosh command to run
        command = f'moosh -n course-backup --template -f {backup_folder}cat{category}-{courseId}-{shortname}.mbz {courseId}'
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=moodle_path)
            print(f"Successfully backed up course ID: {courseId}. Shortname: \'{shortname}\'")
            print(f"Backup Path:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to backup course ID: {courseId}. Shortname: \'{shortname}\'")
            print(f"Error Output:\n{e.stderr}")
            print(f"Return Code: {e.returncode}")

backup(courses)
