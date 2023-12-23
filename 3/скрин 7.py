p='gjus?99_!E'
a=[]
m='сложность пароля - '
d=1
for i in range(len(p)):
    if p[i].isdigit()==True:
        a.append(d)
        break
for i in range(len(p)):
    if p[i]=='_' or p[i]=='?' or p[i]=='=': 
        a.append(d)
        break
if len(p)>7:
    a.append(d)
for i in range(len(p)):
    if p[i].isalpha()==True:
        if p[i]==p[i].upper():
          a.append(d)
          break
for i in range(len(p)):
    if p[i]==':':
        a.append(d)
        break
s=sum(a)
g=m+str(s)
print(g)
    

