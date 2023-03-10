import pandas_datareader as web
import pandas as pd
from datetime import datetime,timedelta
from dateutil.parser import parse
from copy import deepcopy
import matplotlib.pyplot as plt
import mplcursors
import yfinance as yf
yf.pdr_override()

class Instrument:
	def __init__(self , name):
		self.data = pd.DataFrame()
		self.name = name
		# add some characteristic features about instrument

	def __str__(self):
		return self.data.to_string()

	def __repr__(self):
		return self.data
	
	def __eq__(self, other):
		if isinstance(other, Instrument):
			return self.data.equals(other.data.equals())
		return False

	def getDataCount(self):
		return len(self.data.index)

	def setName(self , targetName):
		if not isinstance(targetName , str):
			raise TypeError("targetname must be type of string.")
		self.name = targetName

	def getName(self):
		return self.name

	def getData(self):
		return self.data

	def setData(self , targetData):
		if not isinstance(targetData,pd.DataFrame):
			raise TypeError("targetData must be type of DataFrame")
		self.data = targetData

	def addColumn(self , colName , colData):
		if not isinstance(colName , str):
			raise TypeError(colName + " must be type of string.")
		if colName in self.data.columns.values.tolist():
			raise ValueError(colName + " is already a column in the dataframe.")

		self.data[colName] = colData

	def removeColumn(self , colName):
		if not isinstance(colName , str):
			raise TypeError(colName + " must be type of string.")
		if colName not in self.data.columns.values.tolist():
			raise ValueError(colName + " is not a column in the dataframe.")

		self.data.drop( colName, axis=1, inplace=True)

	def getColumn(self , colName):
		if not isinstance(colName , str):
			raise TypeError(colName + " must be type of string.")
		if colName not in self.data.columns.values.tolist():
			raise ValueError(colName + " is not a column in the dataframe.")

		return self.data[colName]


	def setColumn(self , colName , targetData):
		if not isinstance(colName , str):
			raise TypeError(colName + " must be type of string.")
		if colName not in self.data.columns.values.tolist():
			raise ValueError(colName + " is not a column in the dataframe.")

		self.data[colName] = targetData



	def getDataFromFile(self , fileName):

		#dateparse = lambda x: datetime.strptime(x, '%d.%m.%Y')

		if fileName.lower().endswith(".xlsx"):
			self.data = pd.read_excel( fileName , parse_dates=['Date'], date_parser=parse ,index_col = "Date")
		elif fileName.lower().endswith(".csv"):
			self.data = pd.read_csv( fileName , parse_dates=['Date'], date_parser=parse ,index_col = "Date")
		else:
			raise ValueError("unknown file name")

	def getDataStartToEnd(self , start_date , end_date , ds = "yahoo" ):
		if not isinstance(start_date , datetime):
			raise TypeError("start_date must be type of datetime.")
		if not isinstance(end_date , datetime):
			raise TypeError("end_date must be type of datetime.")
		if start_date > end_date:
			raise ValueError("start_date can not be bigger than end_date")		

		#self.data  = web.DataReader(self.name, data_source='yahoo', start = start_date, end = end_date)
		result_data = web.data.get_data_yahoo(self.name,  start = start_date, end = end_date)
		result_data.index = result_data.index.date
		self.setData(result_data)

	def getDataFromToday(self , day_count , ds = "yahoo"):
		""" backwards day_count day from today """
		delta_date = datetime.today() - timedelta(days=day_count)
		self.getDataStartToEnd(delta_date , datetime.today() , ds)


	def getDataStartUntil(self , start_date , day_count , ds = "yahoo"):
		delta_date = start_date + timedelta(days=day_count)
		if delta_date > datetime.today():
			raise ValueError("day_count exceeds")

		self.getDataStartToEnd(start_date , delta_date , ds)


	def isBalanced(self , otherInstrument):
		if self == otherInstrument:
			return True
		else:
			return self.getData().index.equals(otherInstrument.getData().index)


	def balanceDates(self , otherInstrument):
		if not isinstance(otherInstrument , Instrument):
			raise TypeError("otherInstrument must be type of Instrument")
		
		self.setData( self.getData().drop(self.getData().index.difference(otherInstrument.getData().index)) )
		otherInstrument.setData( otherInstrument.getData().drop(otherInstrument.getData().index.difference(self.getData().index)) )

	def divideInstrument(self , otherInstrument , instrumentName = None):
		if instrumentName is None:
			instrumentName = self.getName() + "_" + otherInstrument.getName()
		elif not isinstance(instrumentName , str):
			raise TypeError("instrumentName must be type of string.")


		main_copy = deepcopy(self)
		target_copy = deepcopy(otherInstrument)
		main_copy.balanceDates( target_copy)
		returnedInstrument = self.__class__( instrumentName )
		returnedInstrument.setData( main_copy.getData() / target_copy.getData() )
		returnedInstrument.setColumn("Volume" , main_copy.getColumn("Volume"))
		return returnedInstrument

	def generatePlot(self , columnNames):
		self.getData().plot(kind = 'line' , y = columnNames).get_figure().savefig(self.name + '.png')
		plt.close()

	def showPlot(self , columnNames):
		self.getData().plot(kind = 'line' , y = columnNames)
		mplcursors.cursor(hover=True)
		plt.show()

	def showSubPlot(self , columnNames):
		self.getData().plot(subplots=True, layout=(len(columnNames),1) , kind = 'line' , y = columnNames)
		mplcursors.cursor(hover=True)
		plt.show()

	def toExcel(self , path):
		if not path.lower().endswith(".xlsx"):
			raise ValueError("path extent must be .xlsx")

		self.getData().to_excel(path , sheet_name = datetime.today().strftime("%d_%m_%Y") )




