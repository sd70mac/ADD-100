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
    pass

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
