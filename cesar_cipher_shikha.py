# Done by: Shikha Pandey 

"""
This program encrypts and decrypts text using the Caesar Cipher.
"""

import os

def welcome():
    """
    Prints welcome message for the user
    """
    print("\n\nWelcome to the Caesar Cipher!\n")
    print("This program encrypts and decrypts text with the Caesar Cipher\n\n")

def enter_message():
    """
    Prompts the user to choose a mode: encrypt (e) or decrypt (d) and stores the choice 
    in the variable 'mode'. Prompts the user to choose if they want to read from a file 
    or write their text in the console and stores it in variable 'process'.
    Returns the variables 'mode' and 'process' as string datatypes.
    """
    while True:
        mode = input("Would you like to encrypt(e) or decrypt(d)? :")
        mode = mode.lower()
        if mode not in ('e', 'd'):
            print("Invalid mode. Please type 'e' to encrypt and 'd' to decrypt")
        else:
            break

    while True:
        message = input("Enter your message:")
        message = message.upper()
        if message == "":
            print("Please enter a message.")
        else:
            break
    return message, mode

def encrypt(message, shift):
    """
    Encrypts user message and stores it in variable 'encrypted_message'
    This function has two parameters: message, shift.
    Returns the variable 'encrypted_message' as a string datatype.
    """
    message = message.upper()
    encrypted_message = ""
    for letter in message:
        if letter.isalpha():
            s1 = int(ord(letter) - ord('A'))
            s2 = int((s1 + shift) % 26)
            s3 = int((s2 + ord('A')))
            s4 = chr(s3)
            encrypted_message += s4
        else:
            encrypted_message += letter
    return encrypted_message

def decrypt(message, shift):
    """
    Decrypts user message and stores it in variable 'decrypted_message'
    This function has two parameters: message, shift.
    Returns the variable 'decrypted_message' as a string datatype.
    """
    message = message.upper()
    decrypted_message = ""
    for letter in message:
        if letter.isalpha():
            s1 = int(ord(letter) - ord('A'))
            s2 = int((s1 - shift) % 26)
            s3 = int((s2 + ord('A')))
            s4 = chr(s3)
            decrypted_message += s4
        else:
            decrypted_message += letter
    return decrypted_message

def process_file(file_name, mode):
    """
    Process the file based on mode and shift for encryption or decryption
    """
    while True:
        try:
            shift = int(input("Enter your shift number:"))
            if shift > 100 or shift < -100:
                print("Shift number must be between -100 and 100")
                continue
            break
        except ValueError:
            print("Enter a valid number")
    if not is_file(file_name):
        print("The file was not found")
        return[]
    processed_messages = []
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            message = line.strip()
            if mode == 'e':
                processed_messages.append(encrypt(message, shift))
            if mode == 'd':
                processed_messages.append(decrypt(message, shift))
    return processed_messages

def is_file(file_name):
    """
    Checks if the file exists.
    """
    return os.path.isfile(file_name)

def write_messages(processed_messages):
    """
    Writes processed messages to a file.
    """
    with open('results.txt', 'w', encoding="utf-8") as file:
        for message in processed_messages:
            file.write(message + '\n')
    print("\nThe result is also stored at result.txt\n")

def message_or_file():
    """
    Asks the user whether they want to read from a file or the console.
    """
    while True:
        file_or_console = input(
            "Would you like to read from a file (f) or the console (c)? :"
        )
        file_or_console = file_or_console.lower()
        if file_or_console not in ('f', 'c'):
            print(
            "Your input is not valid. Please type 'f' to read from a file "
            "and 'c' to read from the console."
            )
            continue
        break
    if file_or_console == "f":
        while True:
            mode = input("Would you like to encrypt(e) or decrypt(d)? :")
            mode = mode.lower()
            if mode in ("e", "d"):
                break
            print(
                "Your input is not valid. Please type 'e' to encrypt and 'd' to decrypt."
            )
        while True:
            file_name = input("Enter your Filename with extension:")
            if is_file(file_name):
                break
            print("Please enter a correct file name.")

    else:
        mode = None
        file_name = None

    return mode, file_or_console, file_name

def main():
    """
    Main function to handle the encryption and decryption process.
    """
    welcome()
    while True:
        mode, file_or_console, file_name = message_or_file()
        if file_or_console == 'c':
            while True:
                try:
                    shift = int(input("Enter your shift number:"))
                    if shift>100 or shift<-100:
                        print("Shift number must be between -100 and 100")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number")
            message, mode = enter_message()
            if mode == 'e':
                print("\nEncrypted message:", encrypt(message, shift))
            else:
                print("\nDecrypted message:", decrypt(message, shift))
        elif file_or_console == 'f':
            processed_messages = process_file(file_name, mode)
            print(f"\nProcessed messages (from file):\n{processed_messages}")
            write_messages(processed_messages)

        continue_choice = ""
        while continue_choice not in ['y', 'n']:
            continue_choice = input(
                "\nWould you like to encrypt or decrypt another message? (y/n): "
            )
            if continue_choice.lower() == 'n':
                print("The program has ended")
                break
            if continue_choice.lower() == 'y':
                print("Continuing program...")
                print("-"*30,"\n")
                break
            print(
            "Please enter y if you would like to encrypt or decrypt another message"
            " and n if you would like to exit the program."
            )
        if continue_choice.lower() == 'n':
            break

main()
