a=input()
c=input()
if a==c:
    print("")
else:
    if a=="Ножницы" and c=="Бумага":
        print("Выйграл 1 игрок")
    elif a=="Ножницы"  and c=="Камень":
         print("Выиграл 2 игрок")
    elif a=="Бумага"  and c=="Камень":
             print("Выиграл 2 игрок")
    elif a=="Бумага"  and c=="Ножницы":
         print("Выиграл 2 игрок")
    elif a=="Камень"  and c=="Бумага":
             print("Выиграл 2 игрок")  
    elif a=="Камень"  and c=="Ножницы":
              print("Выиграл 1 игрок")         