#include <Sparki.h> // include the sparki library
  int x;
  int z;
  int t;
  int y;
  int x1;
void setup() 
{
  t=1;
  y=1;
  z=1;
  x1=1;
}
 
void loop() {
  int threshold = 650;
  int edgeLeft   = sparki.edgeLeft();   // measure the left edge IR sensor
  int lineLeft   = sparki.lineLeft();   // measure the left IR sensor
  int lineCenter = sparki.lineCenter(); // measure the center IR sensor
  int lineRight  = sparki.lineRight();  // measure the right IR sensor
  int edgeRight  = sparki.edgeRight();  // measure the right edge IR sensor
 
  if (( lineLeft > threshold )&&( lineRight < threshold )) // if line is below left line sensor
  {
    x=1;
    sparki.moveForward(1); // turn right
    while (( lineLeft > threshold )&&( lineRight < threshold )){
       sparki.moveRight(10); // turn right
       sparki.RGB(0,50,50);
       if (~(( lineLeft > threshold )&&( lineRight < threshold )))
          break;
   }
  }

  else if (( lineRight > threshold )&&( lineLeft < threshold )) // if line is below right line sensor
  {
    x=2;
    sparki.moveForward(1); // turn right
    while (( lineRight > threshold )&&( lineLeft < threshold )){
       sparki.moveLeft(10); // turn left
       sparki.RGB(0,0,50);
       if (~(( lineRight > threshold )&&( lineLeft < threshold )))
          break;
    }
  }

/*else if (( lineCenter < threshold)&&( lineLeft > threshold)&&( lineRight > threshold))
  {
    x=3;
    sparki.moveLeft(); // move forward
    //sparki.RGB(50,0,50);
  }  
  // if the center line sensor is the only one reading a line*/
  else if ((( lineCenter < threshold)&&(lineRight < threshold)&&(lineLeft > threshold))||(( lineCenter < threshold)&&(lineRight > threshold)&&(lineLeft < threshold))||(( lineCenter < threshold)&&(lineRight < threshold)&&(lineLeft < threshold)))
  {
    x=4;
    sparki.moveForward(); // move forward
    sparki.RGB(50,0,50);
  }  

  
/*  else if ((lineCenter < threshold)&&( edgeRight < threshold ))
  {
    x=5;
     sparki.moveForward(20); // move forward
     sparki.moveRight(135); // turn right
  }  
  else if ((lineCenter < threshold)&&(lineLeft < threshold)&&(lineRight < threshold)&&(y==1)){
    x=6;
    sparki.moveRight(15); // turn right
    y=2;
}
  else if ((lineCenter < threshold)&&(lineLeft < threshold)&&(lineRight < threshold)&&(y==2)){
    x=7;
    sparki.moveLeft(15); // turn right
    y=1;
}*/
else{
  if(x1==1){
     sparki.moveForward(1);
     x1=2;
  }
  x=8;
  sparki.moveRight(1); // turn right
  z=z+1;
 // sparki.clearLCD(); // wipe the screen
//  sparki.print("z=  ");
//  sparki.println(z);
 // sparki.updateLCD(); // display all of the information written to the screen
  while(z==160){
    sparki.moveLeft(1); // turn right
    //delay(3000);
    t=t+1;
  sparki.clearLCD(); // wipe the screen
  sparki.print("t calibration=  ");
  sparki.println(t);
  sparki.print("line center= ");
  lineCenter = sparki.lineCenter();
  sparki.println(lineCenter);
  sparki.updateLCD(); // display all of the information written to the screen
  //
   //lineCenter = sparki.lineCenter(); 
  if (lineCenter < 600){//threshold){
    //while(1){}
    z=1;
    x1=1;
    t=1;
    //sparki.clearLCD(); // wipe the screen
    //sparki.print("we are here");
    //sparki.updateLCD(); // display all of the information written to the screen
    break;   
 }
    if(t==360){
      t=1;
      z=1;
      x1=1;
      break;
    }
  }
}

  sparki.clearLCD(); // wipe the screen
  sparki.println();

  sparki.print("case:  ");
  sparki.println(x);
  
  sparki.print("z calibration=  ");
  sparki.println(z);

//  sparki.print("Edge Left:  ");
//  sparki.println(edgeLeft);

  sparki.print("Line Left: "); // show left line sensor on screen
  sparki.println(lineLeft);
 
  sparki.print("Line Center: "); // show center line sensor on screen
  sparki.println(lineCenter);
 
  sparki.print("Line Right: "); // show right line sensor on screen
  sparki.println(lineRight);
  
//  sparki.print("Edge Right:  ");
//  sparki.println(edgeRight);
  
  sparki.println();
  sparki.updateLCD(); // display all of the information written to the screen
 
  delay(100); // wait 0.1 seconds
}

