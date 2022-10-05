basic.show_string("MOTOR STARTS")
ONTIME = 5000
ONTIME = 3000

def on_forever():
    OFFTIME = 0
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.show_string("CLOCK WISE")
    basic.pause(ONTIME)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.show_string("ANTI CLOCK WISE")
    basic.pause(OFFTIME)
basic.forever(on_forever)
