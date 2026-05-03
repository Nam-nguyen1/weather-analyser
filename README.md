# WeatherAnalyser – Wetterdaten-Auswertung

**Auftraggeber:** Bergbahnen Flumserberg AG, Flums  
**Lehrjahr:** 1. Lehrjahr Applikationsentwicklung  
**Sprache:** Python 3  
**Sozialform:** Solo  

---

## Inhaltsverzeichnis

1. [Projektbeschreibung](#1-projektbeschreibung)
2. [Teilaufgabe 1 – Analyse](#2-teilaufgabe-1--analyse)
3. [Teilaufgabe 2 – Design](#3-teilaufgabe-2--design)
4. [Teilaufgabe 3 – Planung](#4-teilaufgabe-3--planung)
5. [Lernjournal](#5-lernjournal)

---

## 1. Projektbeschreibung

Die Bergbahnen Flumserberg AG betreibt mehrere automatische Wettermessstationen auf bis zu 2 220 m ü. M. im Kanton St. Gallen. Jede Station zeichnet stündlich drei Messgrössen auf: Temperatur (°C), Windgeschwindigkeit (km/h) und Schneehöhe (cm). Die Daten werden als CSV-Dateien lokal gespeichert.

**Problem:** Das Technik-Team öffnet die Dateien manuell in Excel – bei mehreren Hundert Zeilen dauert das viel zu lange.

**Lösung:** Ein Python-Script `weather_analyser.py`, das eine CSV-Datei einliest, die Messwerte mit MergeSort sortiert und automatisch Minimum, Maximum und Durchschnitt berechnet. Alle Funktionen sind mit Unit-Tests (pytest) auf 100% Statement Coverage geprüft.

---

## 2. Teilaufgabe 1 – Analyse

### 2.1 Problemstellung

Frau Sandra Walser (Betriebsleiterin) wünscht sich ein Script, das:
- eine CSV-Datei mit Wettermesswerten einliest
- die Daten mit MergeSort sortiert
- Minimum, Maximum und Durchschnitt berechnet und anzeigt
- bei fehlerhaften Dateien eine verständliche Fehlermeldung ausgibt

### 2.2 Ein- und Ausgaben der Funktionen

| Funktion | Eingabe | Ausgabe | Fehlerfälle |
|---|---|---|---|
| `csv_einlesen()` | `dateipfad: str` | `list[dict]` | `FileNotFoundError`, `ValueError` |
| `merge_sort()` | `liste: list, schluessel: str` | `list` | – |
| `merge()` | `links: list, rechts: list, schluessel: str` | `list` | – |
| `minimum()` | `liste: list, schluessel: str` | `dict \| None` | `None` bei leerer Liste |
| `maximum()` | `liste: list, schluessel: str` | `dict \| None` | `None` bei leerer Liste |
| `durchschnitt()` | `liste: list, schluessel: str` | `float \| None` | `None` bei leerer Liste |
| `auswertung()` | `dateipfad: str` | `None` (Terminal-Ausgabe) | Fehler werden abgefangen |

### 2.3 Fehlerfälle

- **Datei nicht vorhanden:** `FileNotFoundError` wird geworfen
- **Datei leer (nur Kopfzeile):** leere Liste `[]` wird zurückgegeben
- **Fehlerhafter Wert in einer Zeile:** `ValueError`
- **Leere Liste bei Statistikfunktionen:** Rückgabe `None` (kein `ZeroDivisionError`)

### 2.4 Landau-Notation (Big-O)

Die Landau-Notation beschreibt das Wachstumsverhalten eines Algorithmus in Abhängigkeit von der Eingabegrösse `n`. Sie gibt an, wie viele Schritte ein Algorithmus im schlechtesten Fall benötigt.

| Algorithmus | Laufzeit | Beispiel n=1000 | Erklärung |
|---|---|---|---|
| Selectionsort (Kap. 2) | O(n²) | ~1'000'000 Schritte | Jedes Element mit jedem vergleichen |
| **MergeSort (dieses Projekt)** | **O(n log n)** | **~10'000 Schritte** | Teilen + Zusammenführen |
| Binäre Suche (Kap. 1) | O(log n) | ~10 Schritte | Halbierung bei jedem Schritt |

MergeSort ist deutlich effizienter als Selectionsort. Das Prinzip ist dasselbe wie bei der binären Suche (Kap. 1): durch Halbierung wächst die Arbeit viel langsamer als die Datenmenge.

### 2.5 User Stories

**User Story 1**
> Als Betriebsleiterin (Frau Walser) möchte ich die Temperaturdaten einer Woche automatisch auswerten lassen können, damit ich sofort sehe, wann es am kältesten und wärmsten war, ohne Excel zu öffnen.

Akzeptanzkriterien:
- Das Script liest eine CSV-Datei ein und gibt Min/Max/Ø der Temperatur aus
- Die Ausgabe enthält Datum, Wert und Einheit (z. B. `Min: -15.3 °C am 2024-01-20`)
- Bei fehlender oder leerer CSV-Datei erscheint eine verständliche Fehlermeldung

---

**User Story 2**
> Als Pistenwart möchte ich die Schneehöhen-Daten sortiert nach Wert sehen können, damit ich schnell erkenne, an welchem Tag die meiste Schneehöhe gemessen wurde.

Akzeptanzkriterien:
- `merge_sort()` sortiert die Liste korrekt nach einem wählbaren Schlüssel
- Das Ergebnis ist aufsteigend sortiert
- `merge_sort()` verändert die ursprüngliche Liste nicht

---

**User Story 3**
> Als Stationsleiter möchte ich den Durchschnitt der Windgeschwindigkeit kennen, damit ich Trends erkennen und Sicherheitsmassnahmen rechtzeitig planen kann.

Akzeptanzkriterien:
- `durchschnitt()` berechnet den Mittelwert aller Werte korrekt
- Das Ergebnis ist auf 2 Dezimalstellen gerundet
- Bei einer leeren Liste gibt die Funktion `None` zurück – kein `ZeroDivisionError`

---

**User Story 4**
> Als zukünftige Entwicklerin möchte ich den Code ohne Rückfragen verstehen können, damit das Script einfach wartbar und erweiterbar bleibt.

Akzeptanzkriterien:
- Jede Funktion hat einen Docstring mit Args, Returns und Raises
- Das Design-Dokument erklärt MergeSort mit PAP-Diagramm
- Alle Funktionen sind mit pytest-Tests abgedeckt (100% Statement Coverage)

---

**User Story 5**
> Als Betriebsleiter möchte ich alle drei Messgrössen in einem einzigen Lauf gleichzeitig auswerten können, damit ich nicht drei separate Scripts ausführen muss.

Akzeptanzkriterien:
- `auswertung()` gibt Min/Max/Ø für alle drei Messgrössen in einem Bericht aus
- Die sortierte Temperaturtabelle wird am Ende des Berichts angezeigt
- Das Script wird mit einem einzigen Befehl gestartet: `python weather_analyser.py`

---

## 3. Teilaufgabe 2 – Design

### 3.1 Was ist MergeSort?

MergeSort ist ein Sortieralgorithmus, der nach dem Teile-und-herrsche-Prinzip (Kapitel 4) funktioniert. Anstatt eine grosse Liste direkt zu sortieren, teilt er sie immer wieder in zwei Hälften auf, bis jede Teilliste nur noch ein Element enthält. Eine Liste mit einem Element ist automatisch sortiert – das ist der sogenannte **Basisfall** (Kapitel 3).

Danach werden die sortierten Teillisten schrittweise wieder zusammengeführt. Beim Zusammenführen (`merge`) werden die jeweils kleinsten Elemente beider Listen verglichen und in der richtigen Reihenfolge ins Ergebnis eingefügt.

MergeSort hat eine Laufzeit von O(n log n), weil die Liste bei jedem Schritt halbiert wird (log n Ebenen) und auf jeder Ebene alle n Elemente einmal verglichen werden.

Die drei Schritte:
1. **Divide (Teilen):** Liste rekursiv halbieren bis Basisfall
2. **Conquer (Lösen):** Basisfall – 1-Element-Liste ist bereits sortiert
3. **Combine (Zusammenführen):** `merge()` fügt sortierte Teillisten zusammen

### 3.2 PAP-Diagramm: merge_sort()

```
START
  |
  v
[Eingabe: liste, schluessel]
  |
  v
<len(liste) <= 1 ?> ──JA──> [RETURN liste]   ← Basisfall
  |
 NEIN
  |
  v
[mitte = len(liste) // 2]
  |
  v
[links  = merge_sort(liste[:mitte], schluessel)]  ← rekursiver Aufruf
  |
  v
[rechts = merge_sort(liste[mitte:], schluessel)]  ← rekursiver Aufruf
  |
  v
[RETURN merge(links, rechts, schluessel)]
  |
 END

── merge(links, rechts, schluessel) ──
Solange beide Listen nicht leer:
  links[i] <= rechts[j] ?  ja  → ergebnis.append(links[i]), i++
                           nein → ergebnis.append(rechts[j]), j++
Rest von links/rechts ans Ergebnis hängen.
RETURN ergebnis
```

### 3.3 PAP-Diagramm: auswertung()

```
START
  |
  v
[dateipfad übergeben]
  |
  v
[csv_einlesen(dateipfad)]
  |
  v
<Fehler ?> ──JA──> [Fehlermeldung ausgeben] ──> END
  |
 NEIN
  |
  v
<Daten leer ?> ──JA──> [Hinweis ausgeben] ──> END
  |
 NEIN
  |
  v
[Für jede Messgrösse (Temperatur, Wind, Schneehöhe):]
  ├─ minimum(daten, schluessel)
  ├─ maximum(daten, schluessel)
  └─ durchschnitt(daten, schluessel)
  |
  v
[Formatierten Bericht im Terminal ausgeben]
  |
  v
[merge_sort(daten, 'temperatur')] → sortierte Liste ausgeben
  |
 END
```

### 3.4 Funktionstabelle

| Funktion | Parameter | Rückgabetyp | Fehlerfälle | Beschreibung |
|---|---|---|---|---|
| `csv_einlesen()` | `dateipfad: str` | `list[dict]` | `FileNotFoundError`, `ValueError` | Liest CSV ein, gibt Liste von Dicts zurück |
| `merge_sort()` | `liste, schluessel` | `list` | – | Rekursives Sortieren |
| `merge()` | `links, rechts, schluessel` | `list` | – | Zwei Listen zusammenführen |
| `minimum()` | `liste, schluessel` | `dict \| None` | `None` bei leer | Datensatz mit kleinstem Wert |
| `maximum()` | `liste, schluessel` | `dict \| None` | `None` bei leer | Datensatz mit grösstem Wert |
| `durchschnitt()` | `liste, schluessel` | `float \| None` | `None` bei leer | Mittelwert, gerundet auf 2 Dez. |
| `auswertung()` | `dateipfad: str` | `None` | Fehler abgefangen | Hauptfunktion, gibt Bericht aus |

### 3.5 Dictionary-Format (csv_einlesen())

`csv_einlesen()` gibt eine Liste von Dictionaries zurück. Jedes Dictionary repräsentiert eine Messung:

```python
[
    {
        'datum':               '2024-01-15',  # str   – Messdatum
        'temperatur':          -8.2,          # float – in °C
        'windgeschwindigkeit':  34.0,         # float – in km/h
        'schneehoehe':         120.0          # float – in cm
    },
    {
        'datum':               '2024-01-16',
        'temperatur':          -3.1,
        'windgeschwindigkeit':  18.0,
        'schneehoehe':         118.0
    },
    # ...
]
```

---

## 4. Teilaufgabe 3 – Planung

### 4.1 Meilensteine

| Nr. | Meilenstein | Kriterium | Termin |
|---|---|---|---|
| M1 | CSV einlesen fertig | `csv_einlesen()` läuft, Daten korrekt geparst | Ende Woche 2 |
| M2 | Kern-Algorithmen fertig | `merge_sort()` + Statistikfunktionen korrekt, erste Tests grün | Ende Woche 3 |
| M3 | Abgabe bereit | 100% Coverage, Testprotokoll, Doku fertig, Video abgegeben | Ende Woche 4 |

### 4.2 Wochenplan

| Woche | Aufgaben | Ergebnis | Meilenstein |
|---|---|---|---|
| Woche 1 | Kein Zeit – ausgefallen | – | – |
| Woche 2 | `csv_einlesen()` nachholen · `merge_sort()` + `merge()` implementieren · Lernjournal W1+W2 | CSV + Sort fertig | M1 ✓ |
| Woche 3 | `minimum()` · `maximum()` · `durchschnitt()` · `auswertung()` · Docstrings · Tests T01–T12 | Programm läuft | M2 ✓ |
| Woche 4 | Tests T13–T18 · 100% Coverage · Testprotokoll · Dokumentation · Video · Abgabe | Alles fertig | M3 ✓ |

---

## 5. Lernjournal

### Woche 1

| Frage | Antwort |
|---|---|
| Was habe ich gemacht? | Kein Zeit diese Woche – konnte das Projekt kaum starten. Habe das Kundenbriefing kurz gelesen. |
| Was hat gut funktioniert? | Das Briefing war klar verständlich. |
| Was war schwierig? | Zeitmangel. Die Landau-Notation war anfangs abstrakt. |
| Was habe ich gelernt? | Grundlegendes Verständnis der Landau-Notation aus Kap. 1. |
| Selbsteinschätzung | Note 3 – weniger erreicht als geplant, Rückstand muss aufgeholt werden. |
| Ziel nächste Woche | `csv_einlesen()` fertigstellen + `merge_sort()` implementieren. |

### Woche 2

| Was habe ich gemacht? | Ich habe den Rückstand aus Woche 1 aufgeholt. Die Dokumentation für Teilaufgabe 1, 2 und 3 fertiggestellt und das GitHub Repository eingerichtet. Die README.md mit der ganzen Projektdokumentation wurde direkt ins Repo hochgeladen. |
| Was hat gut funktioniert? | Das Einrichten des Git Repositories hat gut geklappt. Die Struktur der Dokumentation war klar und ich konnte alles schnell zusammenstellen. |
| Was war schwierig? | Dieses Dokument hat mir viel zu lange gedauert. Es war schwerig um git zu verstehen aber ich habe es geschafft. |
| Was habe ich gelernt? | Ich habe gelernt wie man ein Git Repository erstellt, Dateien hinzufügt und auf GitHub hochlädt. Ausserdem weiss ich jetzt wie eine README.md aufgebaut ist und wie sie auf GitHub angezeigt wird. |
| Selbsteinschätzung | Note 4 – habe den Rückstand aufgeholt und das Repo sauber eingerichtet. |
| Ziel nächste Woche | Alle Funktionen implementieren und erste Tests schreiben. |
### Woche 3


### Woche 4


