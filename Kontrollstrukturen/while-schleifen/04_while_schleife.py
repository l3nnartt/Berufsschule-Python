import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting while_schleife.py')

print("### Aufgabe 1 ###")
# Entwickle ein Programm, das den Nutzer eine Zahl raten lässt. Dazu wird vorher eine zu ratende Zahl definiert,
# welche der Nutzer nicht kennt. Für die eingegebene Zahl und die zu ratende Zahl gilt, dass sie größer als 50 sein
# sollen. Wiederhole die Eingabeaufforderung so lange, bis ein passender Wert eingegeben wurde. Dem Benutzer soll nach
# jeder Eingabe mitgeteilt werden, ob die eingegebene Zahl zu klein ist, also kleiner gleich 50 und/oder ob die
# eingegebene Zahl größer oder kleiner als die zu ratende Zahl ist. Wird die Zahl erraten, so endet das Programm mit
# einem Glückwunsch.

# Zufallszahl generieren
random_number = random.randint(51, 100)

# Nutzereingabe
user_input = int(input("Bitte geben Sie eine Zahl > 50 ein: "))

# Eingabeaufforderung
while user_input < 51:
    print("Die eingegebene Zahl ist < 50!")
    user_input = int(input("Bitte gebe eine Zahl ein: "))

# Vergleich
while user_input != random_number:
    if user_input < random_number:
        print("Die eingegebene Zahl ist kleiner als die zu gesuchte Zahl!")
        user_input = int(input("Bitte gebe eine Zahl ein: "))
    elif user_input > random_number:
        print("Die eingegebene Zahl ist größer als die zu gesuchte Zahl!")
        user_input = int(input("Bitte gebe eine Zahl ein: "))

# Glückwunsch
print("Glückwunsch! Sie haben die Zahl erraten!")

print("### Aufgabe 2 ###")
# Schreibe ein Programm welches die Summe der Zahlen von 1 bis 100 berechnet.
summe = 1
multiplier = 1
while multiplier < 101:
    multiplier += 1
    summe += multiplier
print("Die Summe der Zahlen von 1 bis 100 ist: ", summe)

print("### Aufgabe 3 ###")
# Schreibe ein Programm welches die Rückzahlung eines Kredites berechnet. Folgende Eingaben werden vom Benutzer
# vorgenommen:
#
# die Höhe des Kredites
# der Zinssatz in Prozent
# der jährlicher Rückzahlungsbetrag
#
# Die Ausgabe des Programms soll nach folgender Art erfolgen (Werte der Variablen können frei gewählt werden):
#
#
# Kreditsumme in Euro: 1000
#     Zinssatz    in    Prozent:    6
#     Jährlicher    Rückzahlungsbetrag    in    Euro:    200
#     2004    Zinsen:    60    Euro    Tilgung:    140    Euro     Rest:    860    Euro
#     2005    Zinsen:    51    Euro    Tilgung:    149    Euro     Rest:    711    Euro
#     2006    Zinsen:    42    Euro    Tilgung:    158    Euro     Rest:    553    Euro
#     2007    Zinsen:    33    Euro    Tilgung:    167    Euro     Rest:    386    Euro
#     2008    Zinsen:    23    Euro    Tilgung:    177    Euro     Rest:    209    Euro
#     2009    Zinsen:    12    Euro    Tilgung:    188    Euro     Rest:    21     Euro
#     Restforderung:     21    Euro
# Kreditsumme
credit = float(input("Bitte geben Sie die Kreditsumme in Euro ein: "))

# Zinssatz
interest = float(input("Bitte geben Sie den Zinssatz in Prozent ein: "))

# Rückzahlungsbetrag
repayment = float(input("Bitte geben Sie den Rückzahlungsbetrag in Euro ein: "))

# Ausgabe
year = 2004
while credit > 0:
    interest = credit * (interest / 100)
    credit -= repayment
    print(year, "Zinsen: ", interest, "Euro", "Tilgung: ", repayment, "Euro", "Rest: ", credit, "Euro")
    year += 1

print("Restbetrag: ", credit, "Euro")