import time 
def calculate_time(function):
	def start():
		start = time.time()
		function()
		end = time.time()
		print("Total time ",end - start)
	return start


	
