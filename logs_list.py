# -*- coding: utf-8 -*-

"""
Write a Python function that:
Reads a log file (simulated by a list of strings).
Parses each log entry into a structured dictionary with the following keys:

timestamp: The timestamp of the log entry.
level: The log level (INFO, ERROR, WARNING).
message: The main log message.
metadata: Any additional key-value data after the message.

Returns a list of parsed log entries.

example_logs = [
    "2025-02-24 12:45:30,INFO,User login successful,user_id=123",
    "2025-02-24 12:46:10,ERROR,Failed to connect to database,db_host=db.internal",
    "2025-02-24 12:47:05,WARNING,High memory usage detected,usage=95%"
]
"""

import re


def parse_logs(logs):

    parsed_logs = []
    for log_entry in logs:
        try:
            parts = log_entry.split(",", 2)  # Split at most twice
            timestamp = parts[0]
            level = parts[1]
            message_and_metadata = parts[2]

            # Split message and metadata using a regular expression
            match = re.match(r"(.+?)(,(.*))?", message_and_metadata) # Non-greedy match for message
            message = match.group(1).strip()
            metadata_str = match.group(3)

            metadata = {}
            if metadata_str:
                for item in metadata_str.split(","):
                    key, value = item.split("=")
                    metadata[key.strip()] = value.strip()

            parsed_log = {
                "timestamp": timestamp,
                "level": level,
                "message": message,
                "metadata": metadata
            }
            parsed_logs.append(parsed_log)

        except IndexError:  #handles cases where the log format is incorrect.
            print(f"Skipping invalid log entry: {log_entry}")
            continue #proceeds to the next log entry

        except ValueError as e: #Handles cases where the metadata key-value pairs are not correctly formatted.
            print(f"Skipping invalid log entry due to ValueError: {log_entry}. Error: {e}")
            continue #proceeds to the next log entry

    return parsed_logs


logs = [
    "2025-02-24 12:45:30,INFO,User login successful,user_id=123",
    "2025-02-24 12:46:10,ERROR,Failed to connect to database,db_host=db.internal",
    "2025-02-24 12:47:05,WARNING,High memory usage detected,usage=95%",
    "2025-02-24 12:48:00,DEBUG,Test message", # Example with no metadata
    "2025-02-24 12:49:00,INFO,Another message,key1=value1,key2=value2", # Example with multiple metadata entries
    "2025-02-24 12:50:00,INVALID_LOG_FORMAT", # Example with incorrect format
    "2025-02-24 12:51:00,ERROR,Database Error,key=value1;value2" # Example with incorrect metadata formatting
]

parsed_logs = parse_logs(logs)
for log in parsed_logs:
    print(log)
