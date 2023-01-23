#!/usr/bin/python3
''' utf-8 validation '''


def validUTF8(data):
    '''determine if a given data set represents valid UTF-8 encoding'''
    count = 0
    for num in data:
        # get the 8 least significant bits
        byte = num & 0b11111111
        # if the count is 0, check if byte is valid starting byte
        if count == 0:
            # check if byte starts with 0b10
            if (byte >> 5) == 0b110:
                count = 1
            # check if byte starts with ob110
            elif (byte >> 4) == 0b1110:
                count = 2
            # check if the byte starts with 0b1110
            elif (byte >> 3) == 0b11110:
                count = 3

            # check if byte starts with 0b0 or 0b11111 which are not
            # valid startig bytes
            elif byte >> 7 or byte >> 3 == 0b11111:
                return False

        # if count is not 0, check if byte starts with 0b10
        else:
            if (byte >> 6) != 0b10:
                return False
            count -= 1

        # If the count is not 0 at the end,
        # the data is not a valid UTF-8 encoding
    if count != 0:
        return False
    return True
