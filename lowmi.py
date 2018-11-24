from gmpy2 import *
import math

def multiply(a,b,c,d,e):
    return (((a*b%e)*c)%e)*e

def read(i):#i:str
    fi=open('D:/python/RSA/3/3-2/Frame'+i).read()
    ni=int(fi[:256],16)
    ei=int(fi[256:512],16)
    ci=int(fi[512:],16)
    return ni,ei,ci

n7,e7,c7=read('7')
n11,e11,c11=read('11')
n15,e15,c15=read('15')

print 'e7:',e7
print 'e11:',e11
print 'e15:',e15

n7i=int(invert(n11*n15,n7))
n11i=int(invert(n7*n15,n11))
n15i=int(invert(n7*n11,n15))
N=n7*n11*n15
M=(c7*n7i*n11*n15+c11*n11i*n7*n15+c15*n15i*n7*n11)%N
m=pow(M,1./3)
print m
