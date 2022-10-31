from time import sleep

def lineFollow(robot, colorGround):
    speed = -100
    rotationSpeed = -1.2
    percentageStraight = 40

    rotation = colorGround.reflection() - percentageStraight
    robot.drive(speed, rotationSpeed * rotation)

def robotRotate(gyro, robotBase, speed, rotationTarget):

    gyro.reset_angle(0)
    
    if rotationTarget < 0:
        while gyro.angle() > rotationTarget:
           robotBase.drive(0, speed)
           print(gyro.angle())

    elif rotationTarget > 0:
        while gyro.angle() < rotationTarget:
            robotBase.drive(0, -speed)
            print(gyro.angle())

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