#include <Sparki.h> // include the sparki library
int x=0;
int y=1;
void setup() 
{
}

void loop() {
  //Threshold is the value that helps you determine what's black and white.  
  //Sparki's library indicates white as close to 900, black is around 200.
  //I'm using a threshold of 400 for the example, but if you have a narrow line, or perhaps a lighter black, you may 
  //Need to adjust.
  int threshold = 900;
  sparki.RGB(RGB_OFF); // Make the LED white (all colors)
  int edgeLeft   = sparki.edgeLeft();   // measure the left edge IR sensor
  int lineLeft   = sparki.lineLeft();   // measure the left IR sensor
  int lineCenter = sparki.lineCenter(); // measure the center IR sensor
  int lineRight  = sparki.lineRight();  // measure the right IR sensor
  int edgeRight  = sparki.edgeRight();  // measure the right edge IR sensor
  
  if (( lineLeft > threshold )&&( lineRight < threshold )) // if line is below left line sensor
  {
    x=1;
    sparki.moveForward(1); // turn right
    sparki.moveRight(7); // turn right
    sparki.RGB(0,50,50);
  }

  else if (( lineRight > threshold )&&( lineLeft < threshold )) // if line is below right line sensor
  {
    x=2;
    sparki.moveForward(1); // turn right
    sparki.moveLeft(7); // turn left
    sparki.RGB(0,0,50);
  }

else if (( lineCenter < threshold)&&( lineLeft > threshold)&&( lineRight > threshold))
  {
    x=3;
    sparki.moveLeft(); // move forward
    //sparki.RGB(50,0,50);
  }  
  // if the center line sensor is the only one reading a line
  else if ((( lineCenter < threshold)&&(lineRight < threshold)&&(lineLeft > threshold))||(( lineCenter < threshold)&&(lineRight > threshold)&&(lineLeft < threshold))||(( lineCenter < threshold)&&(lineRight < threshold)&&(lineLeft < threshold)))
  {
    x=4;
    sparki.moveForward(); // move forward
    sparki.RGB(50,0,50);
  }  
/*  if (( lineCenter < threshold)&&(edgeRight < threshold))
  {
    sparki.moveRight(); // move forward
  }  
/*  if (( lineCenter < threshold)&&(edgeLeft < threshold))
  {
    sparki.moveLeft(); // move forward
  }
  if (( lineCenter < threshold)&&(edgeRight < threshold)&&(edgeLeft < threshold))
  {
    sparki.moveRight(); // move forward
  } */ 
    else if (( lineLeft > threshold )&&( lineRight > threshold )&&( lineCenter > threshold)&&(y==1)) // if line is below left line sensor
  {  
      sparki.RGB(50,0,0); // Make the LED maximum Red
      sparki.moveRight(135); // turn right
      //while (1){ }//jry
      x=5;
      y=y+1;
      sparki.RGB(RGB_OFF); // Make the LED white (all colors)
  }
    else if (( lineLeft > threshold )&&( lineRight > threshold )&&( lineCenter > threshold)&&(y==2)) // if line is below left line sensor
  {  
      sparki.RGB(50,50,0); // Make the LED maximum Red
      sparki.moveRight(180); // turn right
      /*delay(3000);
       sparki.moveRight(180); // turn right
    while (1){ }//jry*/
      x=6;
      y=y+1;
        /*sparki.clearLCD(); // wipe the screen

   //   sparki.RGB(RGB_OFF); // Make the LED white (all colors)
      sparki.print("case:   ");
      sparki.println(x);
        sparki.updateLCD(); // display all of the information written to the screen*/
      //while(1){}
  }
    else if (( lineLeft > threshold )&&( lineRight > threshold )&&( lineCenter > threshold)&&(y==3)) // if line is below left line sensor
  { 
      sparki.RGB(0,50,0); // Make the LED maximum Green
      sparki.moveLeft(135); // turn left
      x=7;
      y=y+1;
      //sparki.RGB(RGB_OFF); // Make the LED white (all colors)
  }
// else 
  //   x=7;
    else if (( lineLeft > threshold )&&( lineRight > threshold )&&( lineCenter > threshold)&&(y==4)) // if line is below left line sensor
  {  
      sparki.RGB(50,50,50); // Make the LED maximum Red
      sparki.moveLeft(140); // turn right
      //while (1){ }//jry
      x=8;
      y=1;
      sparki.RGB(RGB_OFF); // Make the LED white (all colors)
  }

  
  sparki.clearLCD(); // wipe the screen
  


  // write the measurements to the screen
 sparki.print("case:   ");
 sparki.println(x);//jerry,edgeLeft);
 
  sparki.println();

  sparki.print("Line Left:   ");
  sparki.println(lineLeft);
  
  sparki.print("Line Center: ");
  sparki.println(lineCenter);
  
  sparki.print("Line Right:  ");
  sparki.println(lineRight);
  
  sparki.println();
  
  sparki.print("Edge Right:  ");
  sparki.println(edgeRight);
  
  sparki.updateLCD(); // display all of the information written to the screen
  delay(100); // wait 0.1 seconds
}


