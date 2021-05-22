
#include <Wire.h> 
#include<BleMouse.h> 


const int MPU_addr=0x68;  
int16_t GyY,GyZ;  
int vz, vy, vz_prec, vy_prec; 
int count=0;


BleMouse blhidm("HCM","HCM TEAM",100); 

void setup(){ 
 Serial.begin(115200);  
 Wire.begin();  //Wire for I2C communication
 Wire.beginTransmission(MPU_addr); //Lets commence the transmission to the gyroscope 
 Wire.write(0x6B);  
 Wire.write(0);     
 Wire.endTransmission(true);  
 blhidm.begin(); 
}


void loop(){
 Wire.beginTransmission(MPU_addr);
 Wire.write(0x43);  
 Wire.endTransmission(false);
 Wire.requestFrom(MPU_addr,14,true);  
 //Hexadecimal Mumbo Jumbo coming up
 GyY=Wire.read()<<8|Wire.read();  
 GyZ=Wire.read()<<8|Wire.read(); 
 vz = -(GyZ+100) / 200; //Cleanup
 vy = -(GyY+100 ) / 200;  //Cleanup
 Serial.print(vz); 
 Serial.print(vy);  
 blhidm.move(vz,vy);  
 if ( (vz_prec - 5) <= vz && vz <= vz_prec + 5 && (vy_prec - 5) <= vy && vy <= vy_prec + 5) 
 {
    count++; 
    if (count == 100) 
    { 
      if (!blhidm.isPressed(MOUSE_LEFT))
      {
          blhidm.click(MOUSE_LEFT);
          count = 0;
      }
    }
    else 
    {
      if (blhidm.isPressed(MOUSE_LEFT))
      {
          blhidm.release(MOUSE_LEFT);             }
      }
 }
 else
  {
            vz_prec = vz;
            vy_prec = vy;
            count = 0;
  }
 delay(10);
 }
