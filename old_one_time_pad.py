import string
from ciphers import Cipher

class OneTimePad(Cipher):


    def __init__(self, pad, message):
        self.message = message.upper()
        # Generates dictionaries that match characters to numerical values
        self.character_dict = {character: num for num, character in \
        zip(range(1, 37), string.ascii_uppercase + string.digits)}
        self.num_dict = {num: character for character, num in \
        zip(string.ascii_uppercase + string.digits, range(1, 37))}
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
        # Applies pad to letters and numerals in the message
        encrypted_char_list = []
        encrypted_message = ''
        pad_index = 0
        for character in self.message:
            if character not in string.ascii_uppercase + string.digits:
                encrypted_char_list.append(character)
            else:
                (encrypted_char_list.append(str(self.character_dict[character]
                + self.character_dict[self.full_pad[pad_index]])))
                pad_index += 1
        # Write encoded characters to the message string
        for character in encrypted_char_list:
            try:
                if int(character) in range(0, 74):
                    mod_char = int(character) % 36
                    encrypted_message += self.num_dict[mod_char]
            except:
                encrypted_message += character
        return encrypted_message

    def decrypt(self):
        # Applies pad to letters and numerals in the message
        decrypted_char_list = []
        decrypted_message = ''
        pad_index = 0
        for character in self.message:
            if character not in string.ascii_uppercase + string.digits:
                decrypted_char_list.append(character)
            else:
                (decrypted_char_list.append(str(self.character_dict[character]
                - self.character_dict[self.full_pad[pad_index]])))
                pad_index += 1
        # Write decoded characters to the message string
        for character in decrypted_char_list:
            try:
                mod_char = (int(character) + 36) % 36
                decrypted_message += self.num_dict[mod_char]
            except:
                decrypted_message += character
        return decrypted_message
