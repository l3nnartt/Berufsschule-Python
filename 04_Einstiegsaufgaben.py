# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 04_Einstiegsaufgaben.py')

# Aufgabe 0:
# Schreibe ein Programm, welches in der Konsole die Worte "Hello World" ausgibt.

print("Hello World")


# Aufgabe 1:
# Schreibe ein Programm mit dem Namen Grundrechenarten, das zwei Zahlen zwischen 0 und 100 addiert,
# subtrahiert, multipliziert und dividiert und die Ergebnisse in der Konsole ausgibt.
# Wähle sowohl für die zwei Zahlen als auch die Ergebnisse der vier Grundrechenarten geeignete Variablen.

def Grundrechenarten(a, b):
    # first calculate the results
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    # then print the results
    print("Addition: ", add)
    print("Subtraction: ", sub)
    print("Multiplication: ", mul)
    print("Division: ", div)


# Aufgabe 2:
# Schreibe ein Programm mit dem Namen Dreieck, das aus der Länge einer Grundseite und der auf dieser Seite
# stehenden Höhe den Flächeninhalt bestimmt. Deklariere und initialisiere jeweils eine Variable für alle drei Werte
# und gib sie anschließend schön formatiert aus, d.h. mit Antwortsatz.

def Dreieck(length, height):
    area = height * length / 2
    print("The area of the triangle is: ", area)
    print("The height of the triangle is: ", height)
    print("The length of the triangle is: ", length)


# Aufgabe 3:
# Schreibe ein Programm mit dem Namen Tausch, das den Inhalt von zwei Variablen miteinander vertauscht.
# Eine Variable a wird mit dem Wert 5 initialisiert und eine Variable b mit dem Wert 3.
# Vertausch anschließend die Werte beider Variablen und gib die Werte aus.
# Dabei muss bei a der Wert 3 und bei b der Wert 5 ausgegeben werden.

def Tausch(x, y):
    print("changing values of x and y")
    print("Before:\n a: ", x, " b: ", y)
    x, y = y, x
    print("After:\n a: ", x, " b: ", y)


a = 5
b = 3

Tausch(a, b)


# Aufgabe 4:
# Schreibe ein Programm mit dem Namen Niederschlag, das die durchschnittliche Niederschlagsmenge für die
# Monate April, Mai und Juni berechnet. Deklariere und initialisiere jeweils eine Variable für jeden Monat. Berechne
# anschließend die durchschnittliche Niederschlagsmenge sowohl in einem Rechenschritt(mit einer Variable z.B.
# average) als auch in zwei Rechenschritten und gib die Ergebnisse in folgender Form aus:
#
# Niederschlag im April : 12
# Niederschlag im Mai : 14
# Niederschlag im Juni : 8
# Durchschnitt 1 Schritt : …
# Durchschnitt 2 Schritte: …

def Niederschlag():
    april = 12
    may = 14
    june = 8

    # Average in 1 Step
    average = (april + may + june) / 3

    # Average in 2+ Steps
    months = [april, may, june]
    count = len(months)
    i = 0
    for month in months:
        i += month
    average2 = i / count

    print("Niederschlag im April: ", april)
    print("Niederschlag im Mai: ", may)
    print("Niederschlag im Juni: ", june)
    print("Durchschnitt 1 Schritt: ", average)
    print("Durchschnitt 2 Schritte: ", average2)
