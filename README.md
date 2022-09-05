# TwitterToLCD
SUMMARY: This project was a small personal project where I used the Tweepy API (Twitter for python) to live update mentions from my Twitter account, and display them on an LCD connected to an arduino.


Because of the limited processing power of the Arduino Uno, I decided that this program would process the information on a Raspberry Pi, and then send the Twitter updates to the Arduino to display on its connected LCD. I did this via serial communication. Most of this code was self-taught, so it's not very refined and clean! (<Apologies in advance>). The python file runs on the Pi, and upload the C file to the arduino using the arduino IDE. Thanks for checking this project out!!
