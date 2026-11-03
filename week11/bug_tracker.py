"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

timestamp = datetime.datetime.now()
# 💡 TODO: create a while loop that will ask the user for information to generate a log
while True:
    print("Enter 'log' to record a bug, or 'quit' to stop: ", end="")
    user_input = input().strip().lower()
    if user_input == "quit":
        break
    elif user_input == "log":
        with open("bug_log.txt", "a") as bug_log:
            timestamp = datetime.datetime.now()
            file_name = input("File name: ")
            description = input("Description of error: ")
            priority = input("Priority (High, Medium, Low): ")
            bug_log.write(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}]\n")
        print("Bug log updated!")


"""
Expected output:
Enter 'log' to record a bug, or 'quit' to stop: log
File name: main.py
Description of error: TypeError when concatenating string and int
Priority (High, Medium, Low): High

Enter 'log' to record a bug, or 'quit' to stop: quit
Bug log updated!
"""
"""
Expected bug_log.txt content:
[2026-03-31 14:22:05]
File: main.py
Status: TypeError when concatenating string and int
Priority: High
--------------------------------------------------
"""
