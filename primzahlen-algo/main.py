# Algorythmus
# 1. Zahl 2 festlegen :-)
# Schleife: :-)
#  - Zahl +1 :-)
# - for schleife mit range 2 - Zahl
# - Dictionary mit for schleife durchgehen, lässt dich die zahl mit der Zahl im dictionary teilen, überprüfen ob ausgewählte Zahl
# im Dictionary 1 oder zahl ist
# JA: Weitermachen
# NEIN: For Schleife abbrechen, zahl in Konsole schreiben und schleife von vorne anfangen

from test import isPrime
zahl = 2
while True:
    zahl += 1
    if isPrime(zahl) == True:
        print(str(zahl))


