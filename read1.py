n=['a' for i in range(21)]
for i in range(21):
    f=open('D:/python/RSA/3/3-2/Frame'+str(i)).read()
    n[i]=int(f[:256],16)
    print(i,n[i])

