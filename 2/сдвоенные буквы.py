a='усвоенный'
def Olesa(a):
    for i in range (len(a)-1):
        m=a[i]
        n=a[i+1]
        if (m==n) :
          print (True)
        else:
          print('Отстань')
    
Olesa(a)