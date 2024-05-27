from enum import Enum
from collections import deque

class Boat(Enum):
	LEFT = 1
	RIGHT = 2

class Move:
	def __init__(self, boat, left_sheep, left_wolves, right_sheep, right_wolves):
		self.prev = None
		self.boat = boat
		self.left_sheep = left_sheep
		self.left_wolves = left_wolves
		self.right_sheep = right_sheep
		self.right_wolves = right_wolves

	def __eq__(self, other):
		return (self.boat == other.boat \
			and self.left_sheep == other.left_sheep \
			and self.left_wolves == other.left_wolves \
			and self.right_sheep == other.right_sheep \
			and self.right_wolves == other.right_wolves)

	def is_valid(self):
		"""This seems like it should work, but it doesn't because of when sheep = 0 
			and wolves > 0 on one side
		return self.left_sheep >= self.left_wolves \
			and self.right_sheep >= self.right_wolves \
			and self.left_sheep >= 0 and self.left_wolves >= 0 \
			and self.right_sheep >= 0 and self.right_wolves >= 0 #"""
		return (self.left_sheep >= self.left_wolves or self.left_sheep == 0) \
			and (self.right_sheep >= self.right_wolves or self.right_sheep == 0) \
			and self.left_sheep >= 0 and self.left_wolves >= 0 \
			and self.right_sheep >= 0 and self.right_wolves >= 0 #"""

	def all_across(self, initial_sheep, initial_wolves):
		return self.boat == Boat.RIGHT and self.left_sheep == 0 \
				and self.left_wolves == 0 and self.right_sheep == initial_sheep \
				and self.right_wolves == initial_wolves

class SemanticNetsAgent:

	def __init__(self):
		pass

	def get_next_moves(self, current):
		next_moves = []
		boat_capacities = None
		if current.boat == Boat.LEFT:  
			if(current.left_sheep > current.left_wolves):
				boat_capacities = [(2,0), (1,1), (1,0), (0,2), (0,1)]
			else: 
				boat_capacities = [(1,1), (1,0), (0,1), (2,0), (0,2)]
			for capacity in boat_capacities:
				next_move = Move(Boat.RIGHT, current.left_sheep - capacity[0], \
					current.left_wolves - capacity[1], \
					current.right_sheep + capacity[0], \
					current.right_wolves + capacity[1])
				if next_move.is_valid():
					next_moves.append(next_move)
					next_move.prev = current
		else:  
			boat_capacities = [(1,0), (0,1), (1,1), (0,2), (2,0)]
			for capacity in boat_capacities:
				next_move = Move(Boat.LEFT, current.left_sheep + capacity[0], \
					current.left_wolves + capacity[1], \
					current.right_sheep - capacity[0], \
					current.right_wolves - capacity[1])
				if next_move.is_valid():
					next_moves.append(next_move)
					next_move.prev = current
		return next_moves

	def search(self, initial_sheep, initial_wolves):  # breadth first
		start = Move(Boat.LEFT, initial_sheep, initial_wolves, 0, 0)
		if start.all_across(initial_sheep, initial_wolves):
			return start
		# faster, but takes more steps:
		#frontier = [] 
		# slower, but takes fewer steps
		frontier = deque([])
		frontier.append(start)
		searched = []
		while len(frontier) > 0:
			# if frontier is list:
			#state = frontier.pop() 
			# if frontier is dequeue:
			state = frontier.popleft()
			if state.all_across(initial_sheep, initial_wolves):
				return state
			searched.append(state)
			moves = self.get_next_moves(state)
			for move in moves:
				if (move not in searched) and (move not in frontier):
					frontier.append(move)
		return None

	def get_solution_from_search(self, search_result):
		parent = search_result.prev
		paths = []
		end_paths = []
		while parent:
			move = (abs(search_result.left_sheep - parent.left_sheep), \
				abs(search_result.left_wolves - parent.left_wolves))
			paths.append(move)
			search_result = parent
			parent = search_result.prev
		for x in range(len(paths)):
			end_result = paths[len(paths) - 1 - x]
			end_paths.append(end_result)
		return end_paths

	def solve(self, initial_sheep, initial_wolves):
		result = self.search(initial_sheep, initial_wolves)
		
		if result:
			return self.get_solution_from_search(result)
		else:
			return []
