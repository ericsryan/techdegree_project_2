"""Encrypt or decrypt a message using the Transposition cipher.

The Transposition cipher works by reordering the characters in a message by
distributing each letter to one of three 'rails.' The characters on each rail
are then recombined to encrypt the message. The message can only be decrypted
if the person receiving the message knows the method of encryption.
"""

import string

from ciphers import Cipher


class Transposition(Cipher):
    """Encrypt or decrypt a message using the Transposition cipher."""

    def __init__(self, message):
        """Set the message as an attribute within the class."""
        self.message = message

    def encrypt(self):
        """Encrypt the message using the Transposition cipher."""
        text = self.message.upper()
        letter_list_1 = []
        letter_list_2 = []
        letter_list_3 = []
        phrase = []
        # Remove spaces and punctuation from the message
        for letter in text:
            if letter in string.ascii_uppercase + string.digits:
                phrase.append(letter)
        text = ''.join(phrase)
        # Distribute the message to three "rails"
        counter = 0
        for i in range(int(len(text) / 4)):
            letter_list_1.append(text[counter])
            counter += 4
        if len(text) % 4 >= 1:
            letter_list_1.append(text[counter])
        counter = 1
        for i in range(int(len(text) / 2)):
            letter_list_2.append(text[counter])
            counter += 2
        counter = 2
        for i in range(int(len(text) / 4)):
            letter_list_3.append(text[counter])
            counter += 4
        if len(text) % 4 == 3:
            letter_list_3.append(text[counter])
        # Combine the rails into a single phrase
        letter_list_1.extend(letter_list_2)
        letter_list_1.extend(letter_list_3)
        # Add junk characters to create even blocks of 5 characters
        if len(letter_list_1) % 5 == 1:
            letter_list_1.extend(['-', '-', '-', '-'])
        elif len(letter_list_1) % 5 == 2:
            letter_list_1.extend(['-', '-', '-'])
        elif len(letter_list_1) % 5 == 3:
            letter_list_1.extend(['-', '-'])
        elif len(letter_list_1) % 5 == 4:
            letter_list_1.extend(['-'])
        # Insert spaces to make the phrase more readable
        counter = 5
        for i in range(int(len(letter_list_1) / 5) - 1):
            letter_list_1.insert(counter, ' ')
            counter += 6
        return ''.join(letter_list_1)

    def decrypt(self):
        """Decrypt the message using the Transposition cipher."""
        text = self.message.upper()
        output = []
        letter_list = []
        letter_list_1 = []
        letter_list_2 = []
        letter_list_3 = []
        for character in text:
            if character in string.ascii_uppercase + string.digits:
                letter_list.append(character)
        if len(letter_list) % 4 == 0:
            letter_list_1 = letter_list[:int(len(letter_list) / 4)]
            letter_list_2 = (letter_list[int(len(letter_list) /
                             4):-int(len(letter_list) / 4)])
            letter_list_3 = letter_list[-int(len(letter_list) / 4):]
        elif len(letter_list) % 4 == 1:
            letter_list_1 = letter_list[:int(len(letter_list) / 4) + 1]
            letter_list_2 = (letter_list[int(len(letter_list) /
                             4 + 1):-int(len(letter_list) / 4)])
            letter_list_3 = letter_list[-int(len(letter_list) / 4):]
        elif len(letter_list) % 4 == 2:
            letter_list_1 = letter_list[:int((len(letter_list) / 4) + 1)]
            letter_list_2 = (letter_list[int((len(letter_list) /
                             4) + 1):-int(len(letter_list) / 4)])
            letter_list_3 = letter_list[-int(len(letter_list) / 4):]
        elif len(letter_list) % 4 == 3:
            letter_list_1 = letter_list[:int(len(letter_list) / 4) + 1]
            letter_list_2 = (letter_list[int(len(letter_list) /
                             4) + 1:-int((len(letter_list) / 4) + 1)])
            letter_list_3 = letter_list[-int((len(letter_list) / 4) + 1):]
        counter_1 = 0
        counter_2 = 0
        for i in range(int(len(letter_list) / 4)):
            output.append(letter_list_1[counter_1])
            output.append(letter_list_2[counter_2])
            counter_2 += 1
            output.append(letter_list_3[counter_1])
            counter_1 += 1
            output.append(letter_list_2[counter_2])
            counter_2 += 1
        if len(letter_list) % 4 >= 1:
            output.append(letter_list_1[counter_1])
        if len(letter_list) % 4 >= 2:
            output.append(letter_list_2[counter_2])
        if len(letter_list) % 4 == 3:
            output.append(letter_list_3[counter_1])
        return ''.join(output)
