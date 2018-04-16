# Python Weather Generator

**Author: Brian Vanderwende**  
**Version: 1.0**

This weather generator creates a sample forecast for multiple cities. Currently, forecasts are produced for:

+ Boulder, CO
+ Philadelphia, PA

Daily values are produced for high temperature, low temperature, and accumulated precipitation.

### Requirements

Python 2.6+ or 3.x

### Details

The weather generator features the following tunable parameters:

+ Number of days to forecast
+ Mean and standard deviation values for Gaussian distributions
+ Chance of precipitation on any particular day

These parameters are set for each city in JSON format in the "cities" directory.

### How to Run

Simply execute the script:

```
./wxgen.py
```

The forecasts will be written to files in the "forecasts" directory:

```
Forecast for Boulder, CO
Generated at 2134Z - 13 Apr 2018

Day 1
  High:      12.33 deg C
  Low:        9.56 deg C
  Precip:     0.00 mm

Day 2
...
```
