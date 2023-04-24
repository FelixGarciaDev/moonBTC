import numpy as np
import datetime
import ephem

def get_phase_on_day(year: int, month: int, day: int):
  """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""
  #Ephem stores its date numbers as floating points, which the following uses
  #to conveniently extract the percent time between one new moon and the next
  #This corresponds (somewhat roughly) to the phase of the moon.

  #Use Year, Month, Day as arguments
  date = ephem.Date(datetime.date(year,month,day))

  nnm = ephem.next_new_moon(date)
  pnm = ephem.previous_new_moon(date)

  lunation = (date-pnm)/(nnm-pnm)

  #Note that there is a ephem.Moon().phase() command, but this returns the
  #percentage of the moon which is illuminated. This is not really what we want.

  return lunation

print(get_phase_on_day(2023,4,18))

def get_moon_phase_by_degrees(degrees: float):
    """Returns a string that describes the moon phase acordingly to the moon degrees"""
    value = degrees
    ranges = {
        tuple(np.arange(0, 45,  0.01)): 'new moon',
        tuple(np.arange(45, 90,   0.01)): 'waxing crescent',
        tuple(np.arange(90, 135,  0.01)): 'first quarter',
        tuple(np.arange(135, 180,  0.01)): 'waxing gibbous',
        tuple(np.arange(180, 225,  0.01)): 'full moon',
        tuple(np.arange(225, 270,  0.01)): 'waning gibbous',
        tuple(np.arange(270, 315,  0.01)): 'last quarter',
        tuple(np.arange(315, 359,  0.01)): 'waning crescent',
        tuple(np.arange(359, 360,  0.01)): 'new moon',
    }

    for r, message in ranges.items():
        if value in r:
            return message
            break
        else:
            print('Value is outside the range')
  

print("---"*10)
# The phase is returned as a string with one of the following values: 
# "new moon", "waxing crescent", "first quarter", "waxing gibbous", "full moon", "waning gibbous", "last quarter", or "waning crescent".
# set the date for which you want to determine the moon phase
date_str = '2023/04/18'
date = ephem.Date(date_str)

# find the date of the previous and next new moons relative to the given date
prev_new_moon = ephem.previous_new_moon(date)
next_new_moon = ephem.next_new_moon(date)

# calculate the moon's phase for the given date
moon = ephem.Moon()
moon.compute(prev_new_moon)
phase_at_prev_new_moon = moon.phase
moon.compute(next_new_moon)
phase_at_next_new_moon = moon.phase
phase = (phase_at_next_new_moon - phase_at_prev_new_moon) * (date - prev_new_moon) / (next_new_moon - prev_new_moon) + phase_at_prev_new_moon
print(phase)

constellation = ephem.constellation(moon)[1]

# print the moon phase
# print(f"The moon's phase is {constellation}.")

# print the moon phase for the given date
stringPhase = get_moon_phase_by_degrees(round(phase,2))
print(f"The moon's phase on {date_str} is {stringPhase} with {phase:.2f} degrees.")
# print(type(phase))
# The moon's phase is returned as a float between 0 and 360 degrees, 
# where 0 degrees represents a new moon, 90 degrees represents a first quarter moon, 
# 180 degrees represents a full moon, and 270 degrees represents a last quarter moon.