from gmpy2 import *
from itertools import permutations

def str2word(m):
    return ''.join([chr(int(b, 16)) for b in [m[i:i+2] for i in range(0, len(m), 2)]])
    


n=['a' for i in range(21)]
for i in range(21):
    f=open('D:/python/RSA/3/3-2/Frame'+str(i)).read()
    n[i]=int(f[:256],16)

x=[]
for i in range(21):
    x.append(i)
for i,j in permutations(x,2):
    t=int(gcd(n[i],n[j]))
    if t!=1 and n[i]!=n[j]:
        print 'i='+str(i),'j='+str(j)
        print 'n[i]:',n[i],'\n', 'n[i]:',n[j]
        print 't:',t
        print'#'*72

#i=18,j=1
p=int(gcd(n[18],n[1]))
n18=n[18]
q18=n18/p
print 'q18=',q18

n1=n[1]
q1=n1/p
print 'q1=',q1

print'#'*72


def m(i,p,q,n):#i:str
    fi=open('D:/python/RSA/3/3-2/Frame'+i).read()
    ei=int(fi[256:512],16)
    ci=int(fi[512:],16)
    print 'e'+i,ei
    print 'c'+i,ci
    fni=(p-1)*(q-1)
    di=int(invert(ei,fni))
    m_i=hex(pow(ci,di,n))[-17:-1]
    print 'm_'+i,m_i
    mi=str2word(m_i)
    print 'm'+i,mi
    return mi
    
m18=m('18',p,q18,n18)
m1=m('1',p,q1,n1)




'''
f18=open('D:/python/RSA/3/3-2/Frame'+str(18)).read()
e18=int(f18[256:512],16)
c18=int(f18[512:],16)
print 'e18:',e18
print 'c18:',c18
fn18=(p-1)*(q18-1)
d18=int(invert(e18,fn18))
m_18=hex(pow(c18,d18,n18))[-17:-1]
print 'm_18:',m_18
m18=str2word(m_18)
print 'm18=',m18
'''
       
