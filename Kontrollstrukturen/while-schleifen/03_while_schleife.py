# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting while_schleife.py')

print("### Aufgabe 1 ###")
# Schreibe ein Programm, welches die Werte von 0 bis 5 ausgibt.
i = 0
while i < 6:
    print(i)
    i += 1

print("### Aufgabe 2 ###")
# Schreibe ein Programm, welches die Werte von 2 bis 7 ausgibt.
i = 2
while i < 8:
    print(i)
    i += 1

print("### Aufgabe 3 ###")
# Schreibe ein Programm, welches die Werte von 1 bis 19 in Zweierschritten ausgibt.
i = 1
while i < 20:
    print(i)
    i += 2

print("### Aufgabe 4 ###")
# Schreibe ein Programm, welches die Werte von 10 bis -10 in Zweierschritten rückwärts ausgibt.
i = 10
while i > -11:
    print(i)
    i -= 2

print("### Aufgabe 5 ###")
# Schreibe ein Programm, welches x mit y multipliziert, wobei x von 1 bis 5 läuft und y von 1 bis 3 läuft.
# Die Ausgabe könnte so aussehen:
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
x = 1
while x < 6:
    y = 1
    while y < 4:
        print(x * y, end=" ")
        y += 1
    print()
    x += 1

print("### Aufgabe 6 ###")
# Schreibe ein Programm, welches die Nutzerin nach einer Zahl fragt. Anschließend wird zurückgegeben,
# ob die Zahl durch die Zahl sieben teilbar ist oder nicht. Diese Abfrage wird solange wiederholt,
# bis die Nutzerin nichts eingibt (Der Rückgabewert entspricht also einem leeren String ("").
# Hinweis: Nutze die Funktion input().
while True:
    user_input = input("Bitte geben Sie eine Zahl ein: ")
    if user_input == "":
        break
    elif int(user_input) % 7 == 0:
        print("Die Zahl ist durch 7 teilbar!")
    else:
        print("Die Zahl ist nicht durch 7 teilbar!")
