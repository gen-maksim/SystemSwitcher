while True:
    print ("_______Начало______")
    print ("число 1: ")
    a= int(input())
    print ("система 1: ")
    b= int(input())
    print ("система 2: ")
    d= int(input())
    perehod=0
    c=str(a)
    dlina=len(c)-1
    for i in  c:
        perehod+= int(i)* (b**dlina)
        dlina-=1

    c=''
    while perehod>0:
        c=str(perehod%d)+c
        perehod=perehod//d
    print ("Число ", a ," в ", d ,"-й системе счисления выглядит как:",c)
    print ("""Чтобы закончить программу введите "N". \r\nЧтобы продолжить нажмите Enter.""")
    vihod = input()
    vihod = vihod.upper()
    if vihod == "N":
        break
