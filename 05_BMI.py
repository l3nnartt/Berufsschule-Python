# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 05_BMI.py')


# Aufgabe 1:
# Erstellen Sie ein Python Programm (bmi.py), das den Body-Mass-Index (BMI) berechnet.
# Eine Auswertung(Normalgewicht, Übergewicht, etc.) wird nicht durchgeführt.
# Berechnung → https://de.wikipedia.org/wiki/Body-Mass-Index
# Hinweis: Es dürfen keine Verzweigungen(if...else) verwendet werden.

def bmi(height, weight):
    result = weight / (height * height)
    print("BMI: ", result)


bmi(1.88, 64)
