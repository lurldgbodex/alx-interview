#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''
import sys
import re


# reg exp to match log format
pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
pattern_fmt = '{}\\-{}{}{}{}\\s*'.format(
        pattern[0], pattern[1], pattern[2], pattern[3], pattern[4])

total_size = 0
count = 0

status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }


def log_parse(status_codes, total_size):
    ''''prints the status_code and size'''
    print('File size: {:d}'.format(total_size))
    for status in sorted(status_codes):
        if status_codes[status] != 0:
            print('{}: {:d}'.format(status, status_codes[status]))


for line in sys.stdin:
    match = re.fullmatch(pattern_fmt, line)
    if match:
        status_code = match.group('status_code')
        total_size += int(match.group('file_size'))

    try:
        if status_code in sorted(status_codes.keys()):
            status_codes[status_code] += 1
            if count % 10 == 0 and count != 0:
                log_parse(status_codes, total_size)
            count += 1
    except keyboardInterrupt:
        log_parse(status_codes, total_size)
