m=[1,3,5,4,9]
o = 0
def Olesa(m,o):
    for i in range(len(m)-1):
       if m[i]<m[i+1]:
           o = o + 1
    if o>=(len(m)-1):
     print("Возрастает")
    else:
     print("Не возрастает")
Olesa(m,o)
