import re 
import time



"""
take in a boolean expression in the form of a string, if it
finds an occurance in the larger text (book) that matches
the boolean expression, then it will print it out
"""
class booleanEvaluate:
    exp = ""
    bookOriginal = ""
    bookLowerCase = ""
    length = 0

    def __init__(self, file, expression, userDefinedLength=150):
        # error checking
        if expression == "":
            print("Invalid input")
            return

        # setting variables
        self.exp = self.normalize(expression)
        with open(file) as f:
            self.bookOriginal = f.read()
        self.bookLowerCase = self.bookOriginal.lower()
        self.length = userDefinedLength

        # check and find instances in book that match boolean expression
        instances = self.findInstances()
        if instances:
            self.printInstances(instances)
        else:
            print("no instances of that expression found")


    """
    normalize the expressions passed in by the user
    """
    def normalize(self, exp):
        exp = exp.lower()
        if "(" in exp or ")" in exp:
            exp = exp.replace("(", " ( ")
            exp = exp.replace(")", " ) ")
        return exp



    """
    check for instances of the expression found in the book
    and returns a list of indexes where it found the 
    expression to be true in t
    """
    def findInstances(self):
        instancesFound = []

        words = self.getWordsToLookFor()
        print("words: ", words)

        # get the index of each word in words into a list
        potentialWordIndexes = []
        for word in words:
            temp = [m.start() for m in re.finditer(word, self.bookLowerCase)]
            potentialWordIndexes = potentialWordIndexes + temp
        potentialWordIndexes.sort() # list must be in order for the next step
        

        # from that list found in the last step, sort out each redundant index
        # a redudant indexs is an index that is within user defined length range
        # of a valid index, valid indexes start from the left
        wordIndexes = []
        wordIndexes.append(potentialWordIndexes[0])
        for i in potentialWordIndexes:
            if abs(wordIndexes[-1] - i) > self.length: # if the difference between the two words is greater than the user defined length:
                wordIndexes.append(i)

            
        # now you have a list without redundant key words, search for matches to
        # the boolean phrase
        for i in wordIndexes:

            ###
            # words: ['mary', 'jesus']
            # instances found @: [386706]

            if i ==  386706:
                pass
            ###

            subString = self.getSubString(i)
            if self.checkExpression(subString):
                instancesFound.append(i)

        return instancesFound 


    """
    from the user provided expression
    get all words to look for and return it as a list
    """
    def getWordsToLookFor(self):
        words = []
        wordsToConsider = self.exp.split()

        for word in wordsToConsider:
            w = "".join([i for i in word if i.isalpha()])

            if w == "" or w == "and" or w == "or":
                continue

            words.append(w)
        
        if words:
            return words
        else:
            print(
                f"""an error occurred: getWordsToLookFor
                espression: {self.exp}
                If this is a bug please report back to Steven""")
            
            exit()


    """
    based on the instances found print off the string
    """
    def printInstances(self, instancesIndex):
        print("instances found @: ", len(instancesIndex), instancesIndex)
        for i in instancesIndex:
            subString = self.getSubString(i)
            print("=============")
            print(subString)
            print("=============")

    
    def getSubString(self, index):
        back = index - self.length
        if back < 0: 
            back = 0

        front = index + self.length + 1 # +1 because [] operator used later chops off the last char
        if front >= len(self.bookLowerCase): 
            front = len(self.bookLowerCase)

        return self.bookLowerCase[back:front]


    """
    check the boolean espression withing the substring
    """
    def checkExpression(self, subString):
        operatorStack = []
        valueStack = []

        tokens = self.exp.split(" ")

        for t in tokens:
            t.strip()
            if t == "": continue

            elif t == "and" or t == "(":
                operatorStack.append(t)

            elif t == "or":
                if self.isOnTop(operatorStack, "or"):
                    self.popOperatorApplyToTopTwoStackValues(
                        valueStack, operatorStack, subString
                    )
                operatorStack.append(t)

            elif t == ")":
                if self.isOnTop(operatorStack, "or"):
                    self.popOperatorApplyToTopTwoStackValues(
                        valueStack, operatorStack, subString
                    )

                    if self.isOnTop(operatorStack, "("):
                        operatorStack.pop()
                    else:
                        print(
                            f"""an error occurred: checkExpression
                            token: {t}
                            operatorStack: {operatorStack}
                            valueStack: {valueStack}
                            espression: {self.exp}
                            If this is a bug please report back to Steven"""
                        )

                    if self.isOnTop(operatorStack, "and"):
                        self.popOperatorApplyToTopTwoStackValues(
                            valueStack, operatorStack, subString
                        )

                elif self.isOnTop(operatorStack, "("):
                    operatorStack.pop()

                else:
                    print(
                        f"""an error occurred: checkExpression
                        token: {t}
                        operatorStack: {operatorStack}
                        valueStack: {valueStack}
                        espression: {self.exp}
                        If this is a bug please report back to Steven"""
                    )

            else: # string word
                valueStack.append(t)
                if self.isOnTop(operatorStack, "and"):
                    self.popOperatorApplyToTopTwoStackValues(
                        valueStack, operatorStack, subString
                    )


        if not operatorStack and valueStack:
            value = valueStack.pop()
            if (self.isBool(value)): 
                return eval(value)
            else:
                return value in self.bookLowerCase
 

        elif self.isOnTop(operatorStack, "or") or self.isOnTop(operatorStack, "and"):
            if len(operatorStack) == 1 and len(valueStack) == 2:

                self.popOperatorApplyToTopTwoStackValues(
                    valueStack, operatorStack, subString
                )
                return eval(valueStack.pop().title())

        else:
            print(
                f"""an error occurred: checkExpression
                token: {t}
                operatorStack: {operatorStack}
                valueStack: {valueStack}
                espression: {self.exp}
                If this is a bug please report back to Steven""")


    def popOperatorApplyToTopTwoStackValues(self, valueStack, operatorStack, subString):
        try:
            word1 = valueStack.pop()
            word2= valueStack.pop()
            op = operatorStack.pop()

            output = self.performOperation(word1, word2, op, subString)
            valueStack.append(str(output))            

        except:
            print(
                f"""an error occurred: popOperatorApplyToTopTwoStackValues
                value stack: {valueStack}
                operator stack: {operatorStack}
                If this is a bug please report back to Steven""")


    """
    perform a boolean operation between two values based on
    if they are in the substring
    """
    def performOperation(self, word1, word2, op, subString):
        # between two boolean values "True and False"
        if self.isBool(word1) and self.isBool(word2):
            return eval(word1.title() + " " + op + " " + word2.title())

        elif self.isBool(word1):
            strBool = str(word2 in subString)
            return eval(word1.title() + " " + op + " " + strBool)
        
        elif self.isBool(word2):
            strBool = str(word1 in subString)
            return eval(strBool + " " + op + " " + word2.title())

        # no values are boolean, meaning they are both words
        else:
            if op == "and":
                return word1 in subString and word2 in subString
            elif op == "or":
                return word1 in subString or word2 in subString
            else:
                print(
                    f"""an error occurred: perform operation 
                    word1: {word1}
                    word2: {word2}
                    operation {op}
                    If this is a bug please report back to Steven""")
        

    """
    check if a string is a boolean word
    """
    def isBool(self, string):
        return string.lower() == "true" or string.lower() == "false"
             
    """
    return if the token is on top of the stack
    """
    def isOnTop(self, stack, token):
        if stack:
            return stack[-1] == token
        else:
            return False



start = time.time()


file = "Bom.txt"
expression = "jesus and nephi"
userDefinedLength = 150

b = booleanEvaluate(file, expression, userDefinedLength)


end = time.time()
print("time: ", end - start)
