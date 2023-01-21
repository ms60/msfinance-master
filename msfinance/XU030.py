#from enum import Enum
class XU030_META(type):
	def __iter__(self):
		for attr in vars(self):
			if not attr.startswith("__"):
				yield vars(self)[attr]

	def __getitem__(self,key):
		return [x for x in self][key] 

class XU030( metaclass = XU030_META ):

	AKBNK = 'AKBNK.IS'
	ARCLK = 'ARCLK.IS'
	ASELS = 'ASELS.IS'
	BIMAS = 'BIMAS.IS'
	EKGYO = 'EKGYO.IS'
	EREGL = 'EREGL.IS'
	FROTO = 'FROTO.IS'
	GARAN = 'GARAN.IS'
	GUBRF = 'GUBRF.IS'
	HALKB = 'HALKB.IS'
	HEKTS = 'HEKTS.IS'
	ISCTR = 'ISCTR.IS'
	KCHOL = 'KCHOL.IS'
	KOZAA = 'KOZAA.IS'
	KOZAL = 'KOZAL.IS'
	KRDMD = 'KRDMD.IS'
	PETKM = 'PETKM.IS'
	PGSUS = 'PGSUS.IS'
	SAHOL = 'SAHOL.IS'
	SASA = 'SASA.IS'
	SISE = 'SISE.IS'
	TAVHL = 'TAVHL.IS'
	TCELL = 'TCELL.IS'
	THYAO = 'THYAO.IS'
	TKFEN = 'TKFEN.IS'
	TOASO = 'TOASO.IS'
	TTKOM = 'TTKOM.IS'
	TUPRS = 'TUPRS.IS'
	VESTL = 'VESTL.IS'
	YKBNK = 'YKBNK.IS'
