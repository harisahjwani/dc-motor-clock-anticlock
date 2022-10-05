basic.showString("STARTING MOTOR")
let ONTIME = 3000
let OFFTIME = 1000
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.showString("CLOCK WISE")
    basic.pause(ONTIME)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.showString("ANTI CLOCK WISE")
    basic.pause(OFFTIME)
})
