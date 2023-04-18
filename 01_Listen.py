# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 01_Listen.py')

# Aufgabe 1:
# Erstelle eine Liste aus drei selbstgewählten Zahlen.
# Drucke die gesamte Liste komplett aus. Drucke anschließend die Länge der Liste aus.

liste = [1, 2, 3]
print("Liste: ", liste)
print("Länge der Liste (bzw. Anzahl der Objekte): ", len(liste))

# Aufgabe 2:
# Erstelle eine Liste aus drei selbstgewählten Zahlen.
# Drucke anschließend die einzelnen Werte der Liste nach einader aus, ohne eine Schleife zu benutzen.
liste = [1, 2, 3]
print("Liste: ", liste[0], liste[1], liste[2])

# Aufgabe 3:
# Erstelle eine Liste aus drei selbstgewählten Zahlen.
# Drucke anschließend die einzelnen Werte der Liste nach einader aus.
# Verwende nun eine for-Schleife, um auf jedes Element der Liste zuzugreifen.
# Die Liste selbst soll die Sequenz sein, auf die zugegriffen wird.
# Verwende also nicht die range()-Funktion.
liste = [1, 2, 3]
print(liste[0])
print(liste[1])
print(liste[2])

for i in liste:
    print("Element der Liste: ", i)

# Aufgabe 4:
# Erstelle eine Liste aus drei selbstgewählten Zahlen.
# Drucke anschließend die einzelnen Werte der Liste nach einader aus.
# Verwende eine for-Schleife und die range()- Funktion. Dazu musst du vorher die Länge der Liste bestimmen.
# Greife auf das aktuelle Element der Liste über den aktuellen Index zu.
liste = [1, 2, 3]
print(liste[0])
print(liste[1])
print(liste[2])

length = len(liste)

for i in range(length):
    print("Element der Liste: ", liste[i])

# Aufgabe 5:
# Erstelle eine Liste aus drei selbstgewählten Zahlen.
# Drucke anschließend die einzelnen Werte der Liste in umgekehrte Reihenfolge,
# also von hinten nach vorne, nach einader aus.
# Verwende wieder eine for-Schleife, um auf jedes Element der Liste zuzugreifen.
# Hinweis: die Funktion reversed() darf nicht verwendet werden.
liste = [1, 2, 3]
print(liste[2])
print(liste[1])
print(liste[0])

for i in liste:
    print("Element der Liste: ", i)

# Aufgabe 6:
# Erstelle eine Liste mit 5 Zahlen.
# Berechne anschließend in einer Schleife die Summe der in der Liste enthaltenen Zahlen.
# Dazu musst du vor dem Schleifendruchlauf einen Variable "Summe" erstellen, welche anfänglich den Wert 0 hat.
# (summe = 0). Anschließend fügst du der Summe in jedem Durchlauf das aktuelle Element der Liste hinzu.
# Gib am Ende das Ergebnis der Summenberechnung aus.
liste = [1, 2, 3, 4, 5]
summe = 0

for i in liste:
    summe = summe + i

print("Summe: ", summe)

# Aufgabe 7:
# Erstelle eine leere Liste. Füge anschließend in einer Schleife die Quadratzahlen von 1 bis 8 hinzu.
# Dazu soll in jedem Durchlauf jeweils nur ein Element hinzugefügt werden.
# Drucke anschließend die Liste komplett aus.
liste = []
for i in range(1, 9):
    liste.append(i + 1)

print("Liste: ", liste)