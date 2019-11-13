# ----------------------------------------------------------------------------
# Name:         language
# Purpose:      CS 21A Assignment # 7
#
# Author:       Andrew Tran
# Date:         06/01/2019
# ----------------------------------------------------------------------------
"""
Program that implements an infinite random sentence generator function

The generator function will generate nonsensical sentences of a given length.
The sentences will be loosely modeled after some specified text file.
"""
import random
import string


def learn(filename):
    """
    Open the file specified, read it, and learn the words used in it

    :param filename: name of the file (string)
    :return: words mapped to a list of words that follow it (dictionary)
    """
    words = {}  # initialize empty dictionary of words
    previous = None

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.lower()  # ignore capitalization
                for current in line.split():
                    # remove leading and trailing punctuation
                    current = current.strip(string.punctuation)

                    if previous and current:  # cannot be empty strings
                        if previous in words:
                            # append if key is already in dictionary
                            words[previous].append(current)
                        else:
                            # create a new entry if key is not in dictionary
                            words[previous] = [current]
                        previous = current

                    # special case for first word
                    if previous is None and current:  # cannot be empty string
                        previous = current
    except FileNotFoundError as error:
        print(f'Sorry, {filename} not found: {error}')
    else:
        if previous not in words:
            words[previous] = []  # append the empty list for the last word
        return words


def sentence_generator(filename, length=8):
    """
    Generate random sentences based on a dictionary of words

    :param filename: name of the file (string)
    :param length: number of words in the generated sentence (int; default = 8)
    :return: generator object (generator)
    """
    random.seed(100)  # set the seed for the random generator - do not remove

    words = learn(filename)  # get dictionary of words from text file
    all_keys = list(words)  # convert dictionary keys to list
    new_word = random.choice(all_keys)  # get a random dictionary key
    result = [new_word]  # initialize result as the random key
    current = 1  # initialize current as the accumulator

    while True:
        if words[new_word]:
            new_word = random.choice(words[new_word])  # get a random value
        else:
            new_word = random.choice(all_keys)  # get a random dictionary key

        result.append(new_word)  # store word in list
        current += 1  # increment accumulator

        if current == length:
            current = 1  # reset accumulator
            yield ' '.join(result)  # yield all words as a single sentence
            new_word = random.choice(all_keys)  # get a random dictionary key
            result = [new_word]  # reinitialize result as the random key
