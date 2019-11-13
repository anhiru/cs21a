# ----------------------------------------------------------------------------
# Name:         wordstats
# Purpose:      CS 21A Assignment # 5
#
# Author:       Andrew Tran
# Date:         05/11/2019
# ----------------------------------------------------------------------------
"""
Program that computes language statistics based on the contents of a text file

Prompt the user to enter the file name.
Open and read the text file under the given name.
Compute language statistics, including the following:
longest word, most common words, word count.
"""
import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random


# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified

    :param input_count: represents words and their corresponding counts (dict)
    :param min_length: optional - defaults to 0
            minimum length of the words that will appear
            in the cloud representation
    :return: None

    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    current_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=current_row % 5, column=current_row // 5)
        current_row += 1
    root.mainloop()


# Enter your own helper function definitions here


def count_words(filename):
    """
    Build and return the dictionary for the given filename

    :param filename: name of the file (string)
    :return: items in the form of words: frequency (dictionary)
    """
    words_count = {}  # initialize empty dictionary

    # open file for reading
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.lower()  # ignore capitalization
            for word in line.split():
                # remove leading and trailing punctuation marks and digits
                word = word.strip(string.punctuation + string.digits)
                if word:  # check for empty string
                    if word in words_count:
                        words_count[word] += 1  # increment the count by 1
                    else:
                        words_count[word] = 1  # initialize a new entry

    return words_count


def report(word_dict):
    """
    Report on various statistics based on the given word count dictionary

    :param word_dict: items in the form of words: frequency (dictionary)
    :return: None
    """
    # find one of the longest words used in the file
    longest_word = max(word_dict, key=len)
    print(f'\nThe longest word is: {longest_word}')

    print('\nThe 5 most common words are:')
    # build list of top 5 words sorted by decreasing frequency
    for word in sorted(word_dict, key=word_dict.get, reverse=True)[:5]:
        # print words with the number of times they appear in the file
        print(f'{word}: {word_dict[word]}')

    # record the word count of every word in the file, sorted alphabetically
    # open file for writing in 'w' mode
    with open('out.txt', 'w', encoding='utf-8') as file:
        # build list of words sorted alphabetically
        # suppress the last item so the output contains no trailing empty line
        for word in sorted(word_dict)[:-1]:
            file.write(f'{word}: {word_dict[word]}\n')  # write onto new file
        # print the last word outside the loop
        last_word = list(sorted(word_dict.keys()))[-1]
        file.write(f'{last_word}: {word_dict[last_word]}')


def main():
    # get the input file name
    input_name = input('Please enter the input file name: ')

    # build the dictionary for the given file
    word_count = count_words(input_name)

    # report on the contents of the dictionary word_count
    report(word_count)

# If you want to generate a word cloud, uncomment the line below.
# draw_cloud(word_count)


if __name__ == '__main__':
    main()
