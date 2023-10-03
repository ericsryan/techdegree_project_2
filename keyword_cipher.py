"""Encrypt and decrypt messages using the keyword cipher.

A keyword is used as the key, and it determines the letter matchings of the
cipher alphabet to the plain alphabet. Repeats of letters in the word are
removed, then the cipher alphabet is generated with the keyword matching to
A,B,C etc. until the keyword is used up, then the rest of the ciphertext
letters are used in alphabetical order excluding those already used in the key.
"""

import string

from ciphers import Cipher


class Keyword(Cipher):
    """Encrypt and decrypt messages using the keyword cipher."""

    def __init__(self, key, message):
        """Generate an alphabet using a keyword."""
        self.message = message.upper()
        keyword = key.upper()
        plaintext = string.ascii_uppercase
        encrypted = []
        for character in keyword:
            if (character not in encrypted and
                    character in string.ascii_uppercase):
                encrypted.append(character)
        for character in string.ascii_uppercase:
            if character not in encrypted:
                encrypted.append(character)
        self.cipher_alphabet = dict(zip(plaintext, encrypted))
        self.decipher_alphabet = dict(zip(encrypted, plaintext))

    def encrypt(self):
        """Encrypt the message using the keyword alphabet."""
        output = []
        for character in self.message:
            try:
                output.append(self.cipher_alphabet[character])
            except Exception:
                output.append(character)
        return ''.join(output)

    def decrypt(self):
        """Decrypt the message using the keyword alphabet."""
        output = []
        for character in self.message:
            try:
                output.append(self.decipher_alphabet[character])
            except Exception:
                output.append(character)
        return ''.join(output)
