
#include <Wire.h> //For the I2C communication
#include <DigiMouse.h> //The new bluetooth library


const int MPU_addr=0x68;  // Address of the MPU-6050 using the I2C protocol
int16_t GyY,GyZ;  //Initializing the Gyroscope values
int vz, vy, vz_prec, vy_prec; //Just some random variables you will surely understand if you remember the first one
int count=0;



void setup(){ //Have already Explained :P
 Serial.begin(115200);  //Serial baud rate, Only for debugging ;)
 Wire.begin();  //Wire for I2C communication
 Wire.beginTransmission(MPU_addr); //Lets commence the transmission to the gyroscope B)
 Wire.write(0x6B);  // PWR_MGMT_1 register:- There is a low power mode in MPU which makes it hibernate. We are disabling that
 Wire.write(0);     // set to zero (wakes up the MPU-6050)
 Wire.endTransmission(true);  // Lets stop the transmission now so that other libraries can be initialized
 DigiMouse.begin();  //We have initialized the DigiMouse HID mouse library
}


void loop(){
 Wire.beginTransmission(MPU_addr);
 Wire.write(0x45);  // starting with register 0x43 (GYRO_XOUT_L)
 Wire.endTransmission(false); //Now lets restart the transmission
 Wire.requestFrom(MPU_addr,14);  // request a total of 14 registers
 //Hexadecimal Mumbo Jumbo coming up
 GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
 GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
 vz = -(GyZ + 200) / 200; //Cleanup
 vy = -(GyY-160) / 200;  //Cleanup
 DigiMouse.move(vz,vy);  //Let there be some mouse movement
 DigiMouse.delay(10);
 }
