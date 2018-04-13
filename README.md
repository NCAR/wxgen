# Python Weather Generator

**Author: Brian Vanderwende**  
**Version: beta1**

This weather generator creates a sample forecast for Boulder, CO. Daily values are produced for high temperature, low temperature, and accumulated precipitation.

### Requirements

Python 2.6+ or 3.x

### Details

The weather generator features the following tunable parameters:

+ Number of days to forecast
+ Mean and standard deviation values for Gaussian distributions
+ Chance of precipitation on any particular day

### How to Run

Simply execute the script:

```
./wxgen.py
```

The forecast will be written to a file in the "forecasts" directory:

```
Forecast for Boulder, CO

Day 1
  High:      12.33 deg C
  Low:        9.56 deg C
  Precip:     0.00 mm

Day 2
...
```
