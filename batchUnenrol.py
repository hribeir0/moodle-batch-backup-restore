import sys, subprocess, csv

import re #secure strings to use in filename

file = f'/home/ubuntu/all.csv'

# Moodle Instalation path
moodle_path = '/var/www/lms/public_html/'



def readList(file):
    courses = []
    with open(file, 'r') as csvfile:
        # csvreader gets each row as a list
        csvreader = csv.reader(csvfile)
        #next(csvreader) #Skip CSV header
        for row in csvreader:
            courses.append(row)
    return courses

courses = readList(file)


def backup(courses):
    for course in courses:
        courseId = course[0]
        # Moosh command to run
        command = f'sudo moosh -n course-enrol -r editingteacher {courseId} admin'
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=moodle_path)
            print(f"Info for course ID: {courseId}.")
            print(f"Backup Path:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Failed fetch course ID: {courseId}.")
            print(f"Error Output:\n{e.stderr}")
            print(f"Return Code: {e.returncode}")

backup(courses)
