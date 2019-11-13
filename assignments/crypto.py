# ----------------------------------------------------------------------------
# Name:         crypto
# Purpose:      CS 21A Assignment # 3
#
# Author:       Andrew Tran
# Date:         04/28/2019
# ----------------------------------------------------------------------------
"""
Program that encrypts or decrypts a given text into/from a secret language

Prompt user for choice between encryption into the secret language
or decryption from the secret language.
Print out correct translated message depending on the option chosen.
"""


def starts_with_vowel(word):
    """
    Check if inputted word starts with a vowel

    Parameters: word (string)
    Return: True if the word starts with a vowel and False otherwise (boolean)
    """
    # if the first letter of the word is a vowel, return True
    # else, return False
    return word[0] in ['a', 'e', 'i', 'o', 'u']


def encrypt(word):
    """
    Encrypt a single word into the secret language

    Parameters: word (string)
    Return: translated word according to the encryption rules (string)
    """
    # call starts_with_vowel to decide which pattern to follow
    if starts_with_vowel(word):
        result = word + 'bin'
    else:
        result = word[1:] + word[0] + 'ar'

    # return a single word (encrypted)
    return result


def decrypt(word):
    """
    Decrypt a single word from the secret language

    Parameters: word (string)
    Return: translated word according to the decryption rules (string),
    otherwise return None
    """
    # check if word follows a specific format
    if starts_with_vowel(word) and word[-3:] == 'bin':
        result = word[:-3]
    elif not starts_with_vowel(word[-3:]) and word[-2:] == 'ar':
        result = word[-3] + word[:-3]
    else:
        # if the word is not a valid word in the secret language, return None
        return

    # return a single word (decrypted) if possible
    return result


def translate(text, mode):
    """
    Translate (encrypt or decrypt) the entire message

    Parameters: text, mode (strings)
    Return: combined string of individual translated words (string)
    """
    # split the text into a list of words
    words = text.split()
    """
    if mode.upper() == 'E':  # encrypt each word in the list
        for i in range(len(words)):
            words[i] = encrypt(words[i])
    else:
        for i in range(len(words)):  # decrypt each word in the list
            words[i] = decrypt(words[i])
        if None in words:
            return
    """
    new_words = []
    for word in words:
        if mode.upper() == 'E':
            new_word = encrypt(word)
        else:
            new_word = decrypt(word)
            if new_word is None:
                return
        new_words.append(new_word)

    # reverse the list
    new_words.reverse()

    # join the list of reversed translated words into a single string
    result = ' '.join(new_words)
    return result


def choose_mode():
    """
    Prompt user for input repeatedly until they enter 'E', 'e', 'D', or 'd'

    Parameters: None
    Return: letter representing user's choice (string)
    """
    # infinite loop until user enters 'E', 'e', 'D' or 'd'
    while True:
        choice = input('Please type E to encrypt or D to decrypt a message: ')
        if choice.upper() != 'E' and choice.upper() != 'D':
            print('Invalid choice.')
        else:
            return choice


def main():
    # get the user choice: 'E' or 'D'
    mode = choose_mode()

    # prompt user for the message to be translated
    message = input('Please enter your message: ')

    # translate message by calling translate()
    result = translate(message, mode)

    # print result or 'Invalid message.' if applicable
    if result is None:
        print('Invalid message.')
    else:
        print('The secret message is:', result)


if __name__ == '__main__':
    main()
