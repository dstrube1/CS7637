import time
from SemanticNetsAgent import SemanticNetsAgent

def get_time(seconds):
	def get_s_unit(seconds):
		if int(seconds) == 1:
			return " second"
		else:
			return " seconds"
	def get_m_unit(minutes):
		if int(minutes) == 1:
			return " minute"
		else:
			return " minutes"
			
	if int(seconds / 60) == 0:
		if int(seconds) == 0:
			return str(round(seconds,5)) + get_s_unit(seconds)
		return str(int(seconds)) + get_s_unit(seconds)
	minutes = int(seconds / 60)
	seconds = int(seconds % 60)
	# Assuming this won't be called for any time span greater than 60 minutes
	return str(minutes) + get_m_unit(minutes) + " and " + str(seconds) + get_s_unit(seconds)
		
def test():
	#This will test your SemanticNetsAgent
	#with seven initial test cases.
	test_agent = SemanticNetsAgent()

	print(test_agent.solve(1, 1))
	print(test_agent.solve(2, 2))
	print(test_agent.solve(3, 3))
	print(test_agent.solve(5, 3))
	print(test_agent.solve(6, 3))
	print(test_agent.solve(7, 3))
	print(test_agent.solve(5, 5))

	start = time.time()
	solution = test_agent.solve(51, 50)
	print(solution)
	end = time.time()
	print("Done in " + get_time(end - start) + " with " + str(len(solution)) + " steps")

	start = time.time()
	solution = test_agent.solve(100, 50)
	print(solution)
	end = time.time()
	print("Done in " + get_time(end - start) + " with " + str(len(solution)) + " steps")

	start = time.time()
	solution = test_agent.solve(100, 99)
	print(solution)
	end = time.time()
	print("Done in " + get_time(end - start) + " with " + str(len(solution)) + " steps")

	start = time.time()
	solution = test_agent.solve(100, 1)
	print(solution)
	end = time.time()
	print("Done in " + get_time(end - start) + " with " + str(len(solution)) + " steps")

	start = time.time()
	solution = test_agent.solve(200, 100)
	print(solution)
	end = time.time()
	print("Done in " + get_time(end - start) + " with " + str(len(solution)) + " steps")

if __name__ == "__main__":
	test()