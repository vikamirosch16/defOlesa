a="67siygsj90whi4ja2"
def Olesa(a):
    b=0
    f=""
    for i in a:
        t=i.isdigit()
        if t==True: 
            f+=i
        else:
            if f!="":
                b+=int(f)
                f=""
    b+=int(f)    
    print(b)
Olesa(a)


