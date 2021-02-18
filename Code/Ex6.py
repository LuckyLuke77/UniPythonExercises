#--------------------------------
#EXERCICE 6
#LEONIDAS PASTRAS
#P20155
#18-2-2021
#--------------------------------

import tweepy
import webbrowser

consumer_key = "wcnXcos81AbbRUmav7F5etvx7" #API key
consumer_secret = "GmgadKmFZ2LAKvlTb50sZiZAttwJIfdEZB5v0aau9Bv2DwIVmP" #API key secret
callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri) #Some tweepy stuff that i don't really understand
redirect_url = auth.get_authorization_url()                             #Gets the url that redirects you to the tweeter authorization page
webbrowser.open(redirect_url)                                           #Redirects you to the tweeter authorization page
user_pint_input = input("Enter the pint value: ")                               
auth.get_access_token(user_pint_input)                                  #Does tweepy stuff...
api = tweepy.API(auth)
me = api.me()
screen_name = input("Enter a tweeter username: ")
count = 10                                                                    #How many tweets it will read
statuses = api.user_timeline(screen_name, count=count, tweet_mode='extended') #Reads the tweets
allTweets = ""
for status in statuses:
   allTweets = allTweets + status.full_text + "\n"
def TextCleaner(rawText):                           #TextCleaner takes the text given as an input (rawText) and tries (not always succesfuly) to clean any unwanted characters 
    lines = rawText.split("\n")                     #This is the best way i found to clean the "\n" character, by cutting the text in lines
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
    return allWords   
allWords = TextCleaner(allTweets)                
longWords = ["", "", "", "", ""]
for word in allWords: #does stuff
    isNotLink = True
    for i in range(0, 5):
        if "https" not in word and "@" not in word and "#" not in word: #Filters links, mentionsn and hashtags 
            if longWords[i] != word:
                if len(longWords[i]) < len(word):
                    longWords[i] = word
                    break
shortWords = [longWords[0], longWords[0], longWords[0], longWords[0], longWords[0]]
for word in allWords:
    for i in range(0, 5):
        if shortWords[i] != word and word != '':
            if len(shortWords[i]) > len(word):
                shortWords[i] = word
                break
        else:
            break
print("\nThe 5 longest words contained in the last 10 tweets of the user " + screen_name + " are: \n")
for i in range(0, 5):
    print(longWords[i] + "\n")
print("Whilst the 5 shortest words contained in those 10 tweets are: \n" )
for i in range(0, 5):
    print(shortWords[i] + "\n")