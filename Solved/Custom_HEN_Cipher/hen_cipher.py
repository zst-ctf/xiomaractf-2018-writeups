import string


'''
HEN encryption:

'size of plaintext' is number of alphabets in plaintext

Multiply the position of alphabet (starting with one) with
'size of plaintext'  and do mod 26.
now left shift the PT every alphabet with their
corresponding value

Example for HEN encryption scheme:

Plaintext : I_AM
Size of plaintext : 3
Ciphertext: F_UD
'''

charset = string.ascii_uppercase

def hen_getsize(text):
    return len(text.replace('_', ''))

def hen_shift_left(ch, shift):
    index = charset.index(ch) - shift
    while index < 0:
        index += 26

    if index > 25:
        index %= 26

    return charset[index]

def hen_decrypt(ciphertext):
    plaintext = ''
    position = 0
    size = hen_getsize(ciphertext)
    for ch in ciphertext:
        if ch not in charset:
            plaintext += ch
        else:
            position += 1
            # Multiply the position of alphabet (starting with one)
            # with 'size of plaintext' and do mod 26.
            shift = (position * size) % 26

            # do right shift to decrypt (hence negative shift)
            plaintext += hen_shift_left(ch, -shift)
    return plaintext

assert hen_decrypt('F_UD') == 'I_AM'

