# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  print("Start!")

# Aufgabe 1: Eingabeüberprüfung
# Frage den Nutzer nach der Eingabe einer Ganzzahl.
# Überprüfe anschließend, ob die Eingabe nur aus Ziffern besteht.
# Wenn die Eingabe nicht nur aus Ziffern besteht, gib den Satz aus:
# „Die Eingabe war keine Zahl“
# Ansonsten wandle die Eingabe anschließend in einen Integer um.
eingabe = input("Nennen Sie Bitte einen Monat als Zahl zwischen 1 und 12: ")
if not eingabe.isdecimal():  # 0 - 9
    print("Die Eingabe war keine Zahl!")
else:
    zahl = int(eingabe)
