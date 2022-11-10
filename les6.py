import os
print("Welkom bij de online Winkel-Mandje!!\nHier kan je dingen toevoegen aan je lijst!")
MyList = []
while True:
    Question = input("Wil  je nog iets Toevoegen aan jouw lijs? Type dan: T \nWil je nog iets verwijderen van je  lijst? Type dan: V\nWil je nog iets stoppen met je  Winkel-Mandje? Type dan: S\nType hier je keuze: ")
    if Question == 'T':
        os.system("cls")
        toevoeging = input("Wat wil je toevoegen aan de lijst??: ")
        MyList.append(toevoeging)
        print("Jouw lijst bevat de volgende dingen: ")
        print(MyList)
    elif Question == 'V':
        verwijdering = input("Wat wil je verwijderen van de lijst?")
        MyList.remove(verwijdering)
        print("Jouw lijst bevat de volgende dingen: ")
        print(MyList)
    elif Question == 'S':
        print("Jou Winkel-Mandje is zojuist gestopt. ")
        break
    else:
        print("Invalid answer")
        Question = 0
        continue