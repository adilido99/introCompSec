import math


def hex2bin(string):
    return bin(int(string, 16))


def bin2hex(string):
    return hex(int(string, 2))


def fillupbyte(string):
    length = len(string)
    return string if length % 8 == 0 else string.rjust(length + (8 - (length % 8)), '0')


def hex2base64(string):
    """
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    >>> hex2base64('7368726f6f6d')
    'c2hyb29t'
    """

    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    binary_string = fillupbyte(hex2bin(string)[2:])

    length = len(binary_string)

    if length % 6 != 0:
        binary_string = binary_string.ljust(length + (6 - (length % 6)), '0')

    block_num = len(binary_string) // 6

    encode_string = ""

    first_ind = 0

    last_ind = first_ind + 6

    for i in range(block_num):
        encode_string += base64_table[int(binary_string[first_ind:last_ind], 2)]

        first_ind = last_ind

        last_ind = first_ind + 6

    length_encode_string = len(encode_string)

    return encode_string if length_encode_string % 4 == 0 else encode_string.ljust(
        length_encode_string + (4 - (length_encode_string % 4)), '=')


def int2base64(num):
    """
    >>> int2base64(0x61)
    'YQ=='
    >>> int2base64(0x78)
    'eA=='
    """
    return hex2base64(str(hex(num))[2:])


