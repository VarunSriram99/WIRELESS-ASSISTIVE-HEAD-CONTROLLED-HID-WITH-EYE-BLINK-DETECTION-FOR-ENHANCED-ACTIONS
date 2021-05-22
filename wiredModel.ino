
#include <Wire.h> 
#include <DigiMouse.h> 


const int MPU_addr=0x68; 
int16_t GyY,GyZ; 
int vz, vy, vz_prec, vy_prec; 
int count=0;



void setup(){ 
 Serial.begin(115200); 
 Wire.begin();  
 Wire.beginTransmission(MPU_addr); 
 Wire.write(0x6B);  
 Wire.write(0);    
 Wire.endTransmission(true); 
 DigiMouse.begin();  
}


void loop(){
 Wire.beginTransmission(MPU_addr);
 Wire.write(0x45);  
 Wire.endTransmission(false); 
 Wire.requestFrom(MPU_addr,14);  

 GyY=Wire.read()<<8|Wire.read();  
 GyZ=Wire.read()<<8|Wire.read();  
 vz = -(GyZ + 200) / 200; 
 vy = -(GyY-160) / 200;  
 DigiMouse.move(vz,vy); 
 DigiMouse.delay(10);
 }
