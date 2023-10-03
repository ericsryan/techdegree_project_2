# Secret Messages

This program was developed to implement skills that were learned for Object-Oriented Programing in Python. The program will encrypt or decrypt secret messages. The encryption will make reading and decrypting the messages very difficult but this program is not meant to create secure communications.

## Installation

1. Clone the repository to your local machine.
```bash
git clone https://github/ericsryan/techdegree_project_2.git
```

2. Navigate to the project directory.
```bash
cd techdegree_project_2
```

3. Run the main program file `secret_messages.py` in the terminal or console.
```bash
python3 secret_messages.py
```

## Usage

Users have the option of using three ciphers to encrypt or decrypt their messages. They are the Keyword, Polybius, and Transposition ciphers. Users may select the cipher by typing in the name of the cipher they wish to use. However, it is only necessary to type the first syllable of the cipher to select it. The same is true when selecting whether to encrypt or decrypt a message.

The user then has the option to apply a one-time pad to further secure their message. If the one-time pad is forgotten or lost then the message will be unretrievable. It is the default behavior of the Transposition cipher for the output to be formatted into blocks of five. However, if the user would like the output of the other ciphers to be blocks of five they have the option of doing so as well.

## Credits

Thank you Kenneth Love, Craig Dennis, and the rest of Team Treehouse!