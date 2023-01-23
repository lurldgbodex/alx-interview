#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''
import sys
import re


total_size = 0
count = 0

status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }


def log_parse(status_codes, total_size):
    ''''prints the status_code and size'''
    print('File size: {:d}'.format(total_size))
    for status in sorted(status_codes):
        if status_codes[status] > 0:
            print('{}: {:d}'.format(status, status_codes[status]))


try:
    for line in sys.stdin:
        params = line.strip().split()
        if len(params) != 9:
            continue
        status_code = params[7]
        file_size = params[8]

        # check if status code is one of the possible ones
        if status_code in status_codes:
            status_codes[status_code] += 1

        # check if file size is an integer
        try:
            file_size = int(file_size)
        except ValueError:
            continue

        total_size += file_size
        count += 1

        # print stats every 10 lines or keyboard interruption
        if count % 10 == 0:
            log_parse(status_codes, total_size)

except keyboardInterrupt:
    # print final stats
    log_parse(status_codes, total_size)
