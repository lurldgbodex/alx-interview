# 0x03. Log Parsing

This program reads stdin line by line and computes metrics for an HTTP server access log.

## Usage

The program can be executed using the command line:

```shell

$ ./log_parser.py < access.log
```

The program reads each line of the access.log file (provided through stdin) and computes metrics for the following:

    File size: The total size of the files requested.
    HTTP status codes: The number of times each HTTP status code (200, 301, 400, 401, 403, 404, 405, 500) appears in the log.

The metrics are printed to the console every 10 lines, or when the program is interrupted with a keyboard interruption (Ctrl + C).

## Example

```yaml

$ ./log_parser.py < access.log
File size: 20958
200: 17
301: 2
400: 1
404: 1
```

In this example, the program read the access.log file and calculated that the total file size was 20,958 bytes. Additionally, it identified that the server returned HTTP status code 200 17 times, 301 twice, 400 once, and 404 once.

## Requirements

This program has no external dependencies, and can be executed using Python 3.
