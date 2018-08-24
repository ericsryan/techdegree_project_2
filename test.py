import os
import string

from one_time_pad import OneTimePad
from keyword_cipher import Keyword
from polybius_cipher import Polybius
from transposition_cipher import Transposition



    # os.system('cls' if os.name == 'nt' else 'clear')

def draw_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('_' * 60 + '\n\n' + ' ' * 15 + 'Welcome to the \
Cryptographer!\n' + '_' * 60 + '\n')
    if cipher:
        print("Cipher:", cipher)
    if encrypt_decrypt:
        print("Method:", encrypt_decrypt)
    if pad_option:
        print("Pad in use")
    if block_option.upper() == 'Y':
        print("Message will be formatted")
    if keyword:
        print("Keyword:", keyword)
    if message:
        print("Original message:", message)

def ciphers_available():
    print('    Ciphers available:')
    print(
    """
        -Transposition
        -Keyword
        -Polybius

        """)

def blocks_of_five(message):
    message = message.upper()
    block_message = []
    for character in message:
        if character in string.ascii_uppercase:
            block_message.append(character)
    if len(block_message) % 5 == 1:
        block_message.extend(['5', '1', '3', '4'])
    elif len(block_message) % 5 == 2:
        block_message.extend(['8', '7', '3'])
    elif len(block_message) % 5 == 3:
        block_message.extend(['4', '6'])
    elif len(block_message) % 5 == 4:
        block_message.extend(['8'])
    counter = 5
    for i in range(int(len(block_message) / 5) - 1):
        block_message.insert(counter, ' ')
        counter += 6
    return ''.join(block_message)

def use_pad():
    new_instance = OneTimePad()
    if encrypt_decrypt == 'Encrypt':
        return new_instance.encrypt(pad_option, output)
    else:
        return new_instance.decrypt(pad_option, output)

def check_cipher():
    while cipher[0] not in 'TKP':
        if cipher == '':
            cipher = 'null'
        if cipher[0].upper() in 'TKP':
            if cipher[0].upper() == 'T':
                cipher = 'Transposition'
            elif cipher[0].upper() == 'K':
                cipher = 'Keyword'
            elif cipher[0].upper() == 'P':
                cipher = 'Polybius'
        else:
            pass



if __name__ == '__main__':

    while True:
        cipher = ''
        encrypt_decrypt = ''
        pad_option = ''
        block_option = ''
        keyword = ''
        message = ''
        output = ''
        # Select cipher
        draw_screen()
        ciphers_available()
        while True:
            try:
                cipher = input("What cipher would you like to use today? ")
                if cipher.upper() == 'TRANSPOSITION':
                    cipher = 'Transposition'
                    break
                elif cipher.upper() == 'KEYWORD':
                    cipher = 'Keyword'
                    break
                elif cipher.upper() == 'POLYBIUS':
                    cipher = 'Polybius'
                    break
                else:
                    raise ValueError
            except ValueError:
                cipher = ''
                draw_screen()
                ciphers_available()
                cipher = print("That isn't an available cipher.")

        # Select encrypt/decrypt
        # Select pad
        # Select blocks of five if applicable
        # Choose keyword if applicable
        # Enter message
        # Display output
