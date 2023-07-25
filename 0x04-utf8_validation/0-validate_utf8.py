#!/usr/bin/python3
"""
UTF-8 Validation algorithm
"""


def validUTF8(data):
    """
    Check the validity of a UTF-8 data set.
    """
    def check_following_bytes(num_following):
        """
        Check if the subsequent bytes of a multi-byte
        character are valid
        """
        for i in range(num_following):
            if i + idx + 1 >= len(data):
                return False
            if not (data[idx + i + 1] >> 6) == 0b10:
                return False
        return True

    idx = 0
    while idx < len(data):
        if data[idx] >> 7 == 0:
            idx += 1
        elif data[idx] >> 5 == 0b110:
            if not check_following_bytes(1):
                return False
            idx += 2
        elif data[idx] >> 4 == 0b1110:
            if not check_following_bytes(2):
                return False
            idx += 3
        elif data[idx] >> 3 == 0b11110:
            if not check_following_bytes(3):
                return False
            idx += 4
        else:
            return False
    return True
