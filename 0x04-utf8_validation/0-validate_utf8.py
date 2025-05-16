#!/usr/bin/python3
"""
UTF-8 Validation Module
This module contains a function to validate if a data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    UTF-8 encoding rules:
    - 1-byte character: 0xxxxxxx
    - 2-byte character: 110xxxxx 10xxxxxx
    - 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
    - 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Args:
        data (list): A list of integers where each integer represents 1 byte of data.
                     Only the 8 least significant bits are considered.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes to process for the current character
    bytes_to_process = 0

    for byte in data:
        # Only consider the 8 least significant bits
        byte = byte & 0xFF

        # If we are not currently processing a multi-byte character
        if bytes_to_process == 0:
            # Determine the number of bytes for the current character
            if byte >> 7 == 0:  # 0xxxxxxx - 1 byte character
                continue
            elif byte >> 5 == 0b110:  # 110xxxxx - 2 byte character
                bytes_to_process = 1
            elif byte >> 4 == 0b1110:  # 1110xxxx - 3 byte character
                bytes_to_process = 2
            elif byte >> 3 == 0b11110:  # 11110xxx - 4 byte character
                bytes_to_process = 3
            else:
                # Invalid UTF-8 starting byte
                return False
        else:
            # Continuation bytes must start with '10'
            if byte >> 6 != 0b10:
                return False
            bytes_to_process -= 1

    # All characters must be complete
    return bytes_to_process == 0
