# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  print('Starting Einführungsaufgaben.py')


# Aufgabe 1:
# Betrachten Sie das folgende Punktesystem zur Notenvergabe:
#
# Punkte	Note
# 36-40	1
# 31-35	2
# 26-30	3
# 21-25	4
# 10 – 20	5
# < 10	6
#
# Implementieren Sie eine Funktion getNote(), die als Wert die Note der
# übergebenen Punkte zurückliefert. Liefern Sie den Wert -1 zurück, falls der
# Parameter punkte keine gültige Punktezahl darstellt.

def getNote(punkte):
  if 36 <= punkte <= 40:
    return 1
  elif 31 <= punkte <= 35:
    return 2
  elif 26 <= punkte <= 30:
    return 3
  elif 21 <= punkte <= 25:
    return 4
  elif 10 <= punkte <= 20:
    return 5
  elif punkte < 10:
    return 6
  else:
    return -1


# Example:
print(getNote(36))


# Aufgabe 2:
# Implementieren Sie eine Funktion getGreater() die zwei Parameter erhält
# und die größere Zahl zurückliefert.

def getGreater(a, b):
  if a > b:
    return a
  else:
    return b


# Example:
getGreater(1, 2)


# Aufgabe 3:
# Implementieren Sie die Funktion “mail_adressen_generator()”,
# welche eine Mail-Adresse basierend auf einem übergebenem Vornamen
# und Nachnamen generiert und zurückgibt.
#
# Die Mail-Adresse ist nach folgendem Muster aufgebaut:
# <erster_buchstabe_vorname>.<nachname>@schule.bremen.de
# Vorname: Thomas
# Nachname: Mann
#
# Mail: T.Mann@schule.bremen.de
#
# Tipp: Ein String, oder Zeichenkette,
# kann man als eine Sequenz von einzelnen Zeichen sehen.
# Es verhält sich ähnlich wie eine Liste.

def mail_adressen_generator(vorname, nachname):
  suffix = "@schule.bremen.de"
  return vorname[0] + "." + nachname + suffix


# Example:
print(mail_adressen_generator("Thomas", "Mann"))
