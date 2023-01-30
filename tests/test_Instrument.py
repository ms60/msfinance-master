import sys
sys.path.append("..") # add the module to path

from msfinance.Instrument import Instrument
from datetime import datetime

from msfinance.COMMON import COMMON

# for index_name in COMMON:
#     x = Instrument(index_name)
#     x.getDataFromToday(5)
#     print(x)

cds_6m = Instrument('CDS_6M')
cds_6m.getDataFromFile('./test_files/cds_6m.csv')

print(cds_6m)

cds_1y = Instrument('CDS_1Y')
cds_1y.getDataFromFile('./test_files/cds_1y.csv')

print(cds_1y)