
#include<Sparki.h> // include the sparki library
 
//for sensors
int edgeLeft;
int edgeRight;
 
int threshold;
 
//for calibrating
boolean foundLeftWall = false; 
boolean calibrated = false; 
boolean rightWall = false;
 
void setup() 
{
  //indicates to the user that the program started:
  sparki.beep(440, 300);
  delay(300);
  sparki.beep(880, 500);
  Serial.begin(9600);
}
 
void loop() {
  threshold = 700;
 
  readSensors();
 
  calibrateSparki();
 
  //sparki.moveForward();
 
  sparki.clearLCD(); // wipe the screen
 
  sparki.print("Edge Left: "); // show left line sensor on screen
  sparki.println(edgeLeft);
 
  sparki.print("Edge Right: "); // show left line sensor on screen
  sparki.println(edgeRight);
 
  sparki.updateLCD(); // display all of the information written to the screen
}
 
void readSensors()
{
  edgeLeft = sparki.edgeLeft();   // measure the left IR sensor
  edgeRight = sparki.edgeRight(); // measure the left line IR sensor
  //int lineRight  = sparki.lineRight();  // measure the right IR sensor
}
 
void calibrateSparki()
{
  rightWall = false; //variable so we know if Sparki found the right wall
 
  if( foundLeftWall == false &amp;&amp; calibrated == false ) //if Sparki hasn't found a left wall and hasn't been calibrated yet
  {
    sparki.moveLeft(1); //turn Sparki to the left a tiny bit
 
    if ( edgeLeft &lt; threshold ) // if there is a line below left edge sensor
    {
      foundLeftWall = true; //Sparki found the left wall
    }
  }
 
  if( foundLeftWall == true &amp;&amp; calibrated == false ) //if Sparki found a wall but isn't calibrated yet
  {
    if( rightWall == false )
    {
      sparki.motorRotate(MOTOR_LEFT, DIR_CCW, 15); //move forward while rotating to the right a little
      sparki.motorRotate(MOTOR_RIGHT, DIR_CW, 55); //move forward while rotating to the right a little
     }
 
    if( edgeLeft &lt; threshold &amp;&amp; edgeRight &lt; threshold ) //if there is a wall beneath both sensors we're at -30 degrees from the wall
    { //this is also called a "known good" position because we know, no matter where Sparki started, where it is now in relation to the wall
      rightWall = true;
      //turn 28 degrees clockwise and scoot back close to the beginning
      sparki.moveForward();
      delay(1000); //this variable got changed a little
      sparki.moveRight(24); //this variable got changed a little
      sparki.moveBackward();
      delay(1000);
      sparki.motorStop(MOTOR_LEFT);
      sparki.motorStop(MOTOR_RIGHT);
      calibrated = true; //set calibrate flag to true so we exit calibrated code
    }
  }
}
