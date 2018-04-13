#!/usr/bin/env python
#
#   Script:          wxgen.py
#   Author:          Brian Vanderwende
#   Last Revised:    22:02, 12 Apr 2018
#
#   This code generates a fake weather forecast for Boulder, CO
#

# Libraries
from random import gauss, random

# Define some statistics for Boulder, CO
avg_high    = 18.5          # deg C
avg_low     = 3.3           # deg C
avg_precip  = 525.0 / 65    # mm
chc_precip  = 65.0 / 365
std_temp    = 4.5
std_precip  = 10

# Produce a forecast
num_days = 7

print("Forecast for Boulder, CO")

for day in range(num_days):
    # Will rain/snow occur?
    precip = 0.0

    if random() < chc_precip:
        precip = gauss(avg_precip, std_precip)

    print("\nDay {}".format(day + 1))
    print("  High:      {:5.2f} deg C".format(gauss(avg_high, std_temp)))
    print("  Low:       {:5.2f} deg C".format(gauss(avg_low, std_temp)))
    print("  Precip:    {:5.2f} mm".format(precip))
