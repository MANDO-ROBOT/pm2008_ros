#!/usr/bin/env python3
import rospy
import serial
from pm2008_ros.msg import pm2008

def pm2008_publisher():
    
    rospy.init_node('pm2008', anonymous=True)

    serial_port = "/dev/ttyACM0"
    serial_baudrate = 115200

    try:
        ser = serial.Serial(serial_port, serial_baudrate)
    except serial.SerialException as e:
        rospy.logerr("Failed to open serial port: %s", str(e))
        return

    pub   = rospy.Publisher('pm2008', pm2008, queue_size=10)
    rate = rospy.Rate(20) 
    msg = pm2008()
    pcnt = 0

    while not rospy.is_shutdown():
        try:
            serial_data_bytes = ser.readline().strip()
            serial_data = serial_data_bytes.decode('utf-8')

            rospy.loginfo("%s",serial_data)
            parts = serial_data.split(':')

            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()

                if(key == "pm1p0g"): msg.pm1p0g = int(value); pcnt=pcnt+1
                elif(key == "pm2p5g"): msg.pm2p5g = int(value); pcnt=pcnt+1
                elif(key == "pm10g"): msg.pm10g = int(value); pcnt=pcnt+1
                elif(key == "pm1p0t"): msg.pm1p0t = int(value); pcnt=pcnt+1
                elif(key == "pm2p5t"): msg.pm2p5t = int(value); pcnt=pcnt+1
                elif(key == "pm10t"): msg.pm10t = int(value); pcnt=pcnt+1
                elif(key == "0p3um"): msg.n0p3um = int(value); pcnt=pcnt+1
                elif(key == "0p5um"): msg.n0p5um = int(value); pcnt=pcnt+1
                elif(key == "1um"): msg.n1um = int(value); pcnt=pcnt+1
                elif(key == "2p5um"): msg.n2p5um = int(value); pcnt=pcnt+1
                elif(key == "5um"): msg.n5um = int(value); pcnt=pcnt+1
                elif(key == "10um"): msg.n10um = int(value); pcnt=pcnt+1
                elif(key == "tcnt"): msg.tcnt = int(value); pcnt=pcnt+1
                else:
                    rospy.INFO("No matched serial data!!!")

            if pcnt == 13:
                pub.publish(msg)
                pcnt = 0

        except serial.SerialException as e:
            rospy.logerr("Serial communication error: %s", str(e))

        rate.sleep()

if __name__ == '__main__':
    try:
        pm2008_publisher()
    except rospy.ROSInterruptException:
        pass
