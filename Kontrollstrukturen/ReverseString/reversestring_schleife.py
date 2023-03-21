# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting reversestring_schleife.py')

print("### Aufgabe 1 ###")


# https://www.w3schools.com/python/python_howto_reverse_string.asp
# Schreiben Sie das Pythonprogramm reverse_string.py,
# welches einen String von der Konsole einliest und ihn umgekehrt wieder ausgibt.

string = "Hallo Welt!"
reversedString = ""
reversedString2 = ""

# Option 1
for x in range(len(string), -1, -1):
    reversedString += string[x]
    print(reversedString)
    # !tleW ollaH

# Option 2
for c in string:
    reversedString2 = c + reversedString2
    print(reversedString2)
    # !tleW ollaH
