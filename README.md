# PM2008 ROS Package

## Dependencies
```
$ sudo apt install ros-noetic-rosserial ros-noetic-rosserial-arduino
```

## Usage
```
$ roslaunch pm2008_ros pm2008.launch
```

## Topic info
### topic name : /pm2008
```
pm1p0g : PM1.0 concentration, unit: ㎍/㎥, GRIMM  
pm2p5g : PM2.5 concentration, unit: ㎍/㎥, GRIMM  
pm10g : PM10 concentration, unit: ㎍/㎥, GRIMM  
pm1p0t : PM1.0 concentration, unit: ㎍/㎥, TSI  
pm2p5t : PM2.5 concentration, unit: ㎍/㎥, TSI  
pm10t : PM10 concentration, unit: ㎍/㎥, TSI  
n0p3um : Number of 0.3 ㎛, unit: pcs/0.1L  
n0p5um : Number of 0.5 ㎛, unit: pcs/0.1L  
n1um : Number of 1 ㎛, unit: pcs/0.1L  
n2p5um : Number of 2.5 ㎛, unit: pcs/0.1L  
n5um : Number of 5 ㎛, unit: pcs/0.1L  
n10um : Number of 10 ㎛, unit: pcs/0.1L  
tcnt : time count(1 sec)  
```

## Arduino
if you want to change sensor data fix arduino/PM2008_I2C_ROS.ino