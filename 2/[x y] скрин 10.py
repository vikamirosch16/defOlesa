a=[1,2,3,4]
b=[5,6,7,8]
c=[]
print(len(c))
def Olesa(a, b, c):
    for i in range (len(a)):
        h=a[i]
        k=b[i]
        m=str(h)+';'+ str(k)
        c.append(m)
    print(c)  
Olesa(a,b,c)    

