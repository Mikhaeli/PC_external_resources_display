#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Connect to LCD via I2C, default address 0x27 (A0-A2 not jumpered)
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2); // Change to (0x27,16,2) for 16x2 LCD.

void setup() {
  // Initiate the LCD:
  lcd.init();
  lcd.backlight();
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  //while (Serial.available()>0) serIn=Serial.read();
  lcd.print("Ready");
}

void loop() {
  //read from serial
  while (Serial.available() > 0) {
    String serial_input = Serial.readStringUntil('\n');//"CPU : 32"; //Serial.readString();
    //lcd.clear();
   // lcd.setCursor(0, 0); // Set the cursor on the first column and first row.
    //lcd.print("Connected"); // Print the string "Hello World!"
    //if (serial_input.length() > 0)
    //{
    lcd.clear();
      //lcd.setCursor(0, 0); // Set the cursor on the first column and first row.
    lcd.print(serial_input); // Print the string "Hello World!"
      //delay(1000);
      //lcd.setCursor(2, 1); //Set the cursor on the third column and the second row (counting starts at 0!).
    //}
  }
}
