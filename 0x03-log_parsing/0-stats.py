#!/usr/bin/python3
"""
Script that reads stdin line by line & compute metrics
"""
import sys


def parse_line(line):
    """
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None

def print_stats(total_file_size, status_code_counts):
    """
    function that prints the stdin
    """
    print(f"Total file size: File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")


def main():
    total_file_size = 0
    status_code_counts = {}

    try:
        line_counter = 0
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is None:
                continue

            total_file_size += file_size
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            line_counter += 1
            if line_counter % 10 == 0:
                print_stats(total_file_size, status_code_counts)

        if line_counter % 10 != 0:
            print_stats(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_counts)
        sys.exit(0)

if __name__ == '__main__':
    main() 