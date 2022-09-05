import serial
import time
import os
import tweepy
import time
import numpy as np


#Beginning serial communication

ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
ser.flush()
    
     
# Authentication credentials for tweepy
consumer_key = "yjDamjWijnHPNn08DuvVoUE3i"
consumer_key_secret = "uIugP7QUK9PAZtt0P7tkboVXH8ePreZuAHEZePmDcYOG8kclp8"
access_token = "1097267186522046464-lygM6UATwQ3HMCpzim1ShcQouHrGab"
access_token_secret = "f4GbjfXqtKTbSx29IYWQigIhcehtrhML8joyY25hBrwoh"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret, access_token, access_token_secret)

api = tweepy.API(auth)




# TODO: create a loop such that tweepy constantly is looking for new tweets that mentions me, gets their text and displays them on the arduino lcd. If no new tweets are coming in that mention me,
# say "Waiting for new tweets that mention you...". Goes until program is stopped.

# TODO Send to LCD: "Displaying most recent mention:"

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
            
            
            
        
    
    
    
        
    
        
    
    
    
    

# 
#     while True:
#         s = "I Love You!!"
#         
#         ser.write(s.encode('utf-8'))
#         line = ser.readline().decode('utf-8').rstrip()
#         print(line)
#         time.sleep(0.5)
        