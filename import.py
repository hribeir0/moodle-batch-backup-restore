import subprocess

# Define the arguments
arg1 = "cache-clear"

# Call the bash script with the arguments
result = subprocess.run(['./moosh.sh', arg1], capture_output=True, text=True)

# Check the return code and print the output
if result.returncode == 0:
    print("Script executed successfully")
    print("Output:", result.stdout)
else:
    print("Script failed")
    print("Error:", result.stderr)