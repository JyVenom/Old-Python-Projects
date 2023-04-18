#include <Sparki.h>
int x;
void setup() {
  // put your setup code here, to run once:
 sparki.clearLCD();
}

void loop() {
  // put your main code here, to run repeatedly:
for(x=0;x<3;x++){
sparki.beep(1);
delay(100);
}
delay(2000);
}
