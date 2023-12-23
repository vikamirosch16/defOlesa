a='1, 5, 8, 9'
s=1
b=[]
def Olesa(a,s):
    for i in range (len(a)):
        if a[i]!=" " and a[i]!= ",":
            n=int(a[i])
            b.append(n)
        print(b)
        for i in b:
            s=s*i
        print(s)
Olesa(a,s)