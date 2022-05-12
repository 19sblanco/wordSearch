# mainMenu
    When you are done make an interface so its as friendly as the speed reading program


# help
    * python main.py 
        * print help menu
    * python main.py help
        * also print help menu



# WordSearch
    step amount 
        * 2 = skip a letter
        * -1 = go backward
    * search through the enire book of mormon
    * ignore everything but the letter(only isletter)
    * ignore the the chapter names (first nephi chapter 3) with a flag "-c"
    * if you find chapter heading:
        * manually enter in the chapter heading, you this should be a mode that you toggle 
    * python main.py "search" "word to look phrase" "step amount" "flag"
    * print out words that match, if non match print "non match"


# boolean search function 
    (n number of arguments) 
    * a or b and c
    * and is multiply (takes precidence)
    * or is addition 
    
## procedure
    * get the index of all intances of the first 
    * grab 150 indexes behind and 150 indexes infront of that word
    * pass that string along to the booleanEvaluator
    * if it returns a true print



    
    * verses start with [num: num] use a regex
    * parenthesis are allowed ()
    * do this within a verse, if the boolean function doesn't work within a verse go to the next verse and do the boolean function
    * search through a specific book, like first nephi
    * search through the enire book of mormon
    * search through all 4 standard works
        * search for which ones had the text files in them (let dad know)
    * for a certain mode you can specify the number of verse that it will look through
        * for example, if you choose three it will look for 123, 234, 345, 456, for the criteria
        * make sure this works for the first and last verse 
    * when you find a verse that flags true for the boolean funciton, print it out
    * python main.py "boolean" "boolean phrase" "books to look through" "number of verses to look through" 
    * print out words that match, if non match print "non match"

