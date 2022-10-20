def lineFollow(robot, colorGround):
    speed = 700
    rotationSpeed = 1.5
    percentageStraight = 50

    while True:
        rotation = colorGround.reflection() - percentageStraight
        robot.drive(speed, rotationSpeed * rotation)

def robotRotate(gyro, left_motor, right_motor):
    gyro.reset_angle(0)

    correctionRotationSpeed = 2000
    correctionBufferSpeed = 150
    rotationBuffer = 5
    angle_Rotate = 180

    while True:
        if gyro.angle() < angle_Rotate and angle_Rotate - gyro.angle() > rotationBuffer:
            left_motor.run(correctionRotationSpeed)
            right_motor.run(correctionRotationSpeed*-1)
        elif gyro.angle() > angle_Rotate and gyro.angle() - angle_Rotate > rotationBuffer:
            left_motor.run(correctionRotationSpeed*-1)
            right_motor.run(correctionRotationSpeed)
        elif gyro.angle() < angle_Rotate and angle_Rotate - gyro.angle() < rotationBuffer:
            left_motor.run(correctionBufferSpeed)
            right_motor.run(correctionBufferSpeed*-1)
        elif gyro.angle() > angle_Rotate and gyro.angle() - angle_Rotate < rotationBuffer:
            left_motor.run(correctionBufferSpeed*-1)
            right_motor.run(correctionBufferSpeed)
        else:
            left_motor.hold()
            right_motor.hold()
            break
        print(gyro.angle())
