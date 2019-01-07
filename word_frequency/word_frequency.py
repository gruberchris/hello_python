import operator
import re
import sys
import time


def get_word_counts(words, ignored_words):
    word_counts = {}

    reversed_ignored_words = sorted(ignored_words, reverse=True)

    for word in words.split():
        processed_word = word.lstrip('([!,.?:;-)]')
        processed_word = processed_word.rstrip('([!,.?:;-)]')
        processed_word = processed_word.lower()

        if len(processed_word) == 0:
            continue

        if processed_word in word_counts:
            word_counts[processed_word] = word_counts[processed_word] + 1
            continue

        if processed_word[0] in ['n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            if processed_word not in reversed_ignored_words:
                word_counts[processed_word] = 1
        else:
            if processed_word not in ignored_words:
                word_counts[processed_word] = 1

    return word_counts.items()


def get_n_most_frequent(word_counts, n):
    return sorted(word_counts, key=operator.itemgetter(1), reverse=True)[:n]


def start():
    number_of_most_frequent_words = 1
    document_text = ''
    ignored_words = []

    if len(sys.argv) >= 2:
        number_of_most_frequent_words = int(sys.argv[1])

    if len(sys.argv) >= 3:
        input_file_name = sys.argv[2]

        try:
            with open(input_file_name) as file_object:
                raw_document_text = file_object.read()
                document_text = re.sub('[^!-~]+', ' ', raw_document_text).strip()
        except FileNotFoundError:
            print('The specified input file %s does not exist' % (input_file_name))
            return

    if len(sys.argv) >= 4:
        ignored_words_file_name = sys.argv[3]

        try:
            with open(ignored_words_file_name) as file_object:
                raw_document_text = file_object.read()
                ignored_words = raw_document_text.split('\n')
        except FileNotFoundError:
            print('The specified ignored words file %s does not exist' % (ignored_words_file_name))
            return

    startTime = time.time()
    word_counts = get_word_counts(document_text, ignored_words)
    print("Counting words took %f seconds" % (time.time() - startTime))

    startTime = time.time()
    most_frequent_words = get_n_most_frequent(word_counts, number_of_most_frequent_words)
    print("Getting top %d words took %f seconds" % (number_of_most_frequent_words, time.time() - startTime))

    # print(word_counts)
    print(most_frequent_words)


# example to run, "python3 word_frequency.py 10 usa-constitution.txt unimportant_words.txt
start()
