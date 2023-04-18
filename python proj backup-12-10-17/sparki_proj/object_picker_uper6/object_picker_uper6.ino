int x;//need still
int y;//need still
int ssa;//needed varible
int my_case;
int oma;
int ola = 0;
int ora = 0;
int oda;
int oma2;
int cm;
int count=0;
int sum=0;
int dist[80];
int i;
int ang[80];
#include <Sparki.h> // include the sparki library
void setup()
{
  ssa = -1; //needed varible.stands for SPARKI SERVO ANGLE
  sparki.servo(SERVO_CENTER); // rotate the servo to is 0 degree postion (forward)
  delay(1000);
  sparki.gripperClose(5); // close the robot's gripper
  delay(7000);
  x = 1; //need still
  y = 1; //need still
}

void loop()
{
  int threshold = 650;
  int edgeLeft   = sparki.edgeLeft();   // measure the left edge IR sensor
  int lineLeft   = sparki.lineLeft();   // measure the left IR sensor
  int lineCenter = sparki.lineCenter(); // measure the center IR sensor
  int lineRight  = sparki.lineRight();  // measure the right IR sensor
  int edgeRight  = sparki.edgeRight();  // measure the right edge IR sensor
  int code = sparki.readIR();

  if(code != -1){
    sparki.print("Received code: ");
    sparki.println(code);
  }

  switch(code){
    
  // Movement buttons
  case 70: sparki.moveForward(); break;
  case 21: sparki.moveBackward(); break;
  case 67: 
  case 71: sparki.moveRight(); break;
  case 68:
  case 69: sparki.moveLeft(); break;
  case 64: sparki.moveStop(); 
           sparki.gripperStop();
           delay(15000);
           break;

  // Gripper Buttons
  case 9:  sparki.gripperOpen(); break;
  case 7:  sparki.gripperClose(); break;

  // buzzer
  case 74: sparki.beep(); break;

  // Servo
  case 90: sparki.servo(SERVO_LEFT); break;
  case 28: sparki.servo(SERVO_CENTER); break;
  case 8: sparki.servo(SERVO_RIGHT); break;

  // RGB LED
  case 25: sparki.RGB(RGB_OFF); break;
  case 12: sparki.RGB(RGB_RED); break;
  case 24: sparki.RGB(RGB_GREEN); break;
  case 94: sparki.RGB(RGB_BLUE); break;
  
  default:
  break;
  }

  sparki.clearLCD();

  cm = sparki.ping(); // measures the distance with Sparki's eyes
  sparki.print("Distance: ");
  sparki.print(cm); // tells the distance to the computer
  sparki.println(" cm; ");
  sparki.println("ssa:   ");
  sparki.print(ssa);
  sparki.println("my_case:   ");
  sparki.print(my_case);
  //ssa=-1deg-> ssa-- -> -80deg,ssa=+1deg-> ssa++ ->  +80deg -> ssa=1deg ...
  if ((cm > 7.5) && (ssa <= 0) && (ssa >- 80)) { //cm==7cm when detected obj
    sparki.servo(ssa);
    ssa = ssa - 2;
    my_case = 1;
  } else if (ssa <= 80) {
    ssa = 1;
    sparki.servo(ssa);
    my_case = 2;
  } else if ((cm > 7.5) && (ssa <= 80) && (ssa > 0)) {
    sparki.servo(ssa);
    ssa = ssa + 2;
    my_case = 3;
  } else if (ssa >= 80) {
    ssa = -1;
    sparki.servo(ssa);
    my_case = 4;
  }
  //

  if (cm < 10) {
    my_case = 5;
  }
  if ((cm != -1) && (y == 1) && ((ssa == -1) || (ssa == 1))) // make sure its not too close or too far
  {
    if ((cm == 7) || (cm == 6)) // if the distance measured is less than 10 centimeters
    {
      my_case = 6;
      sparki.clearLCD();
      sparki.println("object found");
      cm = sparki.ping(); // measures the distance with Sparki's eyes
      sparki.print("Distance: ");
      sparki.print(cm); // tells the distance to the computer
      sparki.println(" cm; ");

      sparki.updateLCD();
      delay(300);
      sparki.beep(880, 500);
      sparki.moveStop();
      delay(1000);
      sparki.gripperOpen(5);  // open the robot's gripper
      delay(5000);
      //delay(5000);           // for 5 second (5000 milliseconds)
      sparki.moveForward(13);
      delay(5000);

      sparki.gripperClose(); // close the robot's gripper
      delay(5000);           // for 5 second (5000 milliseconds)


      sparki.gripperStop();  // stop the grippers from moving
      delay(1000);           // for 1 second (1000 milliseconds)
      y = 2;
    }
  }
  if ((cm != -1) && (y == 1) && (ssa > 0)) // make sure its not too close or too far
  {
    if ((cm == 7) || (cm == 6)) // if the distance measured is less than 7.5 centimeters
    {
      sparki.clearLCD();
      sparki.println("object found");
      //cm = sparki.ping(); // measures the distance with Sparki's eyes
      sparki.print("Distance: ");
      sparki.print(cm); // tells the distance to the computer
      sparki.println(" cm; ");
      sparki.updateLCD();
      my_case = 7;
      delay(1000);
      sparki.moveStop();
      while ((cm < 7.5) && (ola == 0)) { // if the distance measured is less than 7.5 centimeters
        cm = sparki.ping(); // measures the distance with Sparki's eyes
        sparki.servo(ssa);
        ola = ssa;
        ssa = ssa - 1;
        sparki.clearLCD();
        sparki.print("Distance: ");
        sparki.print(cm); // tells the distance to the computer
        sparki.println(" cm; ");
        sparki.println("ssa:   ");
        sparki.print(ssa);
        sparki.updateLCD();
        sparki.ping();
        if (cm > 7.5) {
          ola = ola - 1;
          ssa = ssa - 1;
          sparki.servo(ssa);
          break;
        }
      }
      while ((cm < 7.5) && (ora == 0)) { // if the distance measured is less than 7.5 centimeters
        cm = sparki.ping(); // measures the distance with Sparki's eyes
        ssa + 1;
        sparki.servo(ssa);
        ora = ssa;
        sparki.clearLCD();
        sparki.print("Distance: ");
        sparki.print(cm); // tells the distance to the computer
        sparki.println(" cm; ");
        sparki.println("ssa:   ");
        sparki.print(ssa);
        sparki.updateLCD();
        sparki.ping();
        if (cm > 7.5) {
          oma = ora - ola;
          oma = oma / 2;
          oma = oma + ola;
          ora = 0;
          ola = 0;
          oma = oma + 15;
          break;
        }
      }
      sparki.moveRight(oma);
      /*          sparki.moveBackward(5);
                ssa=ssa-5;
                sparki.moveRight(ssa);
                sparki.servo(SERVO_CENTER); // rotate the servo to is 0 degree postion (forward)
                delay(1000);
                sparki.clearLCD();
                sparki.println("object found");
                sparki.updateLCD();
                delay(300);*/
      sparki.beep(880, 500);
      sparki.moveStop();
      delay(1000);
      sparki.gripperOpen(5);  // open the robot's gripper

      //delay(5000);           // for 5 second (5000 milliseconds)
      sparki.moveForward(7);
      delay(5000);

      sparki.gripperClose(); // close the robot's gripper
      delay(5000);           // for 5 second (5000 milliseconds)

      sparki.gripperStop();  // stop the grippers from moving
      delay(1000);           // for 1 second (1000 milliseconds)
      y = 2;
      oma = 0;
    }
  }
  if ((cm != -1) && (y == 1) && (ssa < 0)) // cm!=-1:make sure its not too close or too far, y==1: not picked up object, ==2 picked up obj, ssa: servo sound angle.
  {
    if ((cm == 7) || (cm == 6)) // if the distance measured is less than 7.5 centimeters
    {
      
      oda=ssa;
      sparki.moveStop();
      //delay(180000);
      sparki.clearLCD();
      sparki.println("object found");
      // cm = sparki.ping(); // measures the distance with Sparki's eyes
      sparki.print("Distance: ");
      sparki.print(cm); // tells the distance to the computer
      sparki.println(" cm; ");
      sparki.updateLCD();
      my_case = 8;
      delay(1000);
      sparki.moveStop();
      angle_calib();//yifengy2
      sparki.moveLeft(oma);
      delay(1000);
      //oma2 = ola - ora;
      //oma2 = oma2 / 2;
      //oma2 = oma2 + ora;
      sparki.clearLCD();
      sparki.print("ora: ");
      sparki.print(ora); // tells the distance to the computer
      sparki.println("ola:   ");
      sparki.print(ola);
      sparki.println("oma:   ");
      sparki.print(oma);
      sparki.updateLCD();
      sparki.moveStop();
      //delay(600000);
      /*          sparki.moveBackward(5);
                ssa=ssa+5;
                sparki.moveLeft(-ssa);
                sparki.servo(SERVO_CENTER); // rotate the servo to is 0 degree postion (forward)
                sparki.clearLCD();
                sparki.println("object found");
                sparki.updateLCD();
                delay(300);*/
      sparki.beep(880, 500);
      sparki.moveStop();
      delay(1000);
      sparki.gripperOpen(5);  // open the robot's gripper

      delay(5000);           // for 5 second (5000 milliseconds)
      sparki.moveForward(13);
      delay(5000);

      sparki.gripperClose(); // close the robot's gripper
      delay(5000);           // for 5 second (5000 milliseconds)

      sparki.gripperStop();  // stop the grippers from moving
      delay(1000);           // for 1 second (1000 milliseconds)
      y = 2;
      oma = 0;
      ora = 0;
      ola = 0;
      oma2=0;
    }
  }


  if ((lineCenter < threshold) && (lineLeft < threshold) && (lineRight < threshold) && (y == 2))
  {
    my_case = 9;
    sparki.clearLCD();
    sparki.println("object disposed");
    sparki.updateLCD();
    sparki.moveBackward(5);
    sparki.gripperOpen(5);  // open the robot's gripper
    //delay(3000);           // for 3 second (3000 milliseconds)
    sparki.moveBackward(5);
    sparki.gripperClose(); // close the robot's gripper
    delay(10000);           // for 3 second (3000 millisecond
    sparki.gripperStop();  // stop the grippers from moving
    delay(1000);           // for 1 second (1000 milliseconds)
    sparki.moveRight(90);
    sparki.moveForward(10);
    sparki.moveLeft(90);
    sparki.moveForward(1);
    y = 1;
  }
  if ((lineCenter < threshold) && (lineLeft < threshold) && (lineRight < threshold) && (x == 1))
  {
    my_case = 10;
    sparki.moveRight(90);
    sparki.moveForward(3);
    sparki.moveRight(90);
    sparki.moveForward(1);
    sparki.lineLeft();   // measure the left IR sensor
    sparki.lineCenter(); // measure the center IR sensor
    sparki.lineRight();  // measure the right IR sensor
    x = 2;
  }
  else if ((lineCenter < threshold) && (lineLeft < threshold) && (lineRight < threshold) && (edgeLeft > threshold) && (edgeRight > threshold) && (x == 2))
  {
    my_case = 11;
    sparki.moveLeft(90);
    sparki.moveForward(3);
    sparki.moveLeft(90);
    sparki.moveForward(1);
    sparki.lineLeft();   // measure the left IR sensor
    sparki.lineCenter(); // measure the center IR sensor
    sparki.lineRight();  // measure the right IR sensor
    x = 1;
  }
  if ((lineCenter > threshold) && (lineLeft > threshold) && (lineRight > threshold))
  {
    my_case = 12;
    sparki.moveForward();
  }


  sparki.updateLCD();
  delay(100); // wait 0.1 seconds (100 milliseconds)
}

void angle_calib(){
      cm = sparki.ping(); // measures the distance with Sparki's eyes
      sparki.clearLCD();
      sparki.print("calibration start!!!!!! delay 1s center\n");
      sparki.println("ssa:   ");
      sparki.print(ssa);
      sparki.println("cm:   ");
      sparki.print(cm);
      sparki.updateLCD();
      delay(3000);//jerry040216
      ssa=-1;
      sparki.servo(ssa);
      //while ((cm < 7.5) && (ora == 0)) { // if the distance measured is less than 7.5 centimeters
/*      while (1) { // if the distance measured is less than 7.5 centimeters
        cm = sparki.ping(); // measures the distance with Sparki's eyes
        ssa = ssa + 1;
        sparki.servo(ssa);
        ora = ssa;
        sparki.clearLCD();
        sparki.print("Distance: ");
        sparki.print(cm); // tells the distance to the computer
        sparki.println(" cm; ");
        sparki.println("ssa:   ");
        sparki.print(ssa);
        sparki.updateLCD();
        sparki.ping();
        if (cm > 7.5) {
          sparki.clearLCD();
          sparki.print("screen right done\n");
          sparki.println("ora:   ");
          sparki.print(ora);
          sparki.println("cm:   ");
          sparki.print(cm);
          sparki.updateLCD();
          
          delay(10000);
          ora = ora - 1;
          ssa = ssa - 2;
          sparki.servo(ssa);
          break;
        }
      }*/
      //while ((cm < 7.5) && (ola == 0)) { // if the distance measured is less than 7.5 centimeters
      while (ssa >= -80) { // if the distance measured is less than 7.5 centimeters
        cm = sparki.ping(); // measures the distance with Sparki's eyes
        ssa = ssa - 1;
        sparki.servo(ssa);
        ola = ssa;
        sparki.clearLCD();
        sparki.print("Distance: ");
        sparki.print(cm); // tells the distance to the computer
        sparki.println(" cm; ");
        sparki.println("ssa:   ");
        sparki.print(ssa);
        sparki.updateLCD();
        delay(3000);//jerry040216
        sparki.ping();     }         
        //if (cm > 7.5) {
        /*jerry040216if(cm(ssa) > 7.5){
          cm(ssa)=0;
        }
        else if(cm(ssa) < 7.5){
          cm(ssa)=1;
          count=count+1;
          sum=sum+ssa;
        }
        if (cm == 80) {
          avg=sum/count;
          break;
        }
      }*/
      /*jerry040216,for(i=0;i<=80;i++){
        ang[i]=ssa;
        dist[i]=sparki.ping();
        if(dist[i]>7.5){
          ang[i]=0;
        }
        if(dist[i]<7.5){
          sum+=ang[i];
          count+=1;
        }
        if(i==80){
          oma=sum/count;
        }
        ssa-=1;
        sparki.servo(ssa);
      }*/
/*        sparki.clearLCD();
        sparki.print("calib DONE!!! left angle=");
        sparki.print(ola); // tells the distance to the computer
        sparki.print("right angle=");
        sparki.print(ora); // tells the distance to the computer
        sparki.updateLCD();
        delay(600000);//yifengy,
        ola=0;
        ora=0;*/
}
