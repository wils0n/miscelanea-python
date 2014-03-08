#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lotsOfParameters1(a,b,c,d,e):
	print a
	print b
	print c
	print d
	print e

''' 
1) ¿cuál es la opción incorrecta? 
'''

#a
lotsOfParameters1(1, e=5, d=4, c=3, b=2)

#b
lotsOfParameters1(a=5, b=1, c=4, d=2, 3)


#############################################################

def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg



'''
2) de acuerdo a la siguiente función ¿cuáles corresponden a *args y a f_args?

a)
*args: 'yasoob', python', 'eggs', 'test'
f_args: 'yassob'

b) 
*args: python', 'eggs', 'test'
f_args: 'yassob'

'''
test_var_args('yasoob','python','eggs','test')





































'''
1) Rpta: la opción incorrecta es la opción b), porque en el orden de *args y **kwargs, es *args primero y **kwargs segundo
2) Rpta: la opción correcta es la opcion b)
'''