d=int(input("Введите день: ")) #Ввод дня с клавиатуры
m=int(input("Введите месяц: ")) #Ввод месяца с клавиатуры
if (m==1 and 1<=d<=31) or (m==2 and 1<=d<=28) or (m==12 and 1<=d<=31):
    print("Зима") 
elif (m==3 and 1<=d<=31) or (m==4 and 1<=d<=30) or (m==5 and 1<=d<=31):
    print("Весна")
elif (m==6 and 1<=d<=30) or (m==7 and 1<=d<=31) or (m==8 and 1<=d<=31):
    print("Лето")
elif (m==9 and 1<=d<=30) or (m==10 and 1<=d<=31) or (m==11 and 1<=d<=30):
    print("Осень")
else:
    print("Нет такой даты")