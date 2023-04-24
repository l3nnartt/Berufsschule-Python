# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 02_Zweidimensionale_Listen.py')

# Arbeitsauftrag
# Schreibe ein Programm, welches eine zweidimensionale Liste von Wörtern durchläuft und die Anzahl der Buchstaben zählt,
# die in den Wörtern enthalten sind.
#
# Folgende Liste ist gegeben:
# [['Hund', 'Katze', 'Maus'], ['Apfel', 'Banane', 'Erdbeere'], ['Gurke', 'Tomate', 'Kartoffel']]
#
# Das Ergebnis wäre wie folgt, wenn nach einem “a” bzw. “A” gesucht wird:
# “Der Buchstabe A kommt 7 mal in der vorgegeben Liste vor”
#
liste = [['Hund', 'Katze', 'Maus'], ['Apfel', 'Banane', 'Erdbeere'], ['Gurke', 'Tomate', 'Kartoffel']]
counter = 0

for listElement in liste:
    for word in listElement:
        for char in word:
            if char.upper() == "A":
                counter += 1

print("Der Buchstabe A kommt " + str(counter) + " mal in der vorgegeben Liste vor")
