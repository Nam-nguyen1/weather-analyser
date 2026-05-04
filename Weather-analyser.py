
import csv
 
 
def csv_einlesen(dateipfad):
 
    ergebnis = []
    with open(dateipfad, newline="", encoding="utf-8") as datei:
        reader = csv.DictReader(datei, delimiter=";")
        for zeile in reader:
            try:
                ergebnis.append({
                    "datum": zeile["datum"].strip(),
                    "temperatur": float(zeile["temperatur"]),
                    "windgeschwindigkeit": float(zeile["windgeschwindigkeit"]),
                    "schneehoehe": float(zeile["schneehoehe"]),
                })
            except (ValueError, KeyError) as fehler:
                raise ValueError(f"Ungültige Daten: {dict(zeile)}") from fehler
    return ergebnis
 
 
def merge(links, rechts, schluessel):

    ergebnis = []
    i = j = 0
    while i < len(links) and j < len(rechts):
        if links[i][schluessel] <= rechts[j][schluessel]:
            ergebnis.append(links[i])
            i += 1
        else:
            ergebnis.append(rechts[j])
            j += 1
    ergebnis.extend(links[i:])
    ergebnis.extend(rechts[j:])
    return ergebnis
 
 
def merge_sort(liste, schluessel):

    if len(liste) <= 1:
        return list(liste)
    mitte = len(liste) // 2
    links = merge_sort(liste[:mitte], schluessel)
    rechts = merge_sort(liste[mitte:], schluessel)
    return merge(links, rechts, schluessel)
 
 
def minimum(liste, schluessel):

    if not liste:
        return None
    klein = liste[0]
    for eintrag in liste[1:]:
        if eintrag[schluessel] < klein[schluessel]:
            klein = eintrag
    return klein
 
 
def maximum(liste, schluessel):

    if not liste:
        return None
    gross = liste[0]
    for eintrag in liste[1:]:
        if eintrag[schluessel] > gross[schluessel]:
            gross = eintrag
    return gross
 
 
def durchschnitt(liste, schluessel):

    if not liste:
        return None
    summe = 0.0
    for eintrag in liste:
        summe += eintrag[schluessel]
    return round(summe / len(liste), 2)
 
 
def auswertung(dateipfad):

    print("=" * 50)
    print("  Bergbahnen Flumserberg AG – WeatherAnalyser")
    print("  Datei:", dateipfad)
    print("=" * 50)
 
    try:
        daten = csv_einlesen(dateipfad)
    except FileNotFoundError:
        print(f"FEHLER: Datei '{dateipfad}' nicht gefunden.")
        return
    except ValueError as fehler:
        print(f"FEHLER: {fehler}")
        return
 
    if not daten:
        print("Keine Daten in der Datei.")
        return
 
    print(f"  Einträge: {len(daten)}\n")
 
    for schluessel, name, einheit in [
        ("temperatur", "Temperatur", "°C"),
        ("windgeschwindigkeit", "Wind", "km/h"),
        ("schneehoehe", "Schneehöhe", "cm"),
    ]:
        mi = minimum(daten, schluessel)
        ma = maximum(daten, schluessel)
        avg = durchschnitt(daten, schluessel)
        print(f"  {name}:")
        print(f"    Min: {mi[schluessel]} {einheit} ({mi['datum']})")
        print(f"    Max: {ma[schluessel]} {einheit} ({ma['datum']})")
        print(f"    Ø  : {avg} {einheit}\n")
 
    print("=" * 50)
 
 
if __name__ == "__main__":
    datei = input("CSV-Datei eingeben: ")
    auswertung(datei)
 