import sys
import wordSearch as w
import re

# print(f"Name of the script      : {sys.argv[0]=}")
# print(f"Arguments of the script : {sys.argv[1:]=}")

phrase = "tuh"
# t = "a n,   a p p l e"

# print(t[0:-1:2])
"""
problem if you are going to ignore certain chars ","
then you will have to accound for that when you print the output
the [::] slice operator doesn't account for the commanas

a solution would be to rid the file of all non alpha and space characters before
processing the file
"""
"""
dad's program
    use a regex 
        * get rid of all non letter and space characters
        * do a string builder, build up the number of step amounts 
            * step = 2
            * [first letter][only letters and spaces][second letter][only letters and spaces]


"""
wSearch = w.WordSearch("Bom.txt", phrase.lower(), 2, True) 




