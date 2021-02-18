#--------------------------------
#EXERCICE 4
#LEONIDAS PASTRAS
#P20155
#18-2-2021
#--------------------------------

#Depending on the size of the .txt file this might take a while

import random
rawText = open("C:\Python39\AcademicTasks\sem1\Ex13\Test.txt", "r") #The Files Directory 
def TextCleaner(rawText):                           #TextCleaner takes the text given as an input (rawText) and tries (not always succesfuly) to clean any unwanted characters 
    text = rawText.read()
    lines = text.split("\n")                        #This is the best way i found to clean the "\n" character, by cutting the text in lines
    paragraph = " ".join(lines)                     #After the "\n" character is gone i put the lines together again
    allWords = paragraph.split(" ")                 #Create the allWords list which contains... all words!
    emptyWords = 0                                  #This is a counter of how many empty ("") words exist in the text
    i = 0
    while i < len(allWords):
        if "." in allWords[i]:
            allWords[i] = allWords[i].replace(".", "")
            continue
        if "," in allWords[i]:
            allWords[i] = allWords[i].replace(",", "")
            continue
        if "?" in allWords[i]:
            allWords[i] = allWords[i].replace("?", "")
            continue
        if "!" in allWords[i]:
            allWords[i] = allWords[i].replace("!", "")
            continue
        if "[" in allWords[i]:
            allWords[i] = allWords[i].replace("[", "")
            continue
        if "]" in allWords[i]:
            allWords[i] = allWords[i].replace("]", "")
            continue
        if "{" in allWords[i]:
            allWords[i] = allWords[i].replace("{", "")
            continue
        if "}" in allWords[i]:
            allWords[i] = allWords[i].replace("}", "")
            continue
        if '"' in allWords[i]:
            allWords[i] = allWords[i].replace('"', "")
            continue
        if ";" in allWords[i]:
            allWords[i] = allWords[i].replace(";", "")
            continue
        if allWords[i] == "":                # this is where i count all the empty words
            emptyWords = emptyWords + 1
            allWords.remove("")              # here is remove them from the list
            allWords.append("")              # and here i add them again at the end of the list because otherwise to loop gets confused and doesn't know when to end or something like that
        i = i + 1
    for i in range(emptyWords):              # and this is where i remove them by popping them (since they are all at the bottom of the list from the previous function)
        allWords.pop()
    return allWords                          # returns the clean text
allWords = TextCleaner(rawText)
notPairs = len(allWords) % 3                 # here i count the max amount of pairs that can be created
Pairs = allWords.copy()                      # In the list "Pairs" is where all the pairs will be created
loopCount = len(allWords) - 1 - notPairs
for i in range (0, loopCount, 3):            # here the pairs are born
    for j in range (i, i + 3):
        if j == i:
            Pairs[i] = allWords[j]
        elif j == i + 1:
            Pairs[i] = Pairs[i] + " " + allWords[j] + " "
            Pairs[j] = ''
        else:
            Pairs[i] = Pairs[i] + allWords[j]
            Pairs[j] = ''
loopCount = len(Pairs) - 1
k = 0
for i in range(loopCount):                  # In the next 2 loops, just like above i count the empty pairs and them destroy them
    if Pairs[i] == '':
        k = k + 1
        Pairs.remove('')
        Pairs.append('')
loopCount = k + 1 + notPairs
for i in range(loopCount):
    Pairs.pop()
r = random.randint(0, len(Pairs) - 1)       # Here i chose a random int from 0 to the length of the pairs list, that translates to THE RANDOM PAIR OF 3
for i in range(len(Pairs)):                 # Here the pairs turn from one string ["x y z"] into little lists of strings [["x"], ["y"], ["z"]], this helps me to analyse them below
    Pairs[i] = Pairs[i].split(" ")
finalWords = []                             # finalWords is the list of words that will contain all the words that will be used to create the final sentence
finalWords.append(Pairs[r][1])              # these are the LAST 2 WORDS OF THE RANDOM PAIR OF 3 
finalWords.append(Pairs[r][2])
phrase = finalWords[0] + finalWords[1] 
for pair in Pairs:                          # in this loop is tries to find a pair of 3 that starts with the 2 last words the RANDOM PAIR OF 3 
    if pair[0] == finalWords[0]:
        if pair[1] == finalWords[1]:
            finalWords.append(pair[2])      # if it does find such a pair, then it adds it the word to the finalWords list
random.shuffle(finalWords)
k = 0
for word in finalWords:                     # in this loop the final sentence in created
    k = k + 1
    if k <= 200:                            # making sure there are no more than 200 words in the sentence
        if k == 1:
            phrase = word
        else: 
            phrase = phrase + " " + word
    else:
        break
print(phrase)

           

# EXMAPLE:
# RANDOM PAIR OF 3: [["x"], ["y"], ["z"]]
# finalWords = ["y", "z"]
# SEARCHES AND FINDS THE PAIR: [["y"], ["z"], ["k"]]
# finalWords = ["y", "z", "k"]
#
# NΟTE:
# it usually just prints 2 words since its pretty rare to find matching pairs, but it does work once in a while!