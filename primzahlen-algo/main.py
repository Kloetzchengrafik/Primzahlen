# Überprüfung importieren
from test import isPrime
# Anfangszahl festlegen
zahl = 2
#Schleife anfangen
while True:
    # Zahl bei jedem durchlauf um 1 erhöhen
    zahl += 1
    # Überprüfen ob Primzahl
    if isPrime(zahl) == True:
        # Wenn ja: Ausgeben
        print(str(zahl))
