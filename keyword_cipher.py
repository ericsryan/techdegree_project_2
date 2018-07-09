import string

from ciphers import Cipher



class Keyword(Cipher):
    def __init__(self, key):
        keyword = key.upper()
        plaintext = string.ascii_uppercase
        encrypted = []
        for character in keyword:
            if character not in encrypted and character in string.ascii_uppercase:
                encrypted.append(character)
        for character in string.ascii_uppercase:
            if character not in encrypted:
                encrypted.append(character)
        self.cipher_alphabet = dict(zip(plaintext, encrypted))
        self.decipher_alphabet = dict(zip(encrypted, plaintext))

    def encrypt(self, text):
        output = []
        text = text.upper()
        for character in text:
            try:
                output.append(self.cipher_alphabet[character])
            except:
                output.append(character)
        return ''.join(output)


    def decrypt(self, text):
        output = []
        text = text.upper()
        for character in text:
            try:
                output.append(self.decipher_alphabet[character])
            except:
                output.append(character)
        return ''.join(output)
