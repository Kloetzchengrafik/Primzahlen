# Funktion erstellen
def isPrime(zahl):
    # for Schleife erstellen, von 2 bis zur angegebenen Zahl
    for i in range(2, zahl):
        # Rest errechnen
        hallo = zahl % i
        # Überprüfen: Rest vorhanden?
        if hallo == 0:
            # JA: Abbrechen; Teiler gefunden; Keine Primzahl
            return False
    # Kein Teiler gefunden: Primzahl
    return True
