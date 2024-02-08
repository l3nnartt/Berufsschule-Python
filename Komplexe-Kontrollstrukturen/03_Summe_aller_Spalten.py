# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 03_Summe_aller_Spalten.py')

# Aufgabe:
# Schreibe ein Programm, welches eine Liste mit Zahlen durchläuft und eine neue
# Liste zurückgibt, die die Summen der Spalten der Eingabeliste enthält.
# Beispiel-Liste:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Ausgabe in der Konsole:
# [12, 15, 18]

liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spaltensummen = []

listLength = len(liste)

for element in range(listLength):
    print(element)

print(listLength)
length0 = len(liste[0])
summe = 0

#for x in range(length0):
#    for y in range(length):
#        summe = summe + liste[y][x]
#    spaltensummen.append(summe)

ergebnis = spaltensummen
print(ergebnis)
