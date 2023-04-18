int ssa;//needed varible
#include <Sparki.h> // include the sparki library
#include <Servo.h>
void setup()
{
  ssa=0;//needed varible.stands for SPARKI SERVO ANGLE
}
void loop(){
  ssa=0;
  sparki.servo(ssa);
  sparki.clearLCD();
  sparki.println("ssa:   ");
  sparki.print(ssa);
  sparki.updateLCD();
  delay(1000);
  ssa=-50;
  sparki.servo(ssa);
  sparki.clearLCD();
  sparki.println("ssa:   ");
  sparki.print(ssa);
  sparki.updateLCD();
  delay(1000);

}
