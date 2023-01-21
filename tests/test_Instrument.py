import sys
sys.path.append("..") # add the module to path

from msfinance.Instrument import Instrument
from datetime import datetime

arclk = Instrument("ARCLK.IS")
arclk.getDataFromToday(50)
print(arclk)