import string
from ciphers import Cipher

class OneTimePad(Cipher):


    def __init__(self):
        self.character_dict = {character: num for num, character in \
        zip(range(0,36), string.ascii_uppercase + string.digits)}
        self.num_dict = {num: character for character, num in \
        zip(string.ascii_uppercase + string.digits, range(0, 36))}

    def encrypt(self, pad, message):
        message = message.upper()
        full_pad = pad.upper()
        encrypted_char_list = []
        encrypted_message = ''
        pad_index = 0
        if len(full_pad) < len(message):
            multiply_by = len(message) / len(full_pad)
            full_pad = full_pad * (int(multiply_by) + 1)
        for character in message:
            if character not in string.ascii_uppercase + string.digits:
                encrypted_char_list.append(character)
            else:
                (encrypted_char_list.append(str(self.character_dict[character]
                + self.character_dict[full_pad[pad_index]])))
                pad_index += 1
        for character in encrypted_char_list:
            try:
                if int(character) in range(0, 72):
                    mod_char = int(character) % 36
                    encrypted_message += self.num_dict[mod_char]
            except:
                encrypted_message += character
        return encrypted_message

    def decrypt(self, pad, message):
        message = message.upper()
        full_pad = pad.upper()
        decrypted_char_list = []
        decrypted_message = ''
        pad_index = 0
        if len(full_pad) < len(message):
            multiply_by = len(message) / len(full_pad)
            full_pad = full_pad * (int(multiply_by) + 1)
        for character in message:
            if character not in string.ascii_uppercase + string.digits:
                decrypted_char_list.append(character)
            else:
                (decrypted_char_list.append(str(self.character_dict[character]
                - self.character_dict[full_pad[pad_index]])))
                pad_index += 1
        for character in decrypted_char_list:
            try:
                if int(character) in range(0, 36):
                    mod_char = int(character) % 36
                    decrypted_message += self.num_dict[mod_char]
                elif int(character) < 0:
                    mod_char = int(character) + 36
                    decrypted_message += self.num_dict[mod_char]
            except:
                decrypted_message += character
        return decrypted_message
