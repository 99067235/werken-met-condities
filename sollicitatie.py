antwoord = int(input("Hoelang heeft u praktijkervaring met dieren-dressuur?"))
geslaagd = False
if antwoord >= 4:
    antwoord = input("Bent u in het bezit van een diploma MBO 4 ondernemen? Y/N").upper()
    if antwoord =="Y":
        antwoord = input("Bent u in bezit van een geldig vrachtwagenrijbewijs? Y/N").upper()
        if antwoord =="Y":
            antwoord = input("Bent u in bezit van een hoge hoed? Y/N").upper()
            if antwoord =="Y":
                antwoord = input("Bent u man of vrouw? M/V").upper()
                if antwoord =="M":
                    antwoord = input("Heeft u een snor? Y/N").upper()
                    if antwoord =="Y":
                        antwoord = int(input("Hoe breed bent u met snor?"))
                        if antwoord >= 10:
                            antwoord = int(input("Hoelang bent u in cm?"))
                            if antwoord >= 150:
                                antwoord = int(input("Hoeveel weegt u in kg?"))
                                if antwoord >= 90:
                                    antwoord = float(input("Welke schoenmaat heeft u?"))
                                    if antwoord >= 40:
                                        antwoord = int(input("Hoeveel huisdieren heeft u?"))
                                        if antwoord <= 4:
                                            antwoord = (input("Welke kleur vind u mooier: blauw of oranje?"))
                                            if antwoord == "blauw":
                                                geslaagd = True
                if antwoord =="V":
                    antwoord = input("heeft u rood krulhaar? Y/N").upper()
                    if antwoord =="Y":
                        antwoord = int(input("Hoelang is uw rode krulhaar in cm?"))
                        if antwoord >= 20:
                            antwoord = int(input("Hoelang bent u in cm?"))
                            if antwoord >= 150:
                                antwoord = int(input("Hoeveel weegt u in kg?"))
                                if antwoord >= 90:
                                    antwoord = float(input("Welke schoenmaat heeft u?"))
                                    if antwoord >= 40:
                                        antwoord = int(input("Hoeveel huisdieren heeft u?"))
                                        if antwoord <= 4:
                                            antwoord = (input("Welke kleur vind u mooier: blauw of oranje?"))
                                            if antwoord == "blauw":
                                                geslaagd = True
if geslaagd == True:
    print("Gefeliciteerd! U hebt het certificaat: Overleven met gevaarlijk personeel!")
else:
    print("Sorry, maar u bent niet geschikt voor het beroep ruimtevuilnisman")