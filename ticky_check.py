#!/usr/bin/env python3

import re
import sys
import operator
import csv

def generate_report():
    pattern = re.compile(r"ticky: ([\w.]*) (.*) (\((.*?)\))")
    filename = sys.argv[1]
    error = {}
    user = {}

    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            match = pattern.search(line)
            if match:
                user.setdefault(match.group(4), {"INFO": 0, "ERROR": 0})
                if match.group(1) == "INFO":
                    user[match.group(4)]["INFO"] += 1
                if match.group(1) == 'ERROR':
                    user[match.group(4)]["ERROR"] += 1
                    error.setdefault(match.group(2), 0)
                    error[match.group(2)] += 1
     
    return (sorted(error.items(), key=operator.itemgetter(1), reverse=True), sorted(user.items(), key=operator.itemgetter(0)))

def save_to_csv(header, obj, filename):
    with open(filename, 'w+') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        for row in obj:
            if isinstance(row[1], dict):
                csv_writer.writerow([row[0], row[1]['INFO'], row[1]['ERROR']])
            else:
                csv_writer.writerow(row)

if __name__ == "__main__":
    error_header = ["Error", "Count"]
    user_header = ["Username", "INFO", "ERROR"]
    error, user = generate_report()
    save_to_csv(error_header, error, "error_message.csv")
    save_to_csv(user_header, user, "user_statistics.csv")
