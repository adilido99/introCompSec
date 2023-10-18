def hex2string(text):
    """
    >>> hex2string('61')
    'a'
    >>> hex2string('776f726c64')
    'world'
    >>> hex2string('68656c6c6f')
    'hello'
    """
    length = len(text) // 2
    new_text = ""
    for i in range(length):
        new_text += chr(int(text[:2], 16))
        text = text[2:]
    return new_text


def string2hex(text):
    """
    >>> string2hex('a')
    '61'
    >>> string2hex('hello')
    '68656c6c6f'
    >>> string2hex('world')
    '776f726c64'
    >>> string2hex('foo')
    '666f6f'
    """
    new_text = ""
    for i in range(len(text)):
        new_text += str(hex(ord(text[i])))[2:]
    return new_text


def hex_xor(text1, text2):
    """
    >>> hex_xor('0aabbf11','12345678')
    '189fe969'
    >>> hex_xor('12cc','12cc')
    '0000'
    >>> hex_xor('1234','2345')
    '3171'
    >>> hex_xor('111','248')
    '359'
    >>> hex_xor('8888888','1234567')
    '9abcdef'
    """
    new_text = ""
    for i in range(len(text1)):
        new_text += hex(int(text1[i], 16) ^ int(text2[i], 16) )[2:]
    return new_text


def encrypt_single_byte_xor(text1, text2):
    """
    >>> encrypt_single_byte_xor('aaabbccc','00')
    'aaabbccc'
    >>> encrypt_single_byte_xor(string2hex('hello'),'aa')
    'c2cfc6c6c5'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
    'hello'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
    'Encrypt and decrypt are the same'
    """
    new_text = ""
    for i in range(len(text1) // 2):
        new_text += hex_xor(text1[:2], text2)
        text1 = text1[2:]
    return new_text


keys = []
for i in range(256):
    text = hex(i)[2:]
    keys.append(text.zfill(len(text) + (2 - len(text) % 2) % 2))

valid_characters = "abcdefghijklmnopqrstuvxyz ABCDEFGHIJKLMNOPQRSTUVXYZ"


def count_char(text):
    count = 0
    for j in valid_characters:
        count += text.count(j)
    return count


def decrypt_single_byte_xor(message):
    """
    >>> decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480')
    'Hi! You have found me!'
    >>> decrypt_single_byte_xor('b29e9f96839085849d9085989e9f82d1889e84d199908794d197989f95d1859994d181908282869e8395d0')
    'Congratulations you have find the password!'
    >>> decrypt_single_byte_xor('e1ded996ddd8d9c1c596c1ded7c296dfc596ded7c6c6d3d8dfd8d18996e1ded3c4d396d7db96ff89')
    'Who knows what is happening? Where am I?'
    """
    dec_message = ""
    maxi = 0
    for key in keys:
        dec = hex2string(encrypt_single_byte_xor(message, key))
        #print(hex2string(dec))
        point = count_char(dec)
        if point >= maxi:
            dec_message = dec
            maxi = point
    return dec_message

#print(decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480'))
#print(hex(int("0b1010", 2)) ^ hex(int("0b1000", 2)))
