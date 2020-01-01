from .unibit import UniBit as ub

class ForexRate(ub):

	def getRealtimeForexRates(self, base, foreign, amount, startDate, endDate, startMinute, endMinute, selectedFields = "all", datatype = "json"):

		if isinstance(foreign, list):
			temp = "";
			for item in foreign:
				temp = temp + item + ","
			foreign = temp

		if isinstance(amount, str):
			temp = int (amount)
			amount = temp

		endpoints = 'forex/realtime'

		return self.make_request(endpoints=endpoints, data={'base': base, 'foreign': foreign, 'amount':amount, 'startDate': startDate, 'endDate': endDate, 'startMinute': startMinute, 'endMinute': endMinute, 'datatype':datatype})

	def getHistoricalForexRates(self, base, foreign, amount, startDate, endDate, startMinute, endMinute, selectedFields = "all", datatype = "json"):

		if isinstance(foreign, list):
			temp = "";
			for item in foreign:
				temp = temp + item + ","
			foreign = temp

		if isinstance(amount, str):
			temp = int (amount)
			amount = temp

		endpoints = 'forex/historical'

		return self.make_request(endpoints=endpoints, data={'base': base, 'foreign': foreign, 'amount':amount, 'startDate': startDate, 'endDate': endDate, 'startMinute': startMinute, 'endMinute': endMinute, 'datatype':datatype})
