# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 03_Summe_aller_Spalten.py')

# Aufgabe:
# Schreibe ein Programm, welches eine Liste mit Zahlen durchläuft und eine neue Liste zurückgibt,
# die die Summen der Spalten der Eingabeliste enthält.
# Beispiel-Liste:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Ausgabe in der Konsole:
# [12, 15, 18]

liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

summe = [0, 0, 0]
einzelsumme = 0

liste0 = liste[0]
liste1 = liste[1]
liste2 = liste[2]

for i in liste0:
    summe = summe + i

summe[0] = einzelsumme
