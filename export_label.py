import subprocess
import sys

moodle_path = '/var/www/html/moodledev'

html_message = '<div class=\'alert warning\'>Your HTML content here</div>'
course = sys.argv[1]
command = f'moosh -n activity-add -n title2 -o "--intro={html_message}" --section 1 label 5'
print(command)
subprocess.run(command, shell=True, executable="/bin/bash", cwd=moodle_path)