Ikood=""
while len(Ikood) != 11 or Ikood.isdigit()!= True:
    try:
        Ikood=input("Isikukood: ")
    except ValueError:
        print("Viga andmetega")
print("Isikukoodi analüüs: ".center(50, "-"))
print("Esimene sümbol: ")
Ikood_list=list(Ikood)
if int(Ikood_list[0]) not in [1, 2, 3, 4, 5, 6]:
    print(f"{Ikood_list[0]} - Vale sumbol")
else:
    print(Ikood_list[0], "Oige sumbol")
    kuu=Ikood_list[3]+Ikood_list[4]
    kuu=int(kuu)
    if kuu>0 and kuu<13:
        print(Ikood_list[3], Ikood_list[4], "Oiged andmed")
        paev=int(Ikood_list[5]+Ikood_list[6])
        if int(Ikood_list[0])==1 or int(Ikood_list[0])==2:
            aasta=int("18"+Ikood_list[1]+Ikood_list[2])
        elif int(Ikood_list[0])==3 or int(Ikood_list[0])==4:
            aasta=int("19"+Ikood_list[1]+Ikood_list[2])
        elif int(Ikood_list[0])==5 or int(Ikood_list[0])==6:
            aasta=int("20"+Ikood_list[1]+Ikood_list[2])
        if kuu in [1,3,5,7,8,10,12] and paev>0 and paev<32:
            print(Ikood_list[5], Ikood_list[6], "Oige paev")
        elif (kuu in [4,6,9,11] and paev>0 and paev<32) or( kuu==2 and paev>0 and paev<29):
            print(Ikood_list[5], Ikood_list[6], "Oige paev!")
        elif aasta % 4==0 and kuu == 2 and paev>0 and paev<30:
            print(Ikood_list[5], Ikood_list[6], "Oige paev! 29 vebruaar")
        else:
            print(Ikood_list[5], Ikood_list[6], "Vale paev")
          
    else:
        print(Ikood_list[3], Ikood_list[4], "Pole Oiged andmed")
Summa=0
for i in range(1, 11):
    if i<10:
        Summa+=i*int(Ikood_list[i-1])
    else:
        Summa+=(i-9)*int(Ikood_list[i-1])
print("Summa: ", Summa)
jaak=Summa//11
if jaak==10:
    Summa=0
    for i in range(3,13):
        if i<=9:
            Summa+=i*int(Ikood_list[i-1])
        else:
            Summa+=(i-9)*int(Ikood_list[i-1])
    jaak=Summa//11
jaak=Summa-jaak*11
if jaak==int(Ikood_list[10]):
    print("Isikukood on oige!")
else:
    print("Isikukood on vale")
 
#aasta Ikood_list[1], Ikood_list[2]
#kuu Ikood_list[3], Ikood_list[4]
#paev Ikood_list[5], Ikood_list[6]
