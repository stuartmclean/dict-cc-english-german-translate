#!/usr/bin/env python3

from sys import argv
from dictcc import Dict
from itertools import filterfalse


def translate(word, from_english=False):
    result = _fetch_result(word, from_english)
    if result.n_results == 0:
        print(f'no results found for "{word}"')
        return

    basic_translations = list(filterfalse(lambda tup: '[' in tup[1], result.translation_tuples))
    first_matches = ' - '.join([translation[1] for translation in basic_translations[:3]])
    with open('searched_words.txt', 'a') as searched_words:
        searched_words.write(f"{word}: {first_matches}\n")
    print(f'{result.n_results} matches - first 3: {first_matches}')


def _fetch_result(word, from_english):
    translator = Dict()
    if from_english:
        return translator.translate(word, from_language="en", to_language="de")
    else:
        return translator.translate(word, from_language="de", to_language="en")


if __name__ == '__main__':
    if len(argv) < 2:
        print('no search term provided')
        exit(-1)
    translate(argv[1], bool(argv[2]) if len(argv) > 2 else False)

