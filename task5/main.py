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


def encrypt_by_add_mod(text, key):
    """
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    """
    hex_string = string2hex(text)
    new_text = ""

    for i in range(len(hex_string) // 2):
        new_text += hex2string(hex((int(hex_string[:2], 16) + key) % 256)[2:])
        hex_string = hex_string[2:]
    return new_text


def encrypt_xor_with_changing_key_by_prev_cipher(text, key, param):
    """
    >>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
    '3V:V9'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    """
    if param == 'encrypt':
        new_text = ""
        for i in range(len(text)):
            new_key = ord(text[i]) ^ key
            new_text += chr(new_key)
            key = new_key
        return new_text
    else:
        new_text = ""
        for i in range(len(text)):
            new_text += chr(ord(text[i]) ^ key)
            key = ord(text[i])
        return new_text


def create_chunk(text):
    chunks = []
    for i in range(4):
        j = i
        mini_text = ""
        while j < len(text):
            mini_text += text[j]
            j += 4
        chunks.append(mini_text)
    return chunks


def join_chunk(chunk):
    text = ""
    for i in range(len("".join(chunk))):
        for j in range(4):
            if i < len(chunk[j]):
                text += chunk[j][i]
    return text


def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(text, key_list, param):
    """
        >>> key_list = [0x20, 0x44, 0x54, 0x20]
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt')
        'A&7D$@P'
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt')
        'A%5B#GW'
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
        ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),
        ...        key_list,'decrypt')
        'abcdefg'
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
        ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),
        ...        key_list,'decrypt')
        'Hellobello, it will work for a long message as well'
    """
    chunks = create_chunk(text)
    container_chunk = []
    if param == "encrypt":
        for i in range(len(chunks)):
            container_chunk.append(encrypt_xor_with_changing_key_by_prev_cipher(chunks[i], key_list[i], 'encrypt'))
        return join_chunk(container_chunk)
    else:
        for i in range(len(chunks)):
            container_chunk.append(encrypt_xor_with_changing_key_by_prev_cipher(chunks[i], key_list[i], 'decrypt'))
        return join_chunk(container_chunk)
