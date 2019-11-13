# ----------------------------------------------------------------------------
# Name:         spam
# Purpose:      CS 21A Assignment # 4
#
# Author:       Andrew Tran
# Date:         05/05/2019
# ----------------------------------------------------------------------------
"""
Program that classifies messages as either SPAM (unwanted) or HAM (wanted)

Prompt user for a message and print the corresponding spam indicator.
Print out the corresponding classification (SPAM or HAM).
"""
import string

# define set of spam words
SPAM_WORDS = {'claim', 'congratulations', 'credit', 'dictator', 'discount',
              'expire', 'free', 'help', 'inheritance', 'lifetime', 'loan',
              'medicine', 'money', 'now', 'offer', 'opportunity', 'plan',
              'prize', 'rich', 'save', 'top', 'urgent', 'widow', 'winner'}

# define constant that reflects allowed percentage of spam words in message
SPAM_THRESHOLD = 0.10


def spam_indicator(text):
    """
    Take in text message and return the spam indicator

    :param text: message (string)
    :return: spam indicator (float)
    """
    # create set of unique words from given text
    # first, split to list to obtain words instead of characters
    unique_words = set(text.lower().split())  # case insensitive

    # identify words in the intersection of both sets (spam words)
    spam_subset = unique_words & SPAM_WORDS

    # calculate ratio of spam words to the total number of unique words
    if unique_words:
        spam_ratio = len(spam_subset) / len(unique_words)
    else:  # unique words is empty
        spam_ratio = len(unique_words)

    return spam_ratio


def classify(indicator):
    """
    Print the spam classification

    :param indicator: ratio of spam words to unique words (float)
    :return: None
    """
    # check if indicator exceeds the spam threshold
    if indicator > SPAM_THRESHOLD:
        print('This message is: SPAM')
    else:
        print('This message is: HAM')

    return


def get_input():
    """
    Prompt user for input repeatedly and return the input as a string

    :param: None
    :return: user input (string)
    """
    # repeatedly prompts user until a valid, nonempty message is entered
    message = ''
    while not message.strip():
        message = input('Please enter your message: ')

    # replace all punctuation characters in message with empty string
    for char in string.punctuation:
        message = message.replace(char, '')

    return message


def main():
    user_input = get_input()
    spam_ratio = spam_indicator(user_input)
    print(f'SPAM indicator: {spam_ratio:.2f}')  # 2 decimal places
    classify(spam_ratio)


if __name__ == '__main__':
    main()
