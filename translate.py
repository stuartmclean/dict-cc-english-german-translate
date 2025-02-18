#!/usr/bin/env python3

from sys import argv
from dictcc import Dict
from itertools import filterfalse

def translate(word):
    translator = Dict()
    result = translator.translate(word, from_language="en", to_language="de")
    basic_translations = list(filterfalse(lambda tup: '[' in tup[1], result.translation_tuples))
    first_matches = ' - '.join([translation[1] for translation in basic_translations[:3]])
    with open('searched_words.txt', 'a') as searched_words:
        searched_words.write(f"{word}: {first_matches}\n")
    print(first_matches)

if __name__ == '__main__':
    if len(argv) < 2:
        print('no search term provided')
        exit(-1)
    translate(argv[1])

