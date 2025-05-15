#!/usr/bin/env python3

from argparse import ArgumentParser
from datetime import datetime
from dictcc import Dict
from itertools import filterfalse
import json
from pathlib import Path
from searchedword import SearchedWord
from typing import List

TXT_FILE = 'searched_words.txt'
JSON_FILE = 'searched_words.json'


def translate(word, matches_to_show, from_english=False):
    result = _fetch_result(word, from_english)

    if from_english:
        lang = "en"
    else:
        lang = "de"
    
    if result.n_results == 0:
        print(f'no results found for "{word}"')
        return

    basic_translations = list(filterfalse(lambda tup: '[' in tup[1], result.translation_tuples))
    first_matches = ' - '.join([translation[1] for translation in basic_translations[:matches_to_show]])
    with open(TXT_FILE, 'a') as searched_words:
        searched_words.write(f"{word}: {first_matches}\n")

    update_or_add_word(word, first_matches, lang)

    print(f'{result.n_results} matches - first {matches_to_show}: {first_matches}')

def load_words(filename: str) -> List[SearchedWord]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [SearchedWord.from_json(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_words(words: List[SearchedWord], filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([word.to_json() for word in words], f, indent=2)

def update_or_add_word(new_word: str, definition: str, lang: str):
    words = load_words(JSON_FILE)
    now = datetime.now()

    for word in words:
        if word.word == new_word and word.lang == lang:
            word.times_searched += 1
            word.last_searched = now
            break
    else:
        searched_word = SearchedWord(
            word=new_word,
            definition=definition,
            lang=lang,
            first_searched=now,
            last_searched=now,
            times_searched=1
        )
        words.append(searched_word)

    save_words(words, JSON_FILE)

def _fetch_result(word, from_english):
    translator = Dict()
    if from_english:
        return translator.translate(word, from_language="en", to_language="de")
    else:
        return translator.translate(word, from_language="de", to_language="en")


if __name__ == '__main__':
    parser = ArgumentParser(
        prog=Path(__file__).stem,
        description="Get quick translations between German and English",
    )
    parser.add_argument(
        "-d",
        "--from-german",
        help="Translate from German to English",
    )
    parser.add_argument(
        "-e",
        "--from-english",
        help="Translate from English to German",
    )
    parser.add_argument(
        "-m",
        "--matches-to-show",
        type=int,
        default=3,
        help="The number of matches to show",
    )
    args = parser.parse_args()

    if args.from_german and args.from_english:
        print('only one of --from-german (-d) or --from-english (-e) can be provided')
        exit(-1)

    if not args.from_german and not args.from_english:
        print('one of --from-german (-d) or --from-english (-e) must be provided')
        exit(-1)

    if args.from_german:
        translate(args.from_german, args.matches_to_show)
    else:
        translate(args.from_english, args.matches_to_show, from_english=True)

