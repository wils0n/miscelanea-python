

class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.node_neighbors={}

	def add_nodes(self, nodes):
		for node in nodes:
			self.add_node(node)

	def add_node(self, node):
		"""agregando nodo al grafo"""
		if node not in self.node_neighbors:
			self.node_neighbors[node] = {}
		else:
			raise Exception("Node %s is already in graph" % node)
	
	def has_node(self, node):
		"""
		Retorna un boolean para indicar si existe el nodo en el grafo
		"""		
		return node in self.node_neighbors

	def neighbors(self, node):
		"""
		Returns a list of neighbors for a node
		"""
		if not self.has_node(node):
			raise "Node %s not in graph" % node
		return self.node_neighbors[node].keys()