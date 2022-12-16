# TwitterToLCD
This project uses the Tweepy API and communicates information between a Raspberry Pi and an Arduino with an LCD to display recent mentions for some account specified in the code.

## Use
To use this, simply upload the .ino file to the Arduino using the Arduino IDE. Further, if you want to look at the console output for debugging purposes, ensure that you set the baud rate to that which is initiated when serial communication begins. You must connect the Raspberry Pi and Arduino together using a USB to allow serial communication. 

## Running Tweepy
To run Tweepy (Twitter API for Python), you can either add a credentials.json file in your directory or include your API tokens somewhere within the code. Simply run the python script using `python3 communicationstest.py` on your Raspberry Pi. For information on how to download Raspbian OS and run Python, check out [the Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html). 

## Why Use a Pi and an Arduino?
Because of the limited processing power of the Arduino Uno, I decided that this program would process the information on a Raspberry Pi, and then send the Twitter updates to the Arduino to display on its connected LCD. This is mostly because of the many API calls that the Pi makes, and it is much easier to interface with and use because of Raspbian. Plus, learning serial communication is cool - this video piqued my interest and was the source of this project. 
<a href="https://www.youtube.com/watch?v=wdgULBpRoXk">Ben Eater USB Protocol</a>


