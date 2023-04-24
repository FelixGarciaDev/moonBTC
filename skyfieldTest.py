import numpy as np
from skyfield.api import load
from skyfield.framelib import ecliptic_frame

def get_moon_phase_by_degrees(year: int, month:int, day:int, hour:int, minute:int):
    """Returns a string that describes the moon phase acordingly to the moon degrees"""
    ts = load.timescale()
    t = ts.utc(year, month, day, hour, minute)

    eph = load('de421.bsp')
    sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

    e = earth.at(t)
    s = e.observe(sun).apparent()
    m = e.observe(moon).apparent()

    _, slon, _ = s.frame_latlon(ecliptic_frame)
    _, mlon, _ = m.frame_latlon(ecliptic_frame)
    phase = (mlon.degrees - slon.degrees) % 360.0

    percent = 100.0 * m.fraction_illuminated(sun)

    print('Phase (0°–360°): {0:.1f}'.format(phase))
    print('Percent illuminated: {0:.1f}%'.format(percent))
    value = int(phase)
    ranges = {
        tuple(range(0, 45)): 'New Moon',
        tuple(range(45, 90)): 'Waxing Crescent',
        tuple(range(90, 135)): 'First Quarter',
        tuple(range(135, 180)): 'Waxing Gibbous',
        tuple(range(180, 255)): 'Full Moon',
        tuple(range(225, 270)): 'Waning Gibbous',
        tuple(range(270, 315)): 'Last Quarter',
        tuple(range(315, 359)): 'Waning Crescent',
        tuple(range(359, 360)): 'New Moon'
    }

    for r, message in ranges.items():
        if value in r:
            return phase, percent, message
        else:
            print('Value is outside the range')


y = 2017
m = 8
d = 14
h = 2
min = 0
print("the moon phase is: " + str(get_moon_phase_by_degrees(y, m, d, h, min)))
