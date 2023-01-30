class COMMON_META(type):
	def __iter__(self):
		for attr in vars(self):
			if not attr.startswith("__"):
				yield vars(self)[attr]

	def __getitem__(self,key):
		return [x for x in self][key] 

class COMMON( metaclass = COMMON_META ):
	USD_TRY = "TRY=X"
	EUR_TRY = "EURTRY=X"
	XAU_USD = "GC=F"
	XAG_USD = "SI=F"
	CRUDE_OIL = "CL=F"
	XU100_SUST_INDEX = "XUSRD.IS"
	XU100_INDEX = "XU100.IS"
	XGIDA_INDEX = "XGIDA.IS"
	XUSIN_INDEX = "XUSIN.IS"
	XTRZM_INDEX = "XTRZM.IS"