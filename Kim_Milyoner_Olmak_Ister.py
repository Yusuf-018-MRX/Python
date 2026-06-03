import random
import os
from datetime import datetime
from colorama import Fore, Style, init
init()
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
BLUE = Fore.BLUE
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL
MAGENTA = Fore.MAGENTA

FILENAME = "kim_mil_olmak.txt"
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write("\t\t\tKim Milyoner Olmak Ister\n\n")

def write_result(name, money):
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"\t\t\tKIM MILYONER OLMAK ISTER \n Tarixce\n\n{datetime.now().strftime('%Y-%m-%d %H:%M')}\nName:{name}\nMebleg:{money}$\n")#AI OXSASADA GOGLEDE datetime in python with file YAZANDA CIXIR ONSUZ OXSARLARI ORDAN DATETIME ALDIM SONRADA ONSUZ FAYILA VURDUMDA

print(CYAN + BOLD + "\n\t\t\t\t\t\t\t\tKIM MILYONER OLMAQ ISTER\n" + RESET)

riyaziyyat = {
    "Asan": [
        {"sual": "2 + 2 nədir?", "cavab": "4", "variantlar": ["3", "4", "5", "6"]},
        {"sual": "7 + 8 nədir?", "cavab": "15", "variantlar": ["14", "15", "16", "13"]},
        {"sual": "15 - 7 nədir?", "cavab": "8", "variantlar": ["7", "8", "9", "6"]},
        {"sual": "10 + 14 nədir?", "cavab": "24", "variantlar": ["23", "24", "25", "22"]},
        {"sual": "18 / 2 nədir?", "cavab": "9", "variantlar": ["8", "9", "10", "7"]},
        {"sual": "20 - 4 nədir?", "cavab": "16", "variantlar": ["15", "16", "17", "18"]},
    ],
    "Orta": [
        {"sual": "5 * 6 nədir?", "cavab": "30", "variantlar": ["20", "30", "25", "35"]},
        {"sual": "12 / 3 nədir?", "cavab": "4", "variantlar": ["2", "4", "6", "3"]},
        {"sual": "9 * 9 nədir?", "cavab": "81", "variantlar": ["80", "81", "79", "82"]},
        {"sual": "6 * 7 nədir?", "cavab": "42", "variantlar": ["40", "42", "44", "41"]},
    ],
    "Cətin": [
        {"sual": "8 × 7 neçə edir?", "cavab": "56", "variantlar": ["54", "56", "58", "60"]},
        {"sual": "144-ün kvadrat kökü neçədir?", "cavab": "12", "variantlar": ["10", "11", "12", "14"]},
        {"sual": "Bir ədədin 25%-i 50-dirsə, həmin ədəd neçədir?", "cavab": "200", "variantlar": ["100", "150", "200", "250"]},
        {"sual": "3² + 4² neçə edir?", "cavab": "25", "variantlar": ["21", "24", "25", "26"]},
        {"sual": "Bir düzbucaqlının tərəfləri 6 və 4-dür. Sahəsi neçədir?", "cavab": "24", "variantlar": ["20", "22", "24", "26"]},
    ]
}

money_talks = [0, 300, 700, 1000, 1350, 1600, 2000, 2300, 2600, 4500, 5000, 5400, 6000, 7000, 8000, 10000]

while True:
    cetinlik = ["Asan", "Orta", "Cətin"]
    devam = True
    name = input(GREEN+"Name:"+RESET)
    surname = input(GREEN+"Surname:"+RESET)
    if name == "" or surname == "" or name.isdigit() or surname.isdigit():
        print(RED+"Error: Melumatlar Duzgun Daxil edilmedi !!!"+RESET)
        break
    else:
        name2 = name.capitalize()
        sur = surname.capitalize()

    variant = ["A","B","C","D"]
    money = 0
    say = 0
    jokerler = {"50/50":True,"tamasaci":True,"dost":True}
    print(YELLOW+"\nQeyd:\n1.Yarisma sertlerini oyrenmek ucun 2209 daxil edin\n2.Istifadeci haqqinda melumat ucun 911 daxil edin\n"+RESET)

    for seviyye in cetinlik:
        if not devam:
            break
        
        suallar = riyaziyyat[seviyye].copy()
        random.shuffle(suallar)

        for index,sual in enumerate(suallar, 1):
            if not devam:
                break
            print(CYAN+f"{index}.{sual["sual"]}"+RESET) 
            variantlar =sual["variantlar"].copy() 
            random.shuffle(variantlar) 
            AB={} 
            for i,j in enumerate(variantlar, ord("A")): 
                AB[chr(i)] =j 
                print(BOLD+BLUE+f"{chr(i)}.{j}"+RESET)


            while True:
                print()
                print(MAGENTA+"Joker ucun \"J\" daxil edin"+RESET)
                cavab = input("Cavab:").upper()

                if cavab == "":
                    print(RED+"Error: Verilen cavab bosluq ola bilmez"+RESET)
                    continue

                if cavab == "J":
                    print(MAGENTA+"Jokerler: 1.50/50  2.Tamasaci  3.Dosta Zeng"+RESET)
                    secim = input("Secim:")
                    if secim not in ["1","2","3"]:
                        print(RED+"Yanlis joker secimi"+RESET)
                        continue
                    if secim == "1" and jokerler["50/50"]:
                        jokerler["50/50"]= False
                        duz_cavab=sual["cavab"]
                        yanlis=[]
                        for v in variantlar:
                            if v!=duz_cavab:
                                yanlis.append(v)
                        yanlis_cavab=random.choice(yanlis)        
                        AB={"A": duz_cavab, "B": yanlis_cavab}
                        print("A."+duz_cavab)
                        print("B."+yanlis_cavab
                              )
                    elif secim == "2" and jokerler["tamasaci"]:
                        jokerler["tamasaci"] = False
                        print(MAGENTA+"Tamasaci fikri: "+random.choice(variantlar)+RESET)

                    elif secim == "3" and jokerler["dost"]:
                        jokerler["dost"] = False
                        print(MAGENTA+"Dost deyir ki cavab:"+sual["cavab"]+RESET)
                    continue

                if cavab == "911":
                    print(YELLOW+f"Yarismaci: {name2} {sur}"+RESET )
                    devam = False
                    break
                elif cavab == "2209":
                    print(CYAN+"Sertler:\n1. Yarisma sadece A,B,C,D variantlarindan istifade ede biler\n2. Her turdan sonra suallar cetinlesir\n3. Yanlis cavab verildikde qazancda azalma olur\n4.Joker ucun 77 codesini vermek lazimdir"+RESET)
                    continue

                if cavab not in AB:
                    print(RED+"Error: Yanlis cavab tipi"+RESET)
                    devam = False
                    break
                
                    # if cavab not in AB and cavab not in ["J","911","2209"]:
                    #     print(RED+"Error: Yanlis cavab tipi"+RESET)
                    #     devam = False
                    #     break

                if AB[cavab]==sual["cavab"]:
                    money+=money_talks[min(say+1, len(money_talks)-1)]
                    print(GREEN+"\nduz_cavab cavab"+RESET)
                    print(GREEN+f"Qazanc: {money}$"+RESET)
                else:
                    money=max(0, money-300)
                    print(RED+"\nYanlis cavab!!"+RESET)
                    print(GREEN+f"Mebleg:{money}$"+RESET)
                    devam=False
                    break
                break
        if not devam:
            break
        say += 1
    if say == 15:#len(suallar):
        print(GREEN+f"Tebrikler, butun suallara cavab verdiniz!"+RESET)
        print(YELLOW+f"Yarismaci: {name2} {sur}"+RESET)
        print(GREEN+f"Qazanc: {money}$"+RESET)

    if not devam or say==len(suallar):
        try:
            print("1.Yeni oyun\n2.Oyunu sonlandir")
            secim1 = int(input("secim:"))
            if secim1 == 1:
                print("Yeni oyun baslayir...")
            elif secim1 == 2:
                print("Oyun sonlandirildi......")
                break
            else:
                print(RED+"Sadece verilen secimler daxil oluna biler !!"+RESET)
                break
        except ValueError:
            print(RED+"Error: seciminiz sadece int ile ede bilersiniz !"+RESET)
            break
