"""Encryption and decryption using a one-time padself.

In cryptography, the one-time pad is an encryption technique that cannot be
cracked, but requires the use of a one-time pre-shared key the same size as, or
longer than, the message being sent. In this technique, a plaintext is paired
with a random secret key (also referred to as a one-time pad). Then, each bit
or character of the plaintext is encrypted by combining it with the
corresponding bit or character from the pad using modular addition. If the key
is truly random, is at least as long as the plaintext, is never reused in whole
or in part, and is kept completely secret, then the resulting ciphertext will
be impossible to decrypt or break.
"""

import string

from ciphers import Cipher


class OneTimePad(Cipher):
    """Encrypt and decrypt the message using a one-time pad."""

    def __init__(self, pad, message):
        """Generate dictionaries used to encrypt and decrypt the message."""
        self.message = message.upper()
        # Generates dictionaries that match characters to numerical values
        self.character_dict = ({character: num for num, character
                               in zip(range(0, 26), string.ascii_uppercase)})
        self.num_dict = ({num: character for character, num in
                         zip(string.ascii_uppercase, range(0, 26))})
        # Sanitizes pad input and multiplies it to match message length
        new_pad = pad.upper()
        self.full_pad = ''
        for character in new_pad:
            if character in string.ascii_uppercase + string.digits:
                self.full_pad += character
        if len(self.full_pad) < len(self.message):
            multiply_by = int((len(self.message) / len(self.full_pad)) + 1)
            self.full_pad = self.full_pad * multiply_by

    def encrypt(self):
        """Encrypt the message using the one-time pad."""
        output = []
        pad_index = 0
        for character in self.message:
            if character in string.ascii_uppercase:
                output.append(self.num_dict[((self.character_dict[character]
                              + self.character_dict[self.full_pad[pad_index]])
                              % 26)])
                pad_index += 1
            else:
                output.append(character)
        return ''.join(output)

    def decrypt(self):
        """Decrypt the message using the one-time pad."""
        output = []
        pad_index = 0
        for character in self.message:
            if character in string.ascii_uppercase:
                output.append(self.num_dict[(((self.character_dict[character]
                              - self.character_dict[self.full_pad[pad_index]])
                              + 26) % 26)])
                pad_index += 1
            else:
                output.append(character)
        return ''.join(output)
