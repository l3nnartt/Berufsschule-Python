# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting 04_Palindrom.py')

print("### Aufgabe 1 ###")


# Für Strings ist eine Funktion: isPalindrom(char* str1); zu implementieren.
# Es soll zurückgegeben werden, ob ein String Palindrom ist.
# (Palindrom sind Wörter, die vorwärts und rückwärts gelesen gleich sind, z.B.: Otto, Anna, Lagerregal, Rentner)


def isPalindrom(inputString):
    checkString = inputString[::-1]
    if inputString == checkString:
        return True
    else:
        return False


string = input("Bitte geben Sie einen String ein: ").lower()
print("Ist der String ein Palindrom? ", isPalindrom(string))
