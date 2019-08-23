# This program will print out all of the text data from data.json
import json

# Opens tweetFile
tweetFile = open("./data.json" , "r")

# Gets data from opened list
tweetData = json.load(tweetFile)

# Close the file since data is already stored
tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])

for idx in range (len(tweetData)):
    print("Tweet id: ", tweetData[idx]["id"])

for tweet in tweetData:
    print("Tweet text: ", tweet["text"])
