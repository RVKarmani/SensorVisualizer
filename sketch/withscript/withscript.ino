#include <MQ2.h>
#include <Wire.h> 

int Analog_Input = A0;
int methane, co, smoke;
MQ2 mq2(Analog_Input);
void setup(){
  Serial.begin(9600);
  mq2.begin();
}
void loop(){
  delay(500);
  float* values= mq2.read(true); //set it false if you don't want to print the values in the Serial
  float methane = mq2.readLPG();
  float co = mq2.readCO();
  float smoke = mq2.readSmoke();
  Serial.print(methane);
  Serial.print(",");
  Serial.print(co);
  Serial.print(",");
  Serial.print(smoke);
  Serial.println();
  delay(1000);
}
