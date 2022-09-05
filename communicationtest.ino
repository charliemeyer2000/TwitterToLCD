
#include <LiquidCrystal.h>
const int pin_RS = 8; 
const int pin_EN = 9; 
const int pin_d4 = 4; 
const int pin_d5 = 5; 
const int pin_d6 = 6; 
const int pin_d7 = 7; 
const int pin_BL = 10; 
LiquidCrystal lcd( pin_RS,  pin_EN,  pin_d4,  pin_d5,  pin_d6,  pin_d7);
int Li = 16;
int Lii = 0;
String topText = "TEMPORARY TEXT";
String bottomText = "SOME MORE TEMPORARY TEXT FOR YA";

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Latest Mention:");
  lcd.setCursor(0, 1);
  
  
  
}

void loop () {
  // Get info from pi here and assign topText & bottomText with serial

  if(Serial.available()>0){
    String data = Serial.readStringUntil('\n');
    for (int i = 0; i < data.length() + 18; i++)
    {
      lcd.setCursor(0, 1);
      lcd.print(Scroll_LCD_Left(data));
      delay(250);
      
    }
    Clear_LCD_Left();
    
    
  }
 

}

void Clear_LCD_Left()
{
  Li = 16;
  Lii = 0;
}

String Scroll_LCD_Left(String StrDisplay){
  String result;
  String StrProcess = "          " + StrDisplay + "            ";
  result = StrProcess.substring(Li, Lii);
  Li++;
  Lii++;
  if (Li>StrProcess.length()){
    Li=16;
    Lii=0;
  }
  return result;
}
