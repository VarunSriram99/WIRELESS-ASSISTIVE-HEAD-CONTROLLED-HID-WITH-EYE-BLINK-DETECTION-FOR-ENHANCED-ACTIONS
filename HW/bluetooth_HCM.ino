
#include <Wire.h> 
#include<BleMouse.h> 


const int MPU_addr=0x68;  // Address of the MPU-6050 using the I2C protocol
int16_t GyY,GyZ;  //Initializing the Gyroscope values
int vz, vy, vz_prec, vy_prec; 
int count=0;


BleMouse blhidm("HCM","HCM TEAM",100); //Initializing the Bluetooth Low Energy Mouse(HID) with device name, manufacturer name and initial battery level


void setup(){ 
 Serial.begin(115200);  //Serial baud rate
 Wire.begin();  //Wire for I2C communication
 Wire.beginTransmission(MPU_addr); //Lets commence the transmission to the gyroscope 
 Wire.write(0x6B);  // PWR_MGMT_1 register:- There is a low power mode in MPU which makes it hibernate. We are disabling that
 Wire.write(0);     // set to zero (wakes up the MPU-6050)
 Wire.endTransmission(true);  // Lets stop the transmission now so that other libraries can be initialized
 blhidm.begin();  //We have initialized the bluetooth HID mouse library
}


void loop(){
 Wire.beginTransmission(MPU_addr);
 Wire.write(0x43);  // starting with register 0x43 (GYRO_XOUT_L)
 Wire.endTransmission(false); //Now lets restart the transmission
 Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
 //Hexadecimal Mumbo Jumbo coming up
 GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
 GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
 vz = -(GyZ+100) / 200; //Cleanup
 vy = -(GyY+100 ) / 200;  //Cleanup
 Serial.print(vz);  //Just some debugging
 Serial.print(vy);  //Still some debugging
 blhidm.move(vz,vy);  
 if ( (vz_prec - 5) <= vz && vz <= vz_prec + 5 && (vy_prec - 5) <= vy && vy <= vy_prec + 5) //Are you really moving your head?
 {
    count++; //To keep track of how much time your head was still
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
