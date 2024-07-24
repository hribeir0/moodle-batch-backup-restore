import subprocess

def main():
    # Define the command and arguments
    moodle_path = "/var/www/html/moodledev"
    arg1 = 5
    html_message = '<a href="google.com" target="_blank">google</a>'
    command = f'moosh -n activity-add -n title2 -o "--intro={html_message}" --section 3 page {arg1}'

    # Print the command for debugging purposes
    print(f"Executing command: {command}")

    # Execute the command
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=moodle_path)
        print("Command output:", result.stdout)
        print("Command error (if any):", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
