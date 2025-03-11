# German -> English Dict CC Translate
Find translations and keep track of German words you want to review.

Built on top of [dict.cc.py](https://github.com/rbaron/dict.cc.py) - sourcing words from the wonderful [dict.cc](https://www.dict.cc/)

Returns the top 3 search terms from `dict.cc`.

Also writes the terms into a file called `searched_words.txt` for further review.

## Setup:
```
pip3 install -r requirements.txt
```

## Usage:
```
python3 translate.py "<search_terms>" [<en_to_de>]
```
E.G.:
```
$ python3 translate.py "ausprobieren"
20 matches - first 3: test sth. - check out sth. - check sth. out
$ python3 translate.py "test" 1
49 matches - first 3: etw. ausprobieren - etw. prüfen - jdn. etw. untersuchen
```

