import os
import string

from one_time_pad import OneTimePad
from keyword_cipher import Keyword
from polybius_cipher import Polybius
from transposition_cipher import Transposition



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

if __name__ == '__main__':

    while True:
        cipher = ''
        encrypt_decrypt = ''
        pad_option = ''
        block_option = ''
        keyword = ''
        message = ''
        output = ''
        draw_screen()
        ciphers_available()
        cipher = input("Which cipher would you like to use today? ")
        while cipher[0] not in 'TKP':
            if cipher[0].upper() == 'T':
                cipher = 'Transposition'
            elif cipher[0].upper() == 'K':
                cipher = 'Keyword'
            elif cipher[0].upper() == 'P':
                cipher = 'Polybius'
            else:
                cipher = ''
                draw_screen()
                ciphers_available()
                cipher = input("\nThat is not one of the available ciphers. \nWhich cipher would you like to use? ")
        draw_screen()
        encrypt_decrypt = input("\nWould you like to encrypt or decrypt your message? ")
        while encrypt_decrypt[0] not in 'ED':
            if encrypt_decrypt[0].upper() == 'E':
                encrypt_decrypt = 'Encrypt'
            elif encrypt_decrypt[0].upper() == 'D':
                encrypt_decrypt = 'Decrypt'
            else:
                encrypt_decrypt = ''
                draw_screen()
                encrypt_decrypt = input("\nSorry, I didn't get that. \nWould you like to encrypt or decrypt your message? ")
        draw_screen()
        pad_option = input("\nWould you like to use a one time pad? \nIf yes, enter one now or press 'Enter' to continue. \nOnly letters and numbers will be used for the pad: ")
        draw_screen()
        if cipher == 'Keyword' and encrypt_decrypt == 'Encrypt':
            block_option = input("\nWould you like your encrypted message formatted into blocks of five characters? Y/N: ")
            while block_option[0] not in 'YN':
                block_option = input("\nSorry, I didn't get that. \nWould you like your encrypted message formatted into blocks of five characters? Y/N: ")
        draw_screen()
        if cipher == 'Keyword':
            keyword = input("\nEnter the keyword you would like to use: ")
        draw_screen()
        message = input("\nWhat message would you like to {}? ".format(encrypt_decrypt.lower()))
        draw_screen()
        if cipher == 'Transposition':
            new_instance = Transposition()
            if encrypt_decrypt == 'Encrypt':
                output = new_instance.encrypt(message)
            elif encrypt_decrypt == 'Decrypt':
                output = new_instance.decrypt(message)
        if cipher == 'Keyword':
            pass
        if cipher == 'Polybius':
            pass
        draw_screen()
        print("Here is your {}ed message: \n".format(encrypt_decrypt.lower()))
        print(output)
        continue_quit = input("Would you like to use another cipher? Enter 'Y' to continue or 'Q' to quit: ")
        if continue_quit.upper() == 'Y':
            clear_screen()
            continue
        elif continue_quit.upper() == 'Q':
            break

            hwyio aeohr u5134
