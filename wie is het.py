antwoord = input("is de kaas geel? Y/N").upper()

if antwoord == "Y":
    input("Zitten er gaten in?")
    if antwoord == "Y":
        input("Is de kaas belachelijk duur?")
        if antwoord == "Y":
            print("Emmenthaler")
        if antwoord == "N":
            print("Leerdammer")
    if antwoord == "N":
        input("Is de kaas hard als steen?")
        if antwoord == "Y":
            print("Pamnigiano Reggiano")
        if antwoord == "N":
            print("Goudse kaas")
if antwoord == "N":
    input("Heeft de kaas blauwe schimmels?")
    if antwoord == "Y":
        input("Heeft de kaas een korst?")
        if antwoord == "Y":
            print("Bleu de Rochbaron")
        if antwoord == "N":
            print("Foumne d'Ambert")
    if antwoord == "N":
        input("Heeft de kaas een korst?")
        if antwoord == "Y":
            print("Camembert")
        if antwoord == "N":
            print("Mozzerella")
