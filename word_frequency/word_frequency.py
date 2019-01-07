import operator
import re
import sys
import time

def create_or_update_word(word, word_dictionary):
    if word in word_dictionary:
        word_dictionary[word] = word_dictionary[word] + 1
    else:
        word_dictionary[word] = 1

def get_word_counts(words, ignored_words):
    word_counts = {}
    unimportant_word_counts = {}

    for word in words.split(' '):
        processed_word = word.rstrip('!,.?:;-').lower()

        if processed_word not in ignored_words:
            create_or_update_word(processed_word, word_counts)
        else:
            create_or_update_word(processed_word, unimportant_word_counts)

    return (word_counts.items(), unimportant_word_counts.items())

def get_n_most_frequent(word_counts, n):
    return sorted(word_counts, key=operator.itemgetter(1), reverse=True)[:n]

if len(sys.argv) == 4:
    number_of_most_frequent_words = int(sys.argv[1])
    text_file_name = sys.argv[2]
    ignored_words_file_name = sys.argv[3]
    document_string = ''
    ignored_words_string = ''

    with open(text_file_name) as file_object:
        document_string = file_object.read()
        document_string = re.sub('[^!-~]+', ' ', document_string).strip()

    with open(ignored_words_file_name) as file_object:
        ignored_words_string = file_object.read()
        ignored_words_string = ignored_words_string.split('\n')

    startTime = time.time()
    word_counts, unimportant_word_counts = get_word_counts(document_string, ignored_words_string)
    print("Counting words took %f seconds" % (time.time() - startTime))

    startTime = time.time()
    most_frequent_words = get_n_most_frequent(word_counts, number_of_most_frequent_words)
    print("Getting top %d words took %f seconds" % (number_of_most_frequent_words, time.time() - startTime))

    # print(word_counts)
    # print(unimportant_word_counts)
    print(most_frequent_words)