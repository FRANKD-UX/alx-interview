#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import re


def print_stats(total_size, status_codes):
    """
    Print statistics including total file size and count of each status code.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing counts of status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Main function to parse stdin line by line and compute metrics.
    """
    # Initialize variables
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    line_count = 0

    # Regular expression to match the expected log format
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)

            if match:
                # Extract status code and file size from the matched line
                status_code = match.group(3)
                file_size = int(match.group(4))

                # Update total file size
                total_size += file_size

                # Update status code count if it's one we're tracking
                if status_code in status_codes:
                    status_codes[status_code] += 1

            # Increment line count
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass
    finally:
        # Print statistics one last time
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
