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
colorGround = ColorSensor2(Port.S3)
colorFront = ColorSensor1(Port.S2)
distanceSensor = UltrasonicSensor(Port.S4)

# Create your objects here.
ev3 = EV3Brick()

# Initialize driveBase
robotBase = DriveBase(leftMotor, rightMotor, 55.5, 105)
gyro.reset_angle(0)

# Initialize main
def main():
   
    # Initialize variables
    stationCount = 0
    holding = False
    holdingColor = ""
    returnList = []

    stations = {
        0 : None,
        1 : Color.GREEN,
        2 : Color.RED,
        3 : Color.BLUE
    }

    # Maak de arm van de robot open voor het begin
    armMotor.run_until_stalled(-200, duty_limit=90)

    while True:
        # Functie lijn volgen
        functions.lineFollow(robotBase, colorGround)

        # Rechts afslaan bij het zien van Groen
        if colorGround.color() == Color.GREEN:
            robotBase.straight(-130)
            functions.rotationByLine(colorGround, robotBase, 30, 1, Color)
            robotBase.drive(0, 12)
            sleep(0.9)
            robotBase.straight(30)

        # Links afslaan bij het zien van Zwart
        if colorGround.color() == Color.BLACK:
            robotBase.straight(-100)
            functions.rotationByLine(colorGround, robotBase, 30, -1, Color)
            robotBase.drive(0, 12)
            sleep(0.9)
            robotBase.straight(30)

        # Functie Station
        if colorGround.color() == Color.RED:
            returnList = functions.stationCounter(colorFront, robotBase, gyro, armMotor,
                                        stationCount, holding, holdingColor, stations, distanceSensor, Color)
            
            holding = returnList[0]
            holdingColor = returnList[1]

            stationCount += 1
            if stationCount >= len(stations):
                stationCount = 0
            
# Run main2
main()