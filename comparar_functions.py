'''
Cual será el tipo y valor de la salida?
'''

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

print b(a, b)
print a(3>2, a, b)