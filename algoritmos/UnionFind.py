v = []

class QuickFindUF(object):
	"""docstring for QuickFindUF"""
	
	def __init__(self, N):
		for i in range(0, N):
			v.append(i)

	def connected(self, p, q):
		return v[p] == v[q]

	def union(self, p, q):
		pv = v[p]
		qv = v[q]

		for i in range(0, len(v)):
			if v[i] == pv[i]:
				v[i]=qv[i]


def main():
	N = int(raw_input())

	uf = QuickFindUF(N)

	while(N>=0):
		p = int(raw_input())
		q = int(raw_input())

		if(uf.connected(p,q)):
			uf.union(p, q)
			println(str(p)+" "+ str(q))

		N -=1

main()

