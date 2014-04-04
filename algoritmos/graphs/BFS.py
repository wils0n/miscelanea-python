from collections import deque

graph = {
			'1': ['2', '3', '4'], 
			'2': ['5', '6'], 
			'5': ['9', '10'], 
			'4': ['7', '8'], 
			'7': ['11', '12'] 
		}

def bfs(graph, start, end):
	Q = deque()
	Q.append([start])
	while Q:
		path = Q.popleft()

		node = path[-1]
		print "path: ", path

		if node == end:
			return path
		for adjacent in graph.get(node, []):
			new_path = list(path)
			new_path.append(adjacent)
			Q.append(new_path)
		print "queue: ", Q

print bfs(graph, '1', '11')
