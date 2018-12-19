import matplotlib.pyplot as plt

feldListe = []
summe = 0

for feld in range(64):
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}. = {reiskorn:>30,} Reiskoernen und damit insgesamt {summe:>30,} Reiskoerner")
print()

gewicht = 0.02 * summe / 1000 / 1000

print("Wenn ein Reskorn 0,02g wiegt, wiegen die gesamten")
print(f"Reiskoerner {gewicht:18,.0f} Tonnen.")

plt.plot(feldListe)
plt.show()