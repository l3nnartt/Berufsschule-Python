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
