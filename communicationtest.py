import serial
import time
import os
import tweepy
import time



#Beginning serial communication

ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
ser.flush()
    
     
# Authentication credentials for tweepy
consumer_key = #Redacted for privacy reasons
consumer_key_secret = #Redacted for privacy reasons
access_token = #Redacted for privacy reasons
access_token_secret = #Redacted for privacy reasons

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret, access_token, access_token_secret)

api = tweepy.API(auth)






# Initializes the arrays that display the tweet concisely 
lastMentionArr = ["temp"]
thisMentionArr = ["temp"]


#Gets the most recent tweet mentioning user


while True:
    
    print("Most recent tweet mentioning you:")
    
    # Gets most recent tweet mentioning you and prints it
    lastMention = tweepy.Cursor(api.search_tweets, q = "@itisKanyeEast", count = 1, tweet_mode="extended").items(1)
    for t in lastMention:
        lastMentionArr[0] = (t.user.screen_name, t.full_text)
    print(lastMentionArr)
    # Sends most recent tweet mentioning you to LCD
    #ser.write((str(lastMentionArr)+'\n').encode('utf-8'))
    time.sleep(5)
    
        
    while True:
        print("Searching for new mentions...")
        thisMention = tweepy.Cursor(api.search_tweets, q = "@itisKanyeEast", count = 1, tweet_mode="extended").items(1)
        for t in thisMention:
            thisMentionArr[0] = (t.user.screen_name, t.full_text)
        time.sleep(5)
            
        if(thisMentionArr == lastMentionArr):
            print("No new mentions found.")
            t = str("Your last mention was: "+str(thisMentionArr)+'\n')
            ser.write(t.encode('utf-8'))
            time.sleep(5)
            
            
            
        else:
            
            for t in thisMention:
                thisMentionArr[0] = (t.user.screen_name, t.full_text)
            print("New tweet mentioned you! "+ str(thisMentionArr)+'\n')
            s =("New tweet mentioned you!" + str(thisMentionArr) + '\n')
            ser.write(s.encode('utf-8'))
            time.sleep(5)
            lastMentionArr[0] = thisMentionArr[0]
            thisMentionArr[0] = " "
            
