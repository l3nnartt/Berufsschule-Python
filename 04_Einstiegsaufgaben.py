# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Aufgabe 0:
# Schreibe ein Programm, welches in der Konsole die Worte "Hello World" ausgibt.

print("Hello World")


# Aufgabe 1:
# Schreibe ein Programm mit dem Namen Grundrechenarten, das zwei Zahlen zwischen 0 und 100 addiert,
# subtrahiert, multipliziert und dividiert und die Ergebnisse in der Konsole ausgibt.
# Wähle sowohl für die zwei Zahlen als auch die Ergebnisse der vier Grundrechenarten geeignete Variablen.

def Grundrechenarten(a, b):  # functions should be lowercase x.x

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
