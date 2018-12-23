# Import libraries
import matplotlib.pyplot as pyplot
import datetime as dt
from collections import defaultdict

tageswert = defaultdict(list)

# Read data from text file
with open('temperatur.txt') as f:
    for zeile in f:
        datumString, t = zeile.split('\t')
        datum = (dt.datetime.strptime(datumString, '%d.%m.%Y %H:%M:%S')).date()
        t = float(t)
        tageswert[datum].append(t)

# Add information to each needed list
tagMax = []
tagMin = []
tagDatum = []

# Add values if they are in reasonable values
for key in tageswert:
    high = max(tageswert[key])
    low = min(tageswert[key])

    if abs(high) < 40 and abs(low):
        tagMax.append(high)
        tagMin.append(low)
        tagDatum.append(key)

# Plot with matplotlib
fig, ax = pyplot.subplots()
ax.plot(tagDatum, tagMax, lw = 1, label = 'High', color = 'red') # High of the day
ax.plot(tagDatum, tagMin, lw = 1, label = 'Low', color = 'blue') # Low of the day
ax.fill_between(tagDatum, tagMax, tagMin, facecolor = 'orange', alpha = 0.2, label = 'Range') # Fill between high and low of the day
ax.grid(linestyle = ':', linewidth = '0.5', color = 'green') # Grid
ax.legend() # Show labels as legends
pyplot.yticks([-10, 0, 10, 20, 30, 40]) # Values for Y grid

pyplot.show()