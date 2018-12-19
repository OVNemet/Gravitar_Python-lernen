summe = 0

for feld in range(64):
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("Feld {}. = {:>30,} Reiskoernen und damit insgesamt {:>30,} Reiskoerner".format(feld+1, reiskorn, summe))
print()

gewicht = 0.02 * summe / 1000 / 1000
print("Wenn ein Reskorn 0,02g wiegt, wiegen die gesamten")
print("Reiskoerner {:18,.0f} Tonnen.".format(gewicht))