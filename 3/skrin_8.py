a=int(input())
def Olesa(a):
    b = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    c = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    d = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    if a == 0 :
        print("ноль")
    Vika=a%10
    Sonja=(a//10)%10
    Olesa=a//100
    n=hundreds[Olesa]+" "
    if Sonja==1:
        n+=c[Vika]
    elif Sonja==0:
        n+=b[Vika]
    else:
        n+=d[Sonja]+" "+b[Vika]
    print(n.strip())
Olesa(a)