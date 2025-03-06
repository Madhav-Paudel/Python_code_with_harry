# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

def list_directory_contents(directory_path):
    # here we use the  exception handel by using try and except 
    try:
        # Get the list of all files and directories in the specified directory
        entries = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '/'  # Replace with your directory path
list_directory_contents(directory_path)
