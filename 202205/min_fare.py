
min_so_far = float('inf')
min_route = None

def create_graph(data):
	graph = {}
	for row in data:
		s, d, f = row
		if s not in graph:
			graph[s] = {d: f}
		else:
			graph[s][d] = f
	print(graph)
	return graph
	
def find_min_route(s, d, g, fare=0, route=[]):
	global min_so_far
	global min_route
	if s is None:
		return
	if s == d:
		if fare < min_so_far:
			min_so_far = fare
			min_route = route + [d]
	else:
		if s not in route:
			if s not in g:
			 return
			for n in g[s]:
				find_min_route(n, d, g, fare+g[s][n], route+[s])
	

data = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]


g = create_graph(data)
s = 'JFK'
d = 'LAX'
find_min_route(s, d, g, fare=0, route=[])
print(min_route, min_so_far)
