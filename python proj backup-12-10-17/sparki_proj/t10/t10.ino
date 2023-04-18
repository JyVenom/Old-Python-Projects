#include <Sparki.h> // include the sparki library
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
   int threshold = 650;
   int edgeLeft   = sparki.edgeLeft();   // measure the left edge IR sensor
   int lineLeft   = sparki.lineLeft();   // measure the left IR sensor
   int lineCenter = sparki.lineCenter(); // measure the center IR sensor
   int lineRight  = sparki.lineRight();  // measure the right IR sensor
   int edgeRight  = sparki.edgeRight();  // measure the right edge IR sensor
   if(lineCenter<threshold){
      sparki.moveForward(); // move forward
   }
   else if((lineLeft>threshold)&&(lineCenter>threshold)&&(lineRight<threshold)){
         sparki.moveRight(1); // turn right
   }
   else if((lineLeft<threshold)&&(lineCenter>threshold)&&(lineRight>threshold)){
         sparki.moveLeft(1); // turn left
   }
   else if((edgeLeft>threshold)&&(lineLeft>threshold)&&(lineCenter>threshold)&&(lineRight>threshold)&&(edgeRight>threshold)){
      sparki.moveForward(); // move forward
   }
   else if(edgeLeft<threshold){
      while(lineCenter>threshold){
         sparki.moveLeft(1); // turn left
         lineCenter = sparki.lineCenter();
      }
   }
   else if(edgeRight<threshold){
      while(lineCenter>threshold){
        sparki.moveRight(1); // turn right
        lineCenter = sparki.lineCenter();
      }
   }
   else{
      sparki.moveForward(); // move forward
   }
}
