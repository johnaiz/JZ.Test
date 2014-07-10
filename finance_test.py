import datetime
import numpy as numpy
import matplotlib.finance as finance
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.colors as colors



startdate = datetime.date(2006, 1, 1)
today = enddate = datetime.date.today()

ticker = 'SPY'

fh = finance.fetch_historical_yahoo(ticker, startdate, enddate)

r = mlab.csv2rec(fh)

fh.close()

r.sort()

plt.rc('axes', grid=True)
plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)

# textsize = 9
# left, width = 0.1, 0.8
# rect1 = [left, 0.7, width, 0.2]
# rect2 = [left, 0.3, width, 0.4]
# rect3 = [left, 0.1, width, 0.2]


# fig = plt.figure(facecolor='white')
# axescolor  = '#f6f6f6'  # the axes background color

# ax1 = fig.add_axes(rect1, axisbg=axescolor)  #left, bottom, width, height
# ax2 = fig.add_axes(rect2, axisbg=axescolor, sharex=ax1)
# ax2t = ax2.twinx()
# ax3  = fig.add_axes(rect3, axisbg=axescolor, sharex=ax1)






plt.show()