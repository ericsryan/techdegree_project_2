"""Encrypt and decrypt messages using the Polybius cipherself.

Each letter in the alphabet is represented on a grid with numbered rows and
columns. The message is encrypted by replacing each letter with the two digit
coordinates from the grid.
"""

import string

from ciphers import Cipher


class Polybius(Cipher):
    """Encrypt or decrypt a message using the Polybius cipher."""

    def __init__(self, message):
        """Generate a 6x6 grid populated by the alphabet and digits."""
        self.message = message.upper()
        self.table = ([str(x) + str(y) for x in range(1, 7)
                      for y in range(1, 7)])
        self.alpha_nums = string.ascii_uppercase + string.digits
        self.polybius_encode = dict(zip(self.alpha_nums, self.table))
        self.polybius_decode = dict(zip(self.table, self.alpha_nums))

    def encrypt(self):
        """Encrypt the message using the Polybius cipher."""
        output = []
        for character in self.message:
            if character in string.ascii_uppercase + string.digits:
                output.append(self.polybius_encode[character])
            else:
                output.append(character)
        return ''.join(output)

    def decrypt(self):
        """Decrypt the message using the Polybius cipher."""
        output = ''
        input = []
        characters = []
        character_list = []
        counter = 0
        for character in self.message:
            characters.append(character)
        while counter < len(characters):
            if characters[counter] in string.digits:
                input.append(characters[counter:counter + 2])
                counter += 2
            else:
                input.append(characters[counter])
                counter += 1
        for character in input:
            if len(character) == 2:
                character_list.append(''.join(character))
            else:
                character_list.append(character)
        for character in character_list:
            if character in self.table:
                output += self.polybius_decode[character]
            else:
                output += character
        return output
