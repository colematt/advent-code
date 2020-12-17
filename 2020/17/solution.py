#!/usr/bin/env python3

import itertools

class Universe3:
	"""
	Simulation of a pocket dimension, consisting of 3D points behaving similar 
	to Conway's game of life
	"""

	def __init__(self, actives=None):
		if actives: self.active = set(actives)
		else: self.active = set()
		self.t = 0
	
	def __repr__(self):
		if self.active:
			return 'Universe3(active={0})'.format(repr(self.active))
	
	def __str__(self):
		output = 't={0}\n'.format(self.t)
		if self.active:
			minz = min(z for x,y,z in self.active)
			maxz = max(z for x,y,z in self.active)
			for plane in range(minz, maxz+1):
				output += 'z={0}\n'.format(plane)
				for tup in self.active:
					x,y,z = tup
					if z == plane: 
						output += '({0},{1},{2}) '.format(x,y,z)
				output += '\n'
		else:
			output += 'No active points\n'
		return output
	
	@staticmethod
	def parse(filename):
		"""
		Return a Universe3 object from the input in filename
		"""
		with open(filename, 'r') as fin:
			cells =[[col for col in str(line.rstrip())] for line in fin.readlines()]
			actives = set()
			for y in range(len(cells)):
				for x in range(len(cells[y])):
					if cells[x][y] == '#':
						actives.add((x,y,0))
		return Universe3(actives)
		
	def neighbors(self,point,active=True):
		"""
		Given a 3-tuple point, return a list of neighboring point 3-tuples.
		If active, only return neighboring points which are active.
		"""
		vectors = [v for v in itertools.product((-1,0,1), repeat=3) if v != (0,0,0)]
		z = zip(itertools.repeat(point),vectors)
		ns = list(itertools.starmap(lambda p,v: (p[0]+v[0],p[1]+v[1],p[2]+v[2]), z))
		if active:
			return list(filter(lambda p: p in self.active, ns))
		else:
			return ns
	
	def points(self):
		"""
		Return a list of all points in the Universe. 
		These points are within 1 unit of any of xmin/xmax, ymin/ymax, zmin/zmax
		"""
		minx, maxx = min(x for x,y,z in self.active), max(x for x,y,z in self.active)
		miny, maxy = min(y for x,y,z in self.active), max(y for x,y,z in self.active)
		minz, maxz = min(z for x,y,z in self.active), max(z for x,y,z in self.active)
		
		xs = tuple(x for x in range(minx-1,maxx+2))
		ys = tuple(y for y in range(miny-1,maxy+2))
		zs = tuple(z for z in range(minz-1,maxz+2))
		return [tuple(p) for p in itertools.product(xs,ys,zs)]
		
	def step(self):
		"""
		Advance one unit of time forward. All points simultaneously update.
		"""
		temp = set() 
		points = self.points()
		for point in points:
			# Get the active neighbors
			ns = self.neighbors(point, active=True)
			
			# Calculate the next state for this point, 
			# add to temp if it will be active
			# Point is currently active
			if point in self.active:
				if len(ns) == 2 or len(ns) == 3: temp.add(point)
			# Point is not currently active
			else:
				if len(ns) == 3: temp.add(point)
		self.active = temp
		self.t += 1

class Universe4:
	"""
	Simulation of a pocket dimension, consisting of 4D points behaving similar 
	to Conway's game of life
	"""
	
	def __init__(self, actives=None):
		if actives: self.active = set(actives)
		else: self.active = set()
		self.t = 0
		
	def __repr__(self):
		if self.active:
			return 'Universe4(active={0})'.format(repr(self.active))
		
	def __str__(self):
		output = 't={0}\n'.format(self.t)
		if self.active:
			minz = min(z for x,y,z,w in self.active)
			maxz = max(z for x,y,z,w in self.active)
			minw = min(w for x,y,z,w in self.active)
			maxw = max(w for x,y,z,w in self.active)
			for planez in range(minz, maxz+1):
				for planew in range(minw, maxw+1):
					output += 'z={0}, w={1}\n'.format(planez, planew)
					for tup in self.active:
						x,y,z,w = tup
						if z == planez and w == planew: 
							output += '({0},{1},{2},{3}) '.format(x,y,z,w)
					output += '\n'
		else:
			output += 'No active points.\n'
		return output
	
	@staticmethod
	def parse(filename):
		"""
		Return a Universe4 object from the input in filename
		"""
		with open(filename, 'r') as fin:
			cells =[[col for col in str(line.rstrip())] for line in fin.readlines()]
			actives = set()
			for y in range(len(cells)):
				for x in range(len(cells[y])):
					if cells[x][y] == '#':
						actives.add((x,y,0,0))
		return Universe4(actives)
	
	def neighbors(self,point,active=True):
		"""
		Given a 4-tuple point, return a list of neighboring point 4-tuples.
		If active, only return neighboring points which are active.
		"""
		vectors = [v for v in itertools.product((-1,0,1), repeat=4) if v != (0,0,0,0)]
		z = zip(itertools.repeat(point),vectors)
		ns = list(itertools.starmap(lambda p,v: (p[0]+v[0],p[1]+v[1],p[2]+v[2],p[3]+v[3]), z))
		if active:
			return list(filter(lambda p: p in self.active, ns))
		else:
			return ns
		
	def points(self):
		"""
		Return a list of all points in the Universe. 
		These points are within 1 unit of any of xmin/xmax, ymin/ymax, zmin/zmax
		"""
		minx, maxx = min(x for x,y,z,w in self.active), max(x for x,y,z,w in self.active)
		miny, maxy = min(y for x,y,z,w in self.active), max(y for x,y,z,w in self.active)
		minz, maxz = min(z for x,y,z,w in self.active), max(z for x,y,z,w in self.active)
		minw, maxw = min(w for x,y,z,w in self.active), max(w for x,y,z,w in self.active)
		
		xs = tuple(x for x in range(minx-1,maxx+2))
		ys = tuple(y for y in range(miny-1,maxy+2))
		zs = tuple(z for z in range(minz-1,maxz+2))
		ws = tuple(w for w in range(minw-1,maxw+2))
		return [tuple(p) for p in itertools.product(xs,ys,zs,ws)]
	
	def step(self):
		"""
		Advance one unit of time forward. All points simultaneously update.
		"""
		temp = set() 
		points = self.points()
		for point in points:
			# Get the active neighbors
			ns = self.neighbors(point, active=True)
			
			# Calculate the next state for this point, 
			# add to temp if it will be active
			# Point is currently active
			if point in self.active:
				if len(ns) == 2 or len(ns) == 3: temp.add(point)
			# Point is not currently active
			else:
				if len(ns) == 3: temp.add(point)
		self.active = temp
		self.t += 1

def test():
	#### PART 1 ####
	# Read the input file and get a Universe3 instance
	cube = Universe3.parse('test.txt')
	
	# Execute six cycles
	for _ in range(6):
		cube.step()
	
	# Count the number of active points
	assert len(cube.active) == 112
	
	#### PART 2 ####
	# Read the input file and get a Universe4 instance
	hypercube = Universe4.parse('test.txt')
	
	# Execute six cycles
	for _ in range(6):
		hypercube.step()
		
	# Count the number of active points
	assert len(hypercube.active) == 848
	
def main():
	#### PART 1 ####
	# Read the input file and get a Universe3 instance
	cube = Universe3.parse('input.txt')
	
	# Execute six cycles
	for _ in range(6):
		cube.step()
		
	# Count the number of active points
	print(len(cube.active))
	
	#### PART 2 ####
	# Read the input file and get a Universe4 instance
	hypercube = Universe4.parse('input.txt')
	
	# Execute six cycles
	for _ in range(6):
		hypercube.step()
		
	# Count the number of active points
	print(len(hypercube.active))
	
if __name__ == "__main__":
	test()
	main()
	