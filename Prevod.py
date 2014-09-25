while True:
    print ("_______Начало______")
    print ("Ваше число дробное? \r\nBведите Y, если да.\r\nВведите N, если нет.")
    drobcheck = input()
    if drobcheck.upper() == "N":
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
        
    elif drobcheck.upper() == "Y":
        print ("число 1: ")
        rawDrob= input()
        print ("система 1: ")
        b= int(input())
        print ("система 2: ")
        d= int(input())
        print ("Сколько знаков после запятой?")
        pastzap= int(input())
        q=0
        j=rawDrob[q]
        cel=""
        drob=""
        while j !="," and j != ".":
            cel += j
            q+=1
            j=rawDrob[q]
        q+=1
        while q < len(rawDrob):
            drob+=rawDrob[q]
            q+=1
        #______________________________________
        perehod = 0
        dlina=len(cel)-1
        for i in  cel:
            perehod+= int(i)* (b**dlina)
            dlina-=1

        cel=''
        while perehod>0:
            cel=str(perehod%d)+cel
            perehod=perehod//d
        #__________________________________________
        perehod1 = 0
        dlina1=-1 #len(drob)
        
        for r in  drob:
            perehod1+= int(r)* (b**dlina1)
            dlina1-=1
        drob=""
        #perehod1=perehod1*(10**-(len(str(perehod1))))
        perehod2=""
        i=0
        for k in str(perehod1):
            perehod2+=k
            i+=1
            if i == 15: break
        perehod1=float(perehod2)
        i=0
        print(perehod1,b,dlina1,d)
        import math
        while i<pastzap:
            drob+=str(math.floor(perehod1*d))
            if(math.floor(perehod1*d)!=0):
                perehod1=perehod1*d - math.floor(perehod1*d)
            else:
                perehod1=perehod1*d
            i+=1
       # while perehod1>0:
       #     drob=str(perehod1%d)+drob
       #     perehod1=perehod1//d
        print ("Ваше число:",cel,",",drob)
        break
    
    else:
        print("Я Вас не понял. Введите Y или N")
