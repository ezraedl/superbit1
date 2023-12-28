a = 0

def on_received_number(receivedNumber):
    if 0 == receivedNumber:
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, 255, SuperBit.enMotors.M2, 255)
    if 1 == receivedNumber:
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, -255, SuperBit.enMotors.M2, -255)
    if 2 == receivedNumber:
        SuperBit.motor_run_dual(SuperBit.enMotors.M1, 0, SuperBit.enMotors.M2, 0)
radio.on_received_number(on_received_number)

def on_gesture_shake():
    radio.send_number(2)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    radio.send_number(0)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_tilt_left():
    radio.send_number(1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    radio.send_number(2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def anyfunc():
    global a
    a = 5

def on_forever():
    basic.show_leds("""
        . . . . #
        . . . . #
        . . . # #
        . . # . .
        . . . # #
        """)
    basic.show_leds("""
        . . # # .
        . # . . #
        . . . . #
        . . # # #
        . # . . #
        """)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        . . # . .
        """)
basic.forever(on_forever)
