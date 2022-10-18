#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor as cs2,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import ColorSensor as cs1

import functions

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Define the Items
leftMotor = Motor(Port.A)
rightMotor = Motor(Port.B)
armMotor = Motor(Port.C)

gyro = GyroSensor(Port.S1)
colorGround = cs2(Port.S2)
colorFront = cs1(Port.S3)
distanceSensor = UltrasonicSensor(Port.S4)

# Create your objects here.
ev3 = EV3Brick()

# Initialize variables
normalSpeed = 2000
normalTurnSpeed = 500
noTurnSpeed = 0

lineColor = Color.BLACK

# Initialize driveBase
robotBase = DriveBase(leftMotor, rightMotor, 45, 1300)


# Initialize main
def main():
    # functions.lineFollow(robotBase, colorGround)
    functions.robotRotate(gyro, leftMotor, rightMotor)
    

# Run main
main()