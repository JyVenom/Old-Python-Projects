#include <Sparki.h> // include the sparki library
  int x;
  int z;
  int t;
  int y;
  int x1;
void setup() {
  // put your setup code here, to run once:
  t=1;
  y=1;
  z=1;
  x1=1;
  x=0;
}

void loop() {
  // put your main code here, to run repeatedly:
  int threshold = 650;
  int edgeLeft   = sparki.edgeLeft();   // measure the left edge IR sensor
  int lineLeft   = sparki.lineLeft();   // measure the left IR sensor
  int lineCenter = sparki.lineCenter(); // measure the center IR sensor
  int lineRight  = sparki.lineRight();  // measure the right IR sensor
  int edgeRight  = sparki.edgeRight();  // measure the right edge IR sensor
sparki.clearLCD(); // wipe the screen
 /* if( lineCenter < threshold){
    x=4;
    sparki.moveForward(); // move forward
    sparki.RGB(50,0,50);
    sparki.print("case1");
  }  */
  /*if(x1==1){
     sparki.moveForward(1);
     x1=2;
  }*/
  if((lineLeft > threshold)&&(lineCenter > threshold)|| ( lineCenter > threshold)&&(lineRight > threshold)){
  sparki.moveRight(1); // turn right
  z=z+1;
  if((lineLeft < threshold)&&(lineCenter > threshold)&&(lineRight > threshold)){
    sparki.moveRight(10);
  }
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
  sparki.print("case2");
  sparki.updateLCD(); // display all of the information written to the screen
  //
   lineCenter = sparki.lineCenter(); 
  if (lineCenter < threshold){
    lineCenter = sparki.lineCenter();
    z=1;
    x1=1;
    t=1;
    sparki.moveForward(1);
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
  if(lineCenter <threshold && lineRight <threshold){
    while(x<90){
      sparki.moveRight(1); // turn right
      x+=1;
      if(lineLeft < threshold){
        sparki.moveForward(1);
      }
    }
  }
  else {
    sparki.moveForward(1);
  }
  sparki.updateLCD(); // display all of the information written to the screen
}
