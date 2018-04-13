#!/usr/bin/env python
#
#   Script:          wxgen.py
#   Author:          Brian Vanderwende
#   Last Revised:    23:04, 12 Apr 2018
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
fcst_path   = "forecasts/boulder.txt"
num_days    = 7

with open(fcst_path, 'w') as ffo:
    ffo.write("Forecast for Boulder, CO")

    for day in range(num_days):
        # Will rain/snow occur?
        precip = 0.0

        if random() < chc_precip:
            precip = gauss(avg_precip, std_precip)

        ffo.write("\nDay {}".format(day + 1))
        ffo.write("  High:      {:5.2f} deg C".format(gauss(avg_high, std_temp)))
        ffo.write("  Low:       {:5.2f} deg C".format(gauss(avg_low, std_temp)))
        ffo.write("  Precip:    {:5.2f} mm".format(precip))

print("Forecast generated in {}".format(fcst_path))
