#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor as ColorSensor2,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import ColorSensor as ColorSensor1
import functions
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Define the Items
leftMotor = Motor(Port.A)
rightMotor = Motor(Port.B)
armMotor = Motor(Port.C)
gyro = GyroSensor(Port.S1)
colorGround = ColorSensor2(Port.S2)
colorFront = ColorSensor1(Port.S3)
distanceSensor = UltrasonicSensor(Port.S4)

# Create your objects here.
ev3 = EV3Brick()

# Initialize driveBase
robotBase = DriveBase(leftMotor, rightMotor, 55.5, 105)
gyro.reset_angle(0)


# Initialize main
def main():

    stationCount = 0
    holding = True

    while True:
        print(colorFront.color())
        functions.lineFollow(robotBase, colorGround)
        
        if colorGround.color() == Color.GREEN:
            robotBase.straight(-110)
            functions.rotationByLine(colorGround, robotBase, 30, 1, Color)
            robotBase.drive(0, 12)
            sleep(0.9)

        if colorGround.color() == Color.BLACK:
            robotBase.straight(-110)
            functions.rotationByLine(colorGround, robotBase, 30, -1, Color)
            robotBase.drive(0, 12)
            sleep(0.9)
        
        if colorGround.color() == Color.RED:
            robotBase.drive(0,0)
            robotBase.straight(-110)
            functions.robotRotate(gyro, robotBase, 30, -90)
            robotBase.straight(-100)

            if holding == True:
                holding = False
                armMotor.run_time(-200, 5000, wait=True)
            
            elif holding == False:
                holding = True
                armMotor.run_time(200, 5000, wait=True)
            
            robotBase.straight(100)
            functions.robotRotate(gyro, robotBase, 30, 90)

        if colorGround.color() == Color.RED:
            functions.stationCounter(colorFront, robotBase, gyro, armMotor, stationCount)
            stationCount += 1

        if colorGround.color() == Color.RED:
            functions.stationCounter(colorFront, robotBase, gyro, armMotor, stationCount)
            stationCount += 1

# Run main2
main()