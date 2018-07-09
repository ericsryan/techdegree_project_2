import string

class Transposition:
    def encrypt(self, text):
        text = text.upper()
        letter_list_1 = []
        letter_list_2 = []
        letter_list_3 = []
        phrase = []
        # Remove spaces and punctuation from the message
        for letter in text:
            if letter in string.ascii_uppercase:
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
            letter_list_1.extend(['5', '1', '3', '4'])
        elif len(letter_list_1) % 5 == 2:
            letter_list_1.extend(['8', '7', '3'])
        elif len(letter_list_1) % 5 == 3:
            letter_list_1.extend(['4', '6'])
        elif len(letter_list_1) % 5 == 4:
            letter_list_1.extend(['8'])
        # Insert spaces to make the phrase more readable
        counter = 5
        for i in range(int(len(letter_list_1) / 5) - 1):
            letter_list_1.insert(counter, ' ')
            counter += 6
        return ''.join(letter_list_1)

    def decrypt(self, text):
        text = text.upper()
        output = []
        letter_list = []
        letter_list_1 = []
        letter_list_2 = []
        letter_list_3 = []
        for character in text:
            if character in string.ascii_uppercase:
                letter_list.append(character)
        if len(letter_list) % 4 == 0:
            letter_list_1 = letter_list[:int(len(letter_list) / 4)]
            letter_list_2 = letter_list[int(len(letter_list) / 4):-int(len(letter_list) / 4)]
            letter_list_3 = letter_list[-int(len(letter_list) / 4):]
        elif len(letter_list) % 4 == 1:
            letter_list_1 = letter_list[:int(len(letter_list) / 4) + 1]
            letter_list_2 = letter_list[int(len(letter_list) / 4 + 1):-int(len(letter_list) / 4)]
            letter_list_3 = letter_list[-int(len(letter_list) / 4):]
        elif len(letter_list) % 4 == 2:
            letter_list_1 = letter_list[:int((len(letter_list) / 4) + 1)]
            letter_list_2 = letter_list[int((len(letter_list) / 4) + 1):-int(len(letter_list) / 4)]
            letter_list_3 = letter_list[-int(len(letter_list) / 4):]
        elif len(letter_list) % 4 == 3:
            letter_list_1 = letter_list[:int(len(letter_list) / 4) + 1]
            letter_list_2 = letter_list[int(len(letter_list) / 4) + 1:-int((len(letter_list) / 4) + 1)]
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
