# Created: November 18, 2022
# Author: Brendan Keane (GitHub @brendanwilliam)
# Purpose: Shotevent class

# Imports
import json
import pandas as pd
import os
import re

class ShotEvent:
  def __init__(self, data):
    self.time = getTotalSeconds(data)
    self.player = data['playerNameI']
    self.team = data['teamTricode']

def getTotalSeconds(data):
  # Getting clock and period values
  twodigits = re.compile('[0-9]{2}')
  clock = twodigits.findall(data['clock'])
  period = data['period']

  # Converting clock to seconds
  period_seconds = (period - 1) * 3600
  clock_seconds = int(clock[0]) * 60 + int(clock[1]) + int(clock[2]) / 100

  return period_seconds + clock_seconds