import re
"""
problem:
    when it iterates the index it doesn't skip over the charcters that
    you want it to skip over, like commas
"""

"""
fileName, phraseToSearch, stepAmount, ignoreChapterNamesFlag=False
    flags
        -c : ignore chapter names    
"""
class WordSearch:

    __file = None
    __phraseToSearch = ""
    __stepAmount = None 
    __ignoreChapterNamesFlag = False 
    __phraseFound = False
    __pattern = "[a-zA-Z ]"

    def __init__(self, fileName, phraseToSearch, stepAmount, ignoreChapterNamesFlag=False):

        with open(fileName) as f:
            self.__file = f.read().lower()

        self.__phraseToSearch = phraseToSearch
        self.__stepAmount = stepAmount
        self.__ifgnoreChapterNamesFlag = ignoreChapterNamesFlag
        if (phraseToSearch == ""):
            print("please provide a phrase")
            exit()

        self.searchWord()
     
    def searchWord(self):
        indexInFile = 0
        while indexInFile < len(self.__file):
            if self.__file[indexInFile] == self.__phraseToSearch[0]:

                indexInWord = indexInFile
                # loop over word chekcing if file letters match
                for i in range(len(self.__phraseToSearch)):
                    exitLoop = False

                    # on the last ieration, if this loop doesn't exit
                    # from nonmatchin characters (all chars match)
                    # print it 
                    if i == len(self.__phraseToSearch) - 1: 
                        print(i)
                        print(self.__phraseToSearch[i])
                        self.printPhrase(indexInFile, self.__file)                    

                    if indexInWord > len(self.__file) - 1:
                        break

                    while not re.match(self.__pattern, self.__file[indexInWord]):
                        indexInWord += 1
                        if indexInWord > len(self.__file) - 1:
                            exitLoop = True
                            break

                    print(indexInWord)

                    if exitLoop:
                        break
                    if self.__file[indexInWord] == self.__phraseToSearch[i]:
                        indexInWord = self.iterateIndex(indexInWord)

                       

                    else:
                        print("break")
                        break
                #as;lkjasd;lfkja;slkjasd;lfkjas;dlkfja;sldkfja;lskdjf;alksj
                break

            # iterate
            indexInFile = self.iterateIndex(indexInFile)
        if not self.__phraseFound:
            print("no phrases found")


    """
    print the current index, with step amount, 150 chars back and 150 chars forward
    todo: you may want the front to start from the end of the word instead of the beginning
    """
    def printPhrase(self, index, file):
        self.__phraseFound = True

        back = index - (15 * self.__stepAmount)
        front = index + (15 * self.__stepAmount)

        if back < 0:
            back = 0
        
        if front > len(file):
            front = len(file) 

        print("==========")
        print(file[back:front:self.__stepAmount])
        print("==========")


    def iterateIndex(self, index):
        iterationAmounts = 0
        print("before", index)

        while iterationAmounts < self.__stepAmount:
            index += 1
            iterationAmounts += 1

            if index >= len(self.__file) - 1:
                break

            while not re.match(self.__pattern, self.__file[index]):
                index += 1
        print("after", index)

        return index




                      