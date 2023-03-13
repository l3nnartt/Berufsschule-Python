import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting howOftenContaind.py')

print("### Aufgabe 1 ###")


# Fur Strings ist eine Funktion: howOftenContaind(char* str, char c) zu implementieren.
# Es soll berechnet werden, wie oft das Zeichen c im String str enthalten ist.
def howOftenContaind(str, c):
    counter = 0
    for character in str:
        if character == c:
            counter += 1
    return counter


text = input("Bitte geben Sie einen String ein: ")
char = input("Bitte geben Sie ein zu suchendes Zeichen ein: ")
print("Die Anzahl der Vorkommen von 'l' im String 'Hallo Welt' ist: ", howOftenContaind(text, char))
