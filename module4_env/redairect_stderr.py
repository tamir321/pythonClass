import sys
# Save the original stderr
original_stderr = sys.stderr

# Open a file to redirect stderr
filename = "error.log"
try:
    file = open(filename, "w")
except IOError:
    print("Failed to open the file for error logging:", filename)
    sys.exit(1)

# Redirect stderr to the file
sys.stderr = file

# Generate an error to test the redirection
print(1 / 0)

# Restore stderr to its original state
sys.stderr = original_stderr

# Close the file
file.close()