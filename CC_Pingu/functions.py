from time import sleep

def lineFollow(robot, colorGround):
    speed = -50
    rotationSpeed = -1
    percentageStraight = 50

    rotation = colorGround.reflection() - percentageStraight
    robot.drive(speed, rotationSpeed * rotation)

def robotRotate(gyro, robotBase, speed, rotationTarget):
    newRotationTarget = gyro.angle()
    gyro.reset_angle(0)

    if rotationTarget < 0:
        while gyro.angle() > rotationTarget:
           robotBase.drive(0, speed)

    elif rotationTarget > 0:
        while gyro.angle() < rotationTarget:
            robotBase.drive(0, -speed)

    robotBase.drive(0,0)
    print(gyro.angle())

def rotationByLine(colorGround, robotBase, speed, rotationTarget, Color):

    if rotationTarget < 0:
        while True:
            robotBase.drive(0, speed)
            if colorGround.color() == Color.BLUE:
                break        
    elif rotationTarget > 0:
        while True:
            robotBase.drive(0, -speed)
            if colorGround.color() == Color.BLUE:
                break

def stationCounter(colorFront, robotBase, gyro, armMotor,
                    stationCount, holding, holdingColor, stations, distanceSensor, Color):
    
    
    if stationCount == 0:
        if holding == False:
            # Benaderen van het item
            robotBase.drive(0,0)
            robotBase.straight(-110)
            robotRotate(gyro, robotBase, 30, -90)

            # Checken aanwezigheid van item
            while distanceSensor.distance() >= 200:
                pass

            # Pakken van item
            robotBase.reset()
            while distanceSensor.distance() >= 50:
                print(holdingColor)
                print(distanceSensor.distance())

                robotBase.drive(-15, 0)
                tempcolor = colorFront.color()
                if tempcolor != None and tempcolor != Color.YELLOW and tempcolor != Color.WHITE:
                    holdingColor = tempcolor
            
            # Terug draaien
            robotBase.straight(-30)
            robotBase.drive(0, 0)
            armMotor.run_until_stalled(200, duty_limit=90)
            robotBase.straight(robotBase.distance() * -1)
            robotRotate(gyro, robotBase, 30, 90)

            
            holding = True

        else:
            robotBase.straight(-20)

    elif stationCount >= 1:
        # print(holdingColor)
        # print(stations[stationCount])
        if holding == True and stations[stationCount] == holdingColor: #! HIER ZIT DE FOUT
            robotBase.drive(0,0)
            robotBase.straight(-110)
            robotRotate(gyro, robotBase, 30, -90)
            # robotBase.settings(25, 100, 90, 180)
            robotBase.straight(-60)
            # robotBase.settings(100, 200, 90, 180)

            armMotor.run_until_stalled(-200, duty_limit=90)
            holding = False

            robotBase.straight(60)
            robotRotate(gyro, robotBase, 30, 90)
            robotBase.straight(50)
        else:
            robotBase.straight(-20)
    
    returnList = [holding, holdingColor]
    return returnList

