let a = 0
radio.onReceivedNumber(function (receivedNumber) {
    if (0 == receivedNumber) {
        SuperBit.MotorRunDual(
        SuperBit.enMotors.M1,
        255,
        SuperBit.enMotors.M2,
        255
        )
    }
    if (1 == receivedNumber) {
        SuperBit.MotorRunDual(
        SuperBit.enMotors.M1,
        -255,
        SuperBit.enMotors.M2,
        -255
        )
    }
    if (2 == receivedNumber) {
        SuperBit.MotorRunDual(
        SuperBit.enMotors.M1,
        0,
        SuperBit.enMotors.M2,
        0
        )
    }
})
input.onGesture(Gesture.Shake, function () {
    radio.sendNumber(2)
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendNumber(0)
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(2)
})
function anyfunc () {
    a = 5
}
basic.forever(function () {
    basic.showLeds(`
        . . . . #
        . . . . #
        . . . # #
        . . # . .
        . . . # #
        `)
    basic.showLeds(`
        . . # # .
        . # . . #
        . . . . #
        . . # # #
        . # . . #
        `)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        . . # . .
        `)
})
