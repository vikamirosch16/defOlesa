a=int(input())
s=str(a)
f=":00"
b=input("")
print(s+b)
if b=="am":
    print("24 часовой режим-" +s+f)
else:
    d=a+12
    i=str(d)
    print("12 часовой режим-" +i+f)