# ----------------------------------------------------------------------------
# Name:         aggregator.py
# Purpose:      CS 21A - implement a simple general purpose aggregator
#
# Author:       Andrew Tran
# Date:         06/09/2019
# ----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input file that contains a list of the online sources (URLs)
topic: topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys
import os.path


def aggregate(filename, topic):
    """
    Systematically compile references to a topic from multiple URLs in a file

    :param filename: name of file that contains a list of URLs (string)
    :param topic: topic to be researched and reported on
    :return: None
    """
    # open output file before iterating through the URLs
    with open(f'{topic}summary.txt', 'w', encoding='utf-8') as output_file:
        with open(filename, 'r', encoding='utf-8') as source_file:
            for line in source_file:  # read file to fetch one URL at a time
                try:
                    with urllib.request.urlopen(line) as url_file:
                        decoded_page = url_file.read().decode('utf-8')
                except urllib.error.URLError as url_err:
                    print(f'Error opening url: {line}{url_err}')
                except UnicodeDecodeError as decode_err:
                    print(f'Error decoding url: {line}\n{decode_err}')
                else:  # executed if no exceptions are raised
                    references = url_references(decoded_page, topic)
                    write_output(output_file, line, references)


def url_references(text, topic):
    """
    Capture all references to the given topic found inside angle brackets

    :param text: the given text from URL (string)
    :param topic: topic to be researched and reported on (string)
    :return: references to the topic, separated by new line characters (string)

    An empty string is returned if there are no such references.
    """
    all_references = ''  # initialize empty string of references

    # extract text inside angle brackets containing the topic
    pattern = fr'>([^<]*\b{topic}\b.*?)<'
    matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)

    # join all references, separated by new line characters
    if matches:
        all_references = '\n'.join(matches)

    return all_references


def write_output(output_file, url, references):
    """
    Write URLs and text containing references to the topic onto an output file

    :param output_file: file object containing output (File)
    :param url: name of URL (string)
    :param references: references to the topic (string)
    :return: None
    """
    if references:  # write only if source URL includes reference to topic
        output_file.write(f'{url}\n{references}\n')
        for i in range(70):
            output_file.write('-')
        output_file.write('\n')


def valid_source(filename):
    if os.path.realpath(filename):
        return True
    else:
        return False


def main():
    # issue an error message if the cmd line arguments are too few or too many
    if len(sys.argv) != 3:
        print('Error: invalid number of arguments')
        print('Usage: aggregator.py filename topic')
    else:
        filename = sys.argv[1]  # get the filename argument
        topic = sys.argv[2]  # get the topic argument
        aggregate(filename, topic)


if __name__ == '__main__':
    main()
