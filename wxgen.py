#!/usr/bin/env python
#
#   Script:          wxgen.py
#   Author:          Brian Vanderwende
#   Last Revised:    15:33, 13 Apr 2018
#
#   This code generates a fake weather forecast for Boulder, CO
#

# Libraries
import json, sys
from random import gauss, random
from datetime import datetime

# User settings
city_list   = ["boulder","philadelphia"]
fcst_path   = "forecasts/{}.txt"
num_days    = 7

#
## FUNCTION DEFINITIONS
#

def read_city_data(city_name):
    try:
        with open("cities/{}.json".format(city_name), 'r') as city_file:
            city_data = json.load(city_file)
    except IOError:
        print("Error: no JSON file for city {}. Exiting...".format(city_name))
        sys.exit(1)

    return city_data

#
# MAIN PROGRAM
#

if __name__ == "__main__":
    gen_time = datetime.utcnow().strftime("%H%MZ - %d %b %Y")

    for city in city_list:
        # Read settings and specify output file
        csd         = read_city_data(city)
        fcst_file   = fcst_path.format(city)

        with open(fcst_file, 'w') as ffo:
            ffo.write("Forecast for {}, {}\n".format(csd["name"], csd["state"]))
            ffo.write("Generated at {}\n".format(gen_time))

            for day in range(num_days):
                # Produce temperature forecasts
                high    = gauss(csd["high"]["avg"], csd["high"]["std"])
                low     = gauss(csd["low"]["avg"], csd["low"]["std"])

                # Will rain/snow occur?
                precip  = 0.0
                p_chc   = csd["precip"]["days"] / 365.0
                p_avg   = csd["precip"]["yamt"] / csd["precip"]["days"]

                # If precip occurs, use folded normal distribution
                if random() < p_chc:
                    precip = abs(gauss(p_avg, csd["precip"]["std"]))

                ffo.write("\nDay {}".format(day + 1))
                ffo.write("\n  High:      {:5.2f} deg C".format(high))
                ffo.write("\n  Low:       {:5.2f} deg C".format(low))
                ffo.write("\n  Precip:    {:5.2f} mm\n".format(precip))

        print("Forecast generated in {}".format(fcst_file))
