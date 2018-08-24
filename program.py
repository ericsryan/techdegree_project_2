import os
import string
from one_time_pad import OneTimePad
from keyword_cipher import Keyword
from polybius_cipher import Polybius
from transposition_cipher import Transposition




cipher = ''
encrypt_decrypt = ''
pad_option = ''
block_option = ''
keyword = ''
message = ''
output = ''


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_screen():
    clear_screen()
    print('_' * 60 + '\n\n' + ' ' * 15 + 'Welcome to the \
Cryptographer!\n' + '_' * 60 + '\n')
    if cipher:
        print("Cipher:", cipher)
    if encrypt_decrypt:
        print("Method:", encrypt_decrypt)
    if keyword:
        print("Keyword:", keyword)
    if message:
        print("Original message:", message)
    if output:
        print("{}ed Message:".format(encrypt_decrypt), output)

def select_cipher():
    draw_screen()
    print('    Ciphers available:')
    print(
    """
    -Transposition
    -Keyword
    -Polybius

        """)
    while cipher[0] not in 'TKP':
        cipher = input("    Which cipher would you like to use? ")
        if cipher[0].upper() == 'T':
            cipher = 'Transposition'
        elif cipher[0].upper() == 'K':
            cipher = 'Keyword'
        elif cipher[0].upper() == 'P':
            cipher = 'Polybius'
        else:
            draw_screen()
            print('    Ciphers available:')
            print(
            """
    -Transposition
    -Keyword
    -Polybius

                """)
            cipher = input("That is not one of the available ciphers. \nWhich cipher would you like to use? ")

def select_encrypt_decrypt():
    draw_screen()
    encrypt_decrypt = input("    Would you like to encrypt or decrypt your message? ")
    if encrypt_decrypt[0].upper() == 'E':
        encrypt_decrypt = 'Encrypt'
    elif encrypt_decrypt[0].upper() == 'D':
        encrypt_decrypt = 'Decrypt'
    return encrypt_decrypt

def select_message():
    draw_screen()
    message = input("    What is the message you would like to {}".format(encrypt_decrypt.lower()))
    return message

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
    print(''.join(block_message))

def select_pad():
    draw_screen()
    pad_option = input("    Would you like to use a one time pad? \n\
    If you do you may enter it now or press 'Enter' to continue without one: ")

def select_block():
    draw_screen()
    block_option = input("    Would you like to format your message into blocks \
of five? If you do you will lose the spaces and punctuation in your \
message. Y/N? ")
    return block_option

def continue_quit():
    draw_screen()
    continue_quit = input("    Would you like to use another cipher? If you do enter 'Y' or enter 'Q' to quit: ")


clear_screen()
draw_screen()
select_cipher()
continue_quit()

"""
To Do:

-Add messages if invalid input

"""

"""
Main script:

-Prompt user for Cipher
-Prompt user for encrypt_decrypt
-Prompt user for keyword if applicable
-Prompt user for pad
-Prompt user for blocks of 5
-Display encrypt_decrypt message
-Prompt user continue or quit

"""
