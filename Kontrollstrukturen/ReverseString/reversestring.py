# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting reversestring.py')

print("### Aufgabe 1 ###")


# https://www.w3schools.com/python/python_howto_reverse_string.asp
# Schreiben Sie das Pythonprogramm reverse_string.py,
# welches einen String von der Konsole einliest und ihn umgekehrt wieder ausgibt.

def reverseString(inputString):
    return inputString[::-1]


string = input("Bitte geben Sie einen String ein: ").lower()
print("Der umgekehrte String ist: ", reverseString(string))
