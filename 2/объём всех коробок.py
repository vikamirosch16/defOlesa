m=[[5,7,9],[9,3,8],[2,6,4]]
d=0
def Olesa(m,d):
    for i in range(len(m)):
        d+=(m[i][0])*(m[i][1])*(m[i][2])
    print(d)
Olesa(m,d)