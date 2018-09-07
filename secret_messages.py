"""Encrypt or decrypt your message using your choice of cipher.

This program can be used to either encrypt or decrypt a message. The message
can be further encrypted using a one-time pad.
"""

import os
import string

from keyword_cipher import Keyword
from one_time_pad import OneTimePad
from polybius_cipher import Polybius
from transposition_cipher import Transposition


def clear_screen():
    """Clear the screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_screen():
    """Display the user's selections and message."""
    clear_screen()
    print('_' * 60 + '\n\n' + ' ' * 15 + 'Welcome to the Cryptographer!\n' +
          '_' * 60 + '\n')
    if cipher:
        print("Cipher:", cipher)
    if encrypt_decrypt:
        print("Method:", encrypt_decrypt)
    if pad_option:
        print("Pad:", pad_option)
    if block_option.upper() == 'Y':
        print("Message will be formatted")
    if keyword:
        print("Keyword:", keyword)
    if message:
        print("Original message:", message)
    if cipher:
        print('')
    if output:
        print("Here is your {}ed message: \n"
              .format(encrypt_decrypt.lower()) + output)


def ciphers_available():
    """Display the ciphers that are available for use."""
    print('    Ciphers available:')
    print("\n    -Keyword"
          "\n    -Polybius"
          "\n    -Transposition\n"
          )


def five_keyword(message):
    """Reformat the characters of a message into blocks of five."""
    message = message.upper()
    block_message = []
    counter = 0
    for character in message:
        if character in string.ascii_uppercase + string.digits:
            block_message.append(character)
            counter += 1
            if counter == 5:
                block_message.append(' ')
                counter = 0
    block_message.append('-' * (5 - (len(block_message) % 6)))
    return ''.join(block_message)


def five_polybius(message):
    """Reformat the characters of a message into blocks of five."""
    block_message = []
    counter = 0
    for character in message:
        if character in string.digits:
            block_message.append(character)
            counter += 1
            if counter == 10:
                block_message.append(' ')
                counter = 0
    block_message.append('-' * (10 - (len(block_message) % 11)))
    return ''.join(block_message)


def pad_encrypt(message):
    """Instantiate an instance in order to encrypt a message."""
    new_instance = OneTimePad(pad_option, message)
    return new_instance.encrypt()


def pad_decrypt(message):
    """Instantiate an instance in order to decrypt a message."""
    new_instance = OneTimePad(pad_option, message)
    return new_instance.decrypt()


if __name__ == '__main__':

    # Splash screen
    clear_screen()
    print("Thank you for using this program! You will have\nthe opportunity"
          " to select a cipher that can be\nused to encrypt or decrypt your"
          " message. Your\nmessage can be further encrypted"
          " by using a\none-time pad of your choosing.\n\nEnjoy the program!"
          )
    input("\nPress 'Enter to continue.'")

    while True:
        cipher = ''
        encrypt_decrypt = ''
        pad_option = ''
        block_option = ''
        keyword = ''
        message = ''
        output = ''
        continue_quit = ''
        # Select an available cipher.
        draw_screen()
        ciphers_available()
        while cipher == '':
            cipher = input("What cipher would you like to use? ")
            if cipher[0:3].upper() == 'KEY':
                cipher = 'Keyword'
            elif cipher[0:4].upper() == 'POLY':
                cipher = 'Polybius'
            elif cipher[0:4].upper() == 'TRAN':
                cipher = 'Transposition'
            else:
                cipher = ''
                draw_screen()
                ciphers_available()
                print("I'm sorry, that is not an available cipher. ")
        # Choose whether to encrypt or decrypt.
        draw_screen()
        while encrypt_decrypt == '':
            encrypt_decrypt = input("Would you like to encrypt"
                                    " or decrypt your message? "
                                    )
            if encrypt_decrypt[0:2].upper() == 'EN':
                encrypt_decrypt = 'Encrypt'
            elif encrypt_decrypt[0:2].upper() == 'DE':
                encrypt_decrypt = 'Decrypt'
            else:
                encrypt_decrypt = ''
                draw_screen()
                print("I'm sorry, I didn't get that. ")
        # Choose pad option
        draw_screen()
        while pad_option == '':
            pad_option = input("Would you like to use a one-time pad?"
                               " If you do, enter one now."
                               "\nOtherwise, enter 'N' for no. "
                               )
            if pad_option.upper() == 'N':
                pad_option = "Not in use."
            if pad_option == '':
                draw_screen()
                print("You didn't enter anything.")
            if pad_option != 'Not in use.':
                for character in pad_option:
                    if (character.upper() not in
                            string.ascii_uppercase + string.digits):
                        pad_option = ''
                        draw_screen()
                        print("Make sure there are only"
                              " letters and numbers in the pad."
                              )
        # Choose whether to format message into blocks of five.
        draw_screen()
        if ((cipher == 'Keyword' or cipher == 'Polybius') and
                encrypt_decrypt == 'Encrypt'):
            while block_option == '':
                block_option = input("Would you like to format your message"
                                     " into blocks of five? Y/N: "
                                     )
                if block_option.upper() in 'YN':
                    continue
                else:
                    block_option = ''
                    draw_screen()
                    print("I'm sorry, I didn't get that.")
        # Enter keyword
        draw_screen()
        if cipher == 'Keyword':
            while keyword == '':
                keyword = input("What keyword would you like to use to"
                                " {}".format(encrypt_decrypt.lower()) +
                                " your message? "
                                )
                for character in keyword:
                    if character.upper() not in string.ascii_uppercase:
                        keyword = ''
                        draw_screen()
                        print("Only letters can be used in the keyword.")
                        break
        # Enter the message.
        draw_screen()
        while message == '':
            message = input("Enter the message that you would like"
                            " to {}: ".format(encrypt_decrypt.lower())
                            )
            if message == '':
                print("I'm sorry, I didn't get that. ")
        # Implement cipher selection.
        if cipher == 'Keyword':
            if encrypt_decrypt == 'Encrypt':
                new_instance = Keyword(keyword, message)
                output = new_instance.encrypt()
                if pad_option != 'Not in use.':
                    output = pad_encrypt(output)
                if block_option.upper() == 'Y':
                    output = five_keyword(output)
            else:
                if pad_option != 'Not in use.':
                    output = pad_decrypt(message)
                    new_instance = Keyword(keyword, output)
                else:
                    new_instance = Keyword(keyword, message)
                output = new_instance.decrypt()
        if cipher == 'Polybius':
            if encrypt_decrypt == 'Encrypt':
                if pad_option != 'Not in use.':
                    output = pad_encrypt(message)
                    new_instance = Polybius(output)
                else:
                    new_instance = Polybius(message)
                output = new_instance.encrypt()
                if block_option.upper() == 'Y':
                    output = five_polybius(output)
            else:
                new_instance = Polybius(message)
                output = new_instance.decrypt()
                if pad_option != 'Not in use.':
                    output = pad_decrypt(output)
        if cipher == 'Transposition':
            if encrypt_decrypt == 'Encrypt':
                new_instance = Transposition(message)
                output = new_instance.encrypt()
                if pad_option != 'Not in use.':
                    output = pad_encrypt(output)
            else:
                if pad_option != 'Not in use.':
                    output = pad_decrypt(message)
                    new_instance = Transposition(output)
                else:
                    new_instance = Transposition(message)
                output = new_instance.decrypt()
        # Continue/Quit
        draw_screen()
        print('')
        while continue_quit == '':
            continue_quit = input("Would you like to use"
                                  " another cipher? Y/N: ")
            if continue_quit.upper() in 'YN':
                continue
            else:
                continue_quit = ''
                draw_screen()
                print("I'm sorry, I didn't get that.")
        if continue_quit.upper() == 'N':
            break
