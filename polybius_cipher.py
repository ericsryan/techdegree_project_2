import string
from ciphers import Cipher

class Polybius(Cipher):
    def __init__(self):
        self.table = [str(x) + str(y) for x in range(1, 7) for y in range(1, 7)]
        self.alpha_nums = string.ascii_uppercase + string.digits
        self.polybius_encode = dict(zip(self.alpha_nums, self.table))
        self.polybius_decode = dict(zip(self.table, self.alpha_nums))

    def encrypt(self, text):
        output = []
        text = text.upper()
        for character in text:
            try:
                output.append(self.polybius_encode[character])
            except:
                if character == ' ':
                    output.append(character)
                else:
                    continue
        return ''.join(output)

    def decrypt(self, text):
        output = ''
        text = text.split()
        sorted_code = []
        for word in text:
            counter = 0
            sorted_code.append(' ')
            while counter < len(word):
                sorted_code.append(word[counter:counter + 2])
                counter += 2
        sorted_code.remove(' ')
        for character in sorted_code:
            try:
                output += self.polybius_decode[character]
            except:
                if character == ' ':
                    output += character
                else:
                    continue
        return output
