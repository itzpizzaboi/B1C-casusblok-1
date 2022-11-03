from time import sleep

def lineFollow(robot, colorGround):
    speed = -50
    rotationSpeed = -1
    percentageStraight = 50

    # Volg de lijn op basis van reflectie tussen 2 kleuren
    rotation = colorGround.reflection() - percentageStraight
    robot.drive(speed, rotationSpeed * rotation)

def robotRotate(gyro, robotBase, speed, rotationTarget):
    # Draai de gegeven hoeveelheid graden in de aangegeven richting    
    gyro.reset_angle(0)

    if rotationTarget < 0:
        while gyro.angle() > rotationTarget:
            robotBase.drive(0, speed)

    elif rotationTarget > 0:
        while gyro.angle() < rotationTarget:
            robotBase.drive(0, -speed)

    robotBase.drive(0,0)

def rotationByLine(colorGround, robotBase, speed, rotationTarget, Color):
    # Draai totdat de kleur blauw gezien is
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
                    stationCount, holding, holdingColor,
                    stations, distanceSensor, Color):
    # Het ophalen van een item bij station Home                
    if stationCount == 0:
        if holding == False:
            # Benaderen van het item
            robotBase.drive(0,0)
            robotBase.straight(-110)
            robotRotate(gyro, robotBase, 30, -90)

            # Checken aanwezigheid van item
            while distanceSensor.distance() >= 400:
                pass

            # Pakken van item
            robotBase.reset()
            while distanceSensor.distance() >= 35:
                robotBase.drive(-15, 0)
                tempcolor = colorFront.color()
                if tempcolor != None and tempcolor != Color.YELLOW and tempcolor != Color.WHITE:
                    holdingColor = tempcolor
                    print(holdingColor)
            
            # Terug draaien
            robotBase.straight(-25)
            robotBase.drive(0, 0)
            armMotor.run_until_stalled(200, duty_limit=120)
            robotBase.straight(robotBase.distance() * -1)
            robotRotate(gyro, robotBase, 30, 90)

            holding = True
        # Skip het station
        else:
            robotBase.straight(-20)

    # Het afgeven van een item bij alle andere stations
    elif stationCount >= 1:
        if holding == True and stations[stationCount] == holdingColor:
            # Draai naar de afgeef locatie van het item
            robotBase.drive(0,0)
            robotBase.straight(-110)
            robotRotate(gyro, robotBase, 30, -90)
            robotBase.straight(-60)

            # Laat het item los
            armMotor.run_until_stalled(-200, duty_limit=90)
            holding = False

            # Draai terug naar de lijn
            robotBase.straight(60)
            robotRotate(gyro, robotBase, 30, 90)
            robotBase.straight(50)
        # Skip het station
        else:
            robotBase.straight(-20)
    
    returnList = [holding, holdingColor]
    return returnList
