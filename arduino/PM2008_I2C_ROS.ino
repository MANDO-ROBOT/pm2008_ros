#include <pm2008_i2c.h>
#include <MsTimer2.h>
PM2008_I2C pm2008_i2c;
uint8_t ret;
uint16_t tcnt = 1;
void dust(){
  if (ret == 0) {
    Serial.print("pm1p0g:");
    Serial.println(pm2008_i2c.pm1p0_grimm);
    Serial.print("pm2p5g:");
    Serial.println(pm2008_i2c.pm2p5_grimm);
    Serial.print("pm10g:");
    Serial.println(pm2008_i2c.pm10_grimm);
    Serial.print("pm1p0t:");
    Serial.println(pm2008_i2c.pm1p0_tsi);
    Serial.print("pm2p5t:");
    Serial.println(pm2008_i2c.pm2p5_tsi);
    Serial.print("pm10t:");
    Serial.println(pm2008_i2c.pm10_tsi);
    Serial.print("0p3um:");
    Serial.println(pm2008_i2c.number_of_0p3_um);
    Serial.print("0p5um:");
    Serial.println(pm2008_i2c.number_of_0p5_um);
    Serial.print("1um:");
    Serial.println(pm2008_i2c.number_of_1_um);
    Serial.print("2p5um:");
    Serial.println(pm2008_i2c.number_of_2p5_um);
    Serial.print("5um:");
    Serial.println(pm2008_i2c.number_of_5_um);
    Serial.print("10um:");
    Serial.println(pm2008_i2c.number_of_10_um);
  }
  Serial.print("tcnt:");
  Serial.println(tcnt);
  tcnt++;
}
void setup() {
#ifdef PM2008N
  // wait for PM2008N to be changed to I2C mode
  delay(10000);
#endif
  pm2008_i2c.begin();
  Serial.begin(115200);
  pm2008_i2c.command();
  MsTimer2::set(1000, dust);
  MsTimer2::start();
}
void loop() {
  uint8_t ret = pm2008_i2c.read();
}