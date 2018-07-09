
    """def option_select():
        print('    Ciphers available:')
        print(
        """
        -Transposition
        -Keyword
        -Polybius

            """)
        cipher = input("    Which cipher would you like to use? ")
        if cipher[0].upper() == 'T':
            selected_cipher = 'Transposition'
        if cipher[0].upper() == 'K':
            selected_cipher = 'Keyword'
        if cipher[0].upper() == 'P':
            selected_cipher = 'Polybius'
        clear_screen()
        draw_screen()
        print("""    Cipher: {}

        """.format(selected_cipher))
        encrypt_decrypt = input("    Would you like to encrypt or decrypt your message? ")
        if encrypt_decrypt[0].upper() == 'E':
            encrypt_decrypt = 'Encrypt'
        elif encrypt_decrypt[0].upper() == 'D':
            encrypt_decrypt = 'Decrypt'
        clear_screen()
        draw_screen()
        if selected_cipher == 'Keyword':
            print("""    Cipher: {}
    Process: {}

            """.format(selected_cipher, encrypt_decrypt))
            keyword = input("    Please enter the keyword you would like\n    to use to {} the message: ".format(encrypt_decrypt.lower()))
        else:
            print("""    Cipher: {}
    Process: {}

            """.format(selected_cipher, encrypt_decrypt))
        clear_screen()
        draw_screen()
        if selected_cipher == "Keyword":
            print("""    Cipher: {}
    Process: {}
    Keyword: {}

        """.format(selected_cipher, encrypt_decrypt, keyword))
        else:
            print("""    Cipher: {}
    Process: {}

            """.format(selected_cipher, encrypt_decrypt))
        message = input("    What is the message that you would like to {}? ".format(encrypt_decrypt.lower()))
        clear_screen()
        draw_screen()
        if selected_cipher == "Keyword":
            print("""    Cipher: {}
    Process: {}
    Keyword: {}
    Original message: {}

        """.format(selected_cipher, encrypt_decrypt, keyword, message))
        else:
            print("""    Cipher: {}
    Process: {}
    Original message: {}

            """.format(selected_cipher, encrypt_decrypt, message))
        clear_screen()

    def results():
        output = message
        draw_screen()
        if selected_cipher == "Keyword":
            print("""    Cipher: {}
    Process: {}
    Keyword: {}
    Original message: {}

    {}ed message: {}

        """.format(selected_cipher, encrypt_decrypt, keyword, message, encrypt_decrypt, output))
        else:
            print("""    Cipher: {}
    Process: {}
    Original message: {}

            """.format(selected_cipher, encrypt_decrypt, message))



clear_screen()
draw_screen()
option_select()
results()
"""
