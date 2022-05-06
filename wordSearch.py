import re


class WordSearch:
    __noPhraseFound = True
    __lengthOfPrint = None
    __step = None
    __books = {}


    def __init__(self, fileName, phrase, stepAmount, lengthOfPrint, *flags):
        # open file and parse into book
        pass

    """
    open the file and parse into __books{"title": "content"}
    """
    def prepareFile():
        pass

    """
    For each book in __books this will look for matching phrase
    """
    def searchForPhrase():
        pass

    """
    print the phrase found in searchForPhrase
    using __step and __lengthOfPrint
    """
    def printPhrase(title, pointer):
        pass

