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