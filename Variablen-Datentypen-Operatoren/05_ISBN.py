# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 05_ISBN.py')


# Aufgabe 2:
# Die ISBN besteht aus 10 Ziffern.
# z1 z2 z3 z4 z5 z6 z7 z8 z9 z10
#
# Die letzte Ziffer z10 ist eine Prüfziffer. Sie berechnet sich wie folgt:
# Zuerst wird eine Art Quersumme nach folgender Formel gebildet:
# s = 1*z1 + 2*z2 + 3*z3 + 4*z4 + 5*z5 + 6*z6 + 7*z7 + 8*z8 + 9*z9
#
# Die Prüfziffer z10 ist der Rest der ganzzahligen Division von s durch 11, also s % 11.
# Beispiel: Für die ISBN 3826604237 lautet die Prüfziffer 7
# Rechnung: 1*3+2*8+3*2+4*6+5*6+6*0+7*4+8*2+9*3 = 150
# Der Rest der Division von 150 durch 11 ist 7. (Die Ganzzahldivision von 150 durch 11 hat das Ergebnis 13 hat.
# 11 mal 13 ergibt 143. Es bleiben als 7 bis zur 150 über. Also ergibt 150 % 11 = 7.)
#
# Schreiben Sie ein Programm (isbn.py), das die Prüfziffer einer ISBN berechnet. Eingegeben wird eine
# neunstellige natürliche Zahl. Ausgegeben wird die Prüfziffer als Zahl zwischen 0 und 10.

def isbn(number):
    number = tuple(number)
    # first calculate the results
    result = 1 * int(number[0]) + 2 * int(number[1]) + 3 * int(number[2]) + 4 * int(number[3]) + 5 * int(number[4]) \
             + 6 * int(number[5]) + 7 * int(number[6]) + 8 * int(number[7]) + 9 * int(number[8])
    # then print the results
    print("The ISBN is: ", number)
    print("The result of the calculation is: ", result)
    print("The check digit is: ", result % 11)


digit = input("ISBN: ")
isbn(digit)
