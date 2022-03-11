def doubler(function):
	def double():
		function()
		function()
	return double
	
