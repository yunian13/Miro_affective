import time
import miro2 as miro
import random


###################################################
# neutral
# Describe this function...
def neutral():
    look_around()
    move()


# Describe this function...
def look_around():
    robot.neck_angle(miro.constants.JOINT_YAW, 10)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    lookLR()
    robot.wag_frequency(0.5)
    robot.sleep(0.5)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    blink()
    robot.turn_angle(10)
    robot.wag_frequency(0)
    blink3()
    robot.sleep(0.5)
    blink()
    robot.turn_angle((-10))
    robot.sleep(0.5)
    robot.neck_angle(miro.constants.JOINT_LIFT, 34)
    robot.sleep(0.5)
    robot.neck_angle(miro.constants.JOINT_YAW, 5)
    robot.neck_angle(miro.constants.JOINT_LIFT, 59)
    blink()
    robot.sleep(2)
    blink()
    robot.sleep(1)
    robot.sleep(0.5)
    robot.joint_position(miro.constants.JOINT_EYE_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 1.0)
    robot.sleep(3)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 0.0)
    blink3()
    robot.neck_angle(miro.constants.JOINT_LIFT, 34)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    robot.joint_position(miro.constants.JOINT_DROOP, 0.0)


# Describe this function...
def move():
    robot.control_led(miro.constants.ILLUM_ALL, [51, 204, 0], 255)
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 35)
    robot.joint_position(miro.constants.JOINT_WAG, 0.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 25)
    lookLR()
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    robot.sleep(0.5)
    blink()
    robot.sleep(0.5)
    robot.drive_distance(+0.3)
    robot.neck_angle(miro.constants.JOINT_YAW, 10)
    robot.sleep(0.5)
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, (-10))
    robot.neck_angle(miro.constants.JOINT_YAW, 5)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 255], 255)


# Describe this function...
def lookLR():
    robot.joint_position(miro.constants.JOINT_EYE_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 1.0)
    robot.sleep(0.3)
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)
    robot.neck_angle(miro.constants.JOINT_YAW, 54)
    robot.sleep(1)
    robot.neck_angle(miro.constants.JOINT_YAW, -54)
    robot.sleep(1)


# Describe this function...
def blink():
    robot.joint_position(miro.constants.JOINT_EYE_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 1.0)
    robot.sleep(0.3)
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)


# Describe this function...
def blink3():
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, 5)
    robot.sleep(0.8)
    robot.neck_angle(miro.constants.JOINT_PITCH, -21)
    blink()
    robot.sleep(0.5)
    robot.neck_angle(miro.constants.JOINT_PITCH, 0)


############################################################
# angry
# Describe this function...
def angry():
    barking()
    moving()
    barking()
    bluffing()


# Describe this function...

# Describe this function...
def bluffing():
    robot.neck_angle(miro.constants.JOINT_LIFT, 45)
    robot.neck_angle(miro.constants.JOINT_PITCH, -21)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    robot.joint_position(miro.constants.JOINT_DROOP, 0.0)
    blink()
    for count in range(2):
        robot.sleep(0.5)
        robot.play_tone(500, 0.5, 100)
        robot.neck_angle(miro.constants.JOINT_LIFT, 15)
        robot.drive_distance(+0.15)
        robot.neck_angle(miro.constants.JOINT_LIFT, 25)
        robot.sleep(0.25)
        robot.neck_angle(miro.constants.JOINT_LIFT, 15)
        robot.drive_distance(-0.15)
        robot.neck_angle(miro.constants.JOINT_LIFT, 25)


# Describe this function...
def moving():
    robot.control_led(miro.constants.ILLUM_ALL, [255, 102, 102], 255)
    for count2 in range(2):
        blink()
        robot.neck_angle(miro.constants.JOINT_YAW, 10)
        robot.neck_angle(miro.constants.JOINT_LIFT, 15)
        robot.turn_speed(+150)
        robot.sleep(0.8)
        robot.turn_speed(0.0)
        robot.neck_angle(miro.constants.JOINT_YAW, 0)
        robot.neck_angle(miro.constants.JOINT_LIFT, 25)
        robot.speed(+0.4)
        robot.sleep(0.8)
        robot.speed(0.0)
        robot.neck_angle(miro.constants.JOINT_YAW, (-10))
        robot.neck_angle(miro.constants.JOINT_LIFT, 15)
        robot.turn_speed(-150)
        robot.sleep(0.8)
        robot.turn_speed(0.0)
        robot.neck_angle(miro.constants.JOINT_YAW, 0)
        robot.neck_angle(miro.constants.JOINT_LIFT, 25)
        robot.speed(+0.4)
        robot.sleep(0.8)
        robot.neck_angle(miro.constants.JOINT_LIFT, 15)
        robot.speed(0.0)
    robot.sleep(0.25)
    robot.control_led(miro.constants.ILLUM_L, [255, 255, 255], 255)


# Describe this function...
def barking():
    robot.neck_angle(miro.constants.JOINT_PITCH, -21)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 15)
    robot.sleep(0.5)
    blink()
    robot.drive_distance(+0.3)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 0, 0], 255)
    robot.sleep(0.25)
    blink()
    robot.neck_angle(miro.constants.JOINT_PITCH, -21)
    robot.sleep(0.4)
    for count3 in range(6):
        robot.neck_angle(miro.constants.JOINT_LIFT, 5)
        robot.sleep(0.25)
        robot.play_tone(500, 0.5, 100)
        robot.neck_angle(miro.constants.JOINT_LIFT, 15)
        robot.sleep(0.15)
        robot.neck_angle(miro.constants.JOINT_LIFT, 5)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 255], 255)
    robot.neck_angle(miro.constants.JOINT_PITCH, 0)
    robot.sleep(0.5)


###################################################
# happy
# Describe this function...
def slight_happy():
    robot.sleep(0.2)
    robot.joint_position(miro.constants.JOINT_DROOP, 0.0)
    robot.wag_frequency(1)
    blink()
    move_head()
    robot.sleep(1.5)
    robot.wag_frequency(0)


# Describe this function...
def happy():
    spin_around()
    slight_happy()
    super_happy()
    slight_happy()


# Describe this function...
def move_head():
    robot.wag_frequency(1.5)
    robot.neck_angle(miro.constants.JOINT_YAW, 4)
    robot.sleep(1.5)
    robot.neck_angle(miro.constants.JOINT_YAW, 15)
    robot.sleep(1)
    robot.neck_angle(miro.constants.JOINT_YAW, (-4))
    robot.sleep(1.5)
    robot.neck_angle(miro.constants.JOINT_YAW, (-15))
    robot.sleep(1)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)


# Describe this function...
def spin_around():
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 0.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 9)
    robot.joint_position(miro.constants.JOINT_DROOP, 0.0)
    robot.sleep(1)
    robot.wag_frequency(1.5)
    if random.randint(1, 10) % 2 == 0:
        robot.neck_angle(miro.constants.JOINT_YAW, 54)
        robot.turn_speed(+150)
        robot.speed(+0.25)
        blink()
    if random.randint(1, 10) % 2 == 1:
        robot.neck_angle(miro.constants.JOINT_YAW, -54)
        robot.turn_speed(-150)
        robot.speed(+0.25)
        blink()
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 0], 255)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 0.0)
    robot.sleep(1)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    robot.sleep(1)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 0.0)
    robot.sleep(1)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    robot.sleep(1)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 0.0)
    robot.sleep(1)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 255], 255)
    robot.turn_speed(0.0)
    robot.speed(0.0)
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, 0)


# Describe this function...
def super_happy():
    robot.wag_frequency(1.5)
    blink()
    if random.randint(1, 10) % 2 == 0:
        robot.neck_angle(miro.constants.JOINT_YAW, -54)
    if random.randint(1, 10) % 2 == 1:
        robot.neck_angle(miro.constants.JOINT_YAW, 54)
    robot.sleep(1)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    robot.joint_position(miro.constants.JOINT_DROOP, 0.0)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 102], 255)
    robot.speed(+0.25)
    blink()
    robot.sleep(1.5)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 255], 255)
    robot.speed(0.0)
    robot.sleep(0.3)
    spin_around()


###################################################
# Describe this function...
def fearful():
    moving_head()
    turn_around()
    moving_head()
    turn_back()


# Describe this function...
def moving_head():
    robot.control_led(miro.constants.ILLUM_ALL, [102, 51, 51], 255)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 59)
    robot.joint_position(miro.constants.JOINT_DROOP, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 1.0)
    robot.sleep(0.25)
    for count in range(3):
        robot.neck_angle(miro.constants.JOINT_YAW, 2)
        robot.sleep(0.25)
        robot.neck_angle(miro.constants.JOINT_YAW, (-2))
        robot.sleep(0.25)


# Describe this function...
def turn_around():
    robot.sleep(1.25)
    blink()
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 15)
    robot.control_led(miro.constants.ILLUM_ALL, [102, 51, 51], 255)
    robot.joint_position(miro.constants.JOINT_DROOP, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    for count2 in range(2):
        robot.neck_angle(miro.constants.JOINT_YAW, 2)
        robot.sleep(0.2)
        robot.neck_angle(miro.constants.JOINT_YAW, (-2))
        robot.sleep(0.2)
    blink()
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 0.0)
    robot.joint_position(miro.constants.JOINT_DROOP, 1.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 40)
    robot.drive_distance((-0.3), 0.6)
    if random.randint(1, 10) % 2 == 1:
        robot.neck_angle(miro.constants.JOINT_YAW, 10)
        robot.turn_speed(-150)
        robot.turn_angle(90, 180)
        robot.speed(+0.4)
    if random.randint(1, 10) % 2 == 0:
        blink()
        robot.neck_angle(miro.constants.JOINT_YAW, (-10))
        robot.turn_speed(+150)
        robot.turn_angle(90, 90)
        robot.speed(+0.4)
    robot.sleep(2)
    robot.speed(0.0)
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 59)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 1.0)
    robot.sleep(1)


# Describe this function...
def turn_back():
    blink()
    robot.sleep(1.25)
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 15)
    robot.control_led(miro.constants.ILLUM_ALL, [102, 51, 51], 255)
    robot.joint_position(miro.constants.JOINT_DROOP, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    for count3 in range(2):
        robot.neck_angle(miro.constants.JOINT_YAW, 2)
        robot.sleep(0.2)
        robot.neck_angle(miro.constants.JOINT_YAW, (-2))
        robot.sleep(0.2)
    robot.neck_angle(miro.constants.JOINT_LIFT, 40)
    blink()
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_DROOP, 1.0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 40)
    robot.neck_angle(miro.constants.JOINT_YAW, (-10))
    robot.turn_angle(180, 180)
    blink()
    robot.speed(+0.4)
    robot.sleep(2)
    robot.speed(0.0)
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    robot.neck_angle(miro.constants.JOINT_LIFT, 59)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 1.0)
    robot.sleep(1)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 255], 255)


###########################################################
# Describe this function...
def sad():
    robot.joint_position(miro.constants.JOINT_DROOP, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)
    robot.joint_position(miro.constants.JOINT_EAR_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYR_R, 0.0)
    robot.neck_angle(miro.constants.JOINT_PITCH, 7)
    robot.neck_angle(miro.constants.JOINT_LIFT, 59)
    light_sad()
    make_contact()
    super_sad()


# Describe this function...
def light_sad():
    robot.neck_angle(miro.constants.JOINT_LIFT, 60)
    robot.sleep(1)
    robot.joint_position(miro.constants.JOINT_DROOP, 1.0)
    robot.control_led(miro.constants.ILLUM_ALL, [51, 51, 255], 255)
    for count in range(2):
        robot.neck_angle(miro.constants.JOINT_LIFT, 60)
        robot.sleep(0.4)
        robot.neck_angle(miro.constants.JOINT_LIFT, 55)
        robot.sleep(0.5)
        robot.neck_angle(miro.constants.JOINT_LIFT, 60)
        robot.sleep(0.5)


# Describe this function...
def make_contact():
    robot.neck_angle(miro.constants.JOINT_LIFT, 40)
    robot.joint_position(miro.constants.JOINT_EAR_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EAR_R, 1.0)
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, 5)
    robot.sleep(2)
    robot.neck_angle(miro.constants.JOINT_LIFT, 45)
    robot.sleep(0.3)
    robot.joint_position(miro.constants.JOINT_EYE_L, 1.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 1.0)
    for count2 in range(2):
        robot.neck_angle(miro.constants.JOINT_YAW, 3)
        robot.sleep(0.4)
        robot.neck_angle(miro.constants.JOINT_YAW, (-3))
        robot.sleep(0.3)
    robot.control_led(miro.constants.ILLUM_ALL, [51, 102, 255], 255)
    robot.joint_position(miro.constants.JOINT_EYE_L, 0.0)
    robot.joint_position(miro.constants.JOINT_EYE_R, 0.0)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    blink()
    robot.neck_angle(miro.constants.JOINT_PITCH, 7)
    robot.sleep(0.3)
    robot.turn_angle(90)
    robot.neck_angle(miro.constants.JOINT_LIFT, 59)


# Describe this function...
def super_sad():
    robot.sleep(1)
    robot.control_led(miro.constants.ILLUM_ALL, [0, 0, 153], 255)
    robot.neck_angle(miro.constants.JOINT_YAW, 5)
    robot.sleep(1)
    blink()
    robot.neck_angle(miro.constants.JOINT_YAW, (-5))
    robot.sleep(2)
    robot.neck_angle(miro.constants.JOINT_YAW, 0)
    robot.neck_angle(miro.constants.JOINT_PITCH, 7)
    robot.sleep(2)
    robot.joint_position(miro.constants.JOINT_DROOP, 1.0)
    robot.control_led(miro.constants.ILLUM_ALL, [255, 255, 255], 255)

# touching
touch_body_variable = None

# connect to robot
robot = MirocodeInterface(pose_ctrl=False, cliff_reflex=False)

#### robot is now connected ####
# first iteration
neutral()
robot.sleep(10)
angry()
robot.sleep(10)
happy()
robot.sleep(10)
fearful()
robot.sleep(10)
sad()

# second iteration
fearful()
robot.sleep(10)
happy()
robot.sleep(10)
angry()
robot.sleep(10)
sad()
robot.sleep(10)
neutral()

# third iteration
happy()
robot.sleep(10)
fearful()
robot.sleep(10)
neutral()
robot.sleep(10)
sad()
robot.sleep(10)
angry()


touch_body_variable = robot.read_body_touch_sensor_list()[0]
for count in range(10000000):
    if touch_body_variable != robot.read_body_touch_sensor_list()[0]:
        happy()
    if robot.detect_shake() == True:
        fearful()
    if robot.detect_clap() == True:
        angry()
    if robot.read_light_sensor(2) <= 0.2:
        sad()

