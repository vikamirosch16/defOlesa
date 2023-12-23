a=["Олеся", "Соня", "Никита", "Ваня"]
b=["Никита", "Ваня" ]
def olesa(a,b):
    for i in range (len(b)):    
        if a.count(b[i])>0:
            a.remove(b[i])
olesa(a,b)
print(a) 
 # for i in range (len(a)):
 #  e=a[i]
 #  for i in range (len(a)):
 #      m=b[i]
 #      if e==m:
 #          del c[i]

          