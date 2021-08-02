import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import linregress


#data =pd.read_csv("epa-sea-level.csv")

def draw_plot():
# Read data from file
  df =pd.read_csv("epa-sea-level.csv")
#float_precision=‘legacy’
# Create scatter plot

  df.plot.scatter('Year','CSIRO Adjusted Sea Level',label='original data',figsize=(12, 7))

  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
  plt.legend(fontsize="medium")
  plt.show()

# Create first line of best fit
  year1 = list(range(1880, 2050))
  year1 = pd.Series(year1)
  year2 = list(range(2000, 2050))
  year2 = pd.Series(year2)

  res = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
  df2 = df[df.Year>= 2000]
  res2 = linregress(df2.Year, df2["CSIRO Adjusted Sea Level"])

  plt.figure(figsize=(10,5))
  plt.plot(df.Year, df["CSIRO Adjusted Sea Level"], 'o', markersize = 5.2, label='original data')
  plt.plot(year1, res.intercept + res.slope*year1, 'r', linewidth=2.5, label='fitted line 1')

# Create second line of best fit
  plt.plot(year2, res2.intercept + res2.slope*year2, 'r', linewidth=2.5, label='fitted line 2', color='green')
  plt.legend()

# Add labels and title
  plt.xlabel('Year')
