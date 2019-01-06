import operator
import sys

def get_words_counts(words):
    unimportant_words = ('the', 'is', 'as', 'then', 'that', 'a', 'an', 'of', 'are', 'and', 'at', 'in', 'to', 'with', 'on', 'but', 'by')
    word_counts = {}
    unimportant_word_counts = {}

    for word in words.split(' '):
        processed_word = word.strip('!,.?:;(){}-').lower()

        if processed_word not in unimportant_words:
            if processed_word in word_counts:
                word_counts[processed_word] = word_counts[processed_word] + 1
            else:
                word_counts[processed_word] = 1
        else:
            if processed_word in unimportant_word_counts:
                unimportant_word_counts[processed_word] = unimportant_word_counts[processed_word] + 1
            else:
                unimportant_word_counts[processed_word] = 1

    return (word_counts.items(), unimportant_word_counts.items())

def get_n_most_frequent(word_counts, n):
    return sorted(word_counts, key=operator.itemgetter(1), reverse=True)[:n]

if len(sys.argv) == 3:
    number_of_most_frequent_words = int(sys.argv[1])
    document_string = sys.argv[2]
    word_counts, unimportant_word_counts = get_words_counts(document_string)
    most_frequent_words = get_n_most_frequent(word_counts, number_of_most_frequent_words)

    print(word_counts)
    print(unimportant_word_counts)
    print(most_frequent_words)