#--------------------------------
#EXERCICE 13
#LEONIDAS PASTRAS
#P20155
#18-2-2021
#--------------------------------

rawText = open("C:\Python39\AcademicTasks\sem1\Ex13\Test.txt", "r")
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
allNums = []                                 # allNums is a mirror list to allWords, containing the all word's lengths
for word in allWords:                         
    allNums.append(len(word))
for num in allNums:
    i = allNums.index(num)
    if num >= 20:
        allNums.remove(num)
        allWords.remove(allWords[i])
allNums.sort(reverse=True)
allWords = sorted(allWords, key=len, reverse=True) # Here i reverse the lists to help me analyse them more easily
wordPairs = list()
i = 0
listLen = len(allWords)
def FindPairs(i):                                  # Recursion stuff...
    for k in range(i + 1, listLen):
        if allNums[i] < 20:
            numSum = allNums[i] + allNums[k]
            if numSum == 20:
                wordPairs.append(allWords[i] + ", " + allWords[k])
                allNums[k] = 20
                i = i + 1
                FindPairs(i)
                break
            elif numSum < 20:
                break
        else:
            i = i + 1
            FindPairs(i)
            break
FindPairs(i)
for pairs in wordPairs:
    print(pairs)


# NΟTE:
# when given big files to analyze, the program will throw the error: "RecursionError: maximum recursion depth exceeded in comparison"
# from what it know it is not reallt an error but a guard against a stack overflow,