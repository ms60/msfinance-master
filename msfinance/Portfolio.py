from msfinance.Instrument import Instrument
import pandas as pd
from datetime import datetime

class Portfolio:
	def __init__(self , portfolioName ):
		self.portfolioName = portfolioName
		self.instruments = pd.DataFrame(columns=["Instrument Name" , "Instrument Data" , 
			"Instrument Signals Data" , "BUY Signal Count" , "SELL Signal Count" ,
			"NEUTRAL Signal Count" , "NULL Signal Count"])

	def __str__(self):
		return self.instruments.to_string()

	def __repr__(self):
		return self.instruments.to_string()

	def addInstrument(self , targetInstrument):
		if not isinstance(targetInstrument , Instrument):
			raise TypeError("targetInstrument must be type of Instrument")


		    