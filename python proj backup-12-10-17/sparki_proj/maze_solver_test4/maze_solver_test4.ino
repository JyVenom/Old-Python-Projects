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
  //
    if(edgeLeft<threshold){
      sparki.moveForward();
    }
    if((edgeLeft<threshold)&&(lineLeft<threshold)&&(lineCenter<threshold)&&(lineRight<threshold)&&(edgeRight<threshold)){
      sparki.moveRight(90);
    }
    if((edgeLeft>threshold)&&(lineLeft>threshold)&&(lineCenter>threshold)&&(lineRight>threshold)&&(edgeRight<threshold)){
      sparki.moveLeft(90);
      sparki.moveForward(7.5);
      sparki.moveLeft(90);
    }
    if((edgeLeft<threshold)&&(lineLeft<threshold)&&(lineRight>threshold)){
      sparki.moveLeft(90); // turn left
      sparki.moveForward(9);
      sparki.moveLeft(90); // turn left
    }
    if((edgeLeft>threshold)&&(lineLeft>threshold)&&(lineRight<threshold)&&(edgeRight<threshold)||(edgeLeft<threshold)&&(lineLeft>threshold)&&(lineRight<threshold)&&(edgeRight<threshold)){
      sparki.moveRight(90); // turn right
      sparki.moveForward(9);
      sparki.moveRight(90); // turn right
    }
    if((edgeLeft<threshold)&&(lineLeft<threshold)&&(lineCenter<threshold)&&(lineRight<threshold)){
      sparki.moveRight(90);
    }
    else{
      sparki.moveForward();
    }
  }
