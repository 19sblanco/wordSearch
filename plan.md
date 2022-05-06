# overall view of wordSearch

## inputs:
    wordSearch(fileName, phrase, stepAmount, lengthOfPrint, *flags)

## procedure:
    Set up:
        1. open file
        2. with file, split collection into dictionary {title: contents} (debug to make sure working)

    Seaching for phrase
        2. for each collection loop over all the characters that are letters
            * int pointer = 0
            * loop through book
                * if book[n] is letter:
                    * if book[n] matches first letter of phrase:
                        * if matches the rest of the word:
                            * noPhraseFound = false
                            * print the book name
                            * print 150 chars in front and behind it
                    
                pointer++

            if noPhraseFound:
                print("no phrase found")
                
## structure:
    fields:
        dictionaryOfBooks
        lengthOfPrint
        step

    methods:
        constructor:
            check inputs: ("" for phrase)
            split collection into dictionary
            searchForPhrase()

        searchForPhrase() 
            calls printPhrase("title", n)

        printPhrase(title, pointerInFile)
            prints title
            print(text[back:front:step])

