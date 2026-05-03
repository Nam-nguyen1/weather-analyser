# WeatherAnalyser – Wetterdaten-Auswertung
 
**Auftraggeber:** Bergbahnen Flumserberg AG, Flums
 
---
 
## Inhaltsverzeichnis
 
1. [Projektbeschreibung](#1-projektbeschreibung)
2. [Analyse](#2-analyse)
3. [Design](#3-design)
4. [Planung](#4-planung)
5. [Lernjournal](#5-lernjournal)
---
 
## 1. Projektbeschreibung
 
Die Bergbahnen Flumserberg AG misst jede Stunde Temperatur, Wind und Schneehöhe auf ihren Bergstationen. Die Daten werden als CSV-Datei gespeichert.
 
Das Team schaut die Daten manuell in Excel an. Bei vielen Zeilen dauert das zu lange.
 
Das Script liest die CSV-Datei ein, sortiert die Daten mit MergeSort und zeigt den kleinsten, grössten und durchschnittlichen Wert. Alle Funktionen werden mit Tests geprüft.
 
```bash
python weather_analyser.py
pytest test_weather_analyser.py --cov=weather_analyser --cov-report=term-missing
```
 
---
 
## 2. Analyse
 
### Was will der Kunde?
 
Frau Walser möchte ein Script das die CSV-Datei automatisch auswertet. Sie will Min, Max und Durchschnitt für Temperatur, Wind und Schneehöhe sehen, ohne Excel zu öffnen.
 
### CSV-Datei
 
```
datum;temperatur;windgeschwindigkeit;schneehoehe
2024-01-15;-8.2;34;120
2024-01-16;-3.1;18;118
```
 
### Funktionen
 
| Funktion | Eingabe | Ausgabe | Fehler |
|---|---|---|---|
| `csv_einlesen()` | Pfad zur Datei | Liste mit Messungen | Datei fehlt, falscher Wert |
| `merge_sort()` | Liste + Spaltenname | Sortierte Liste | – |
| `merge()` | Zwei Listen | Eine zusammengeführte Liste | – |
| `minimum()` | Liste + Spaltenname | Kleinste Messung | `None` wenn leer |
| `maximum()` | Liste + Spaltenname | Grösste Messung | `None` wenn leer |
| `durchschnitt()` | Liste + Spaltenname | Mittelwert | `None` wenn leer |
| `auswertung()` | Pfad zur Datei | Bericht im Terminal | Fehler abgefangen |
 
### Fehlerfälle
 
| Problem | Was passiert |
|---|---|
| Datei existiert nicht | Fehlermeldung |
| Datei ist leer | Leere Liste |
| Wert ist keine Zahl | Fehlermeldung |
| Liste ist leer | `None`, kein Absturz |
 
### Wie schnell ist MergeSort?
 
Big-O zeigt wie viele Schritte ein Algorithmus braucht wenn die Liste grösser wird.
 
| Algorithmus | Geschwindigkeit | Bei 1000 Einträgen |
|---|---|---|
| Selectionsort | O(n²) | ~1'000'000 Schritte |
| **MergeSort** | **O(n log n)** | **~10'000 Schritte** |
| Binäre Suche | O(log n) | ~10 Schritte |
 
MergeSort ist viel schneller weil er die Liste immer halbiert statt alles mit allem zu vergleichen.
 
### User Stories
 
**User Story 1**
> Als Betriebsleiterin möchte ich die Temperaturen automatisch auswerten lassen, damit ich nicht mehr Excel öffnen muss.
 
| Kriterium | OK? |
|---|---|
| Script zeigt Min, Max und Durchschnitt der Temperatur | |
| Ausgabe zeigt Datum, Wert und Einheit | |
| Bei fehlender Datei kommt eine Fehlermeldung |  |
 
**User Story 2**
> Als Pistenwart möchte ich die Schneehöhen sortiert sehen, damit ich weiss an welchem Tag am meisten Schnee lag.
 
| Kriterium | OK? |
|---|---|
| `merge_sort()` sortiert die Liste richtig |  |
| Die Liste ist von klein nach gross sortiert |  |
| Die Originalliste bleibt unverändert |  |
 
**User Story 3**
> Als Stationsleiter möchte ich den Durchschnitt der Windgeschwindigkeit sehen, damit ich gefährliche Wetterlagen früh erkenne.
 
| Kriterium | OK? |
|---|---|
| `durchschnitt()` rechnet den Mittelwert korrekt |  |
| Ergebnis auf 2 Stellen nach dem Komma gerundet |  |
| Bei leerer Liste kommt `None` zurück | |
 
**User Story 4**
> Als nächster Entwickler möchte ich den Code schnell verstehen, damit ich ihn einfach anpassen kann.
 
| Kriterium | OK? |
|---|---|
| Jede Funktion hat eine Erklärung (Docstring) |  |
| Es gibt ein Ablaufdiagramm für MergeSort |  |
| Alle Funktionen haben Tests mit 100% Abdeckung |  |
 
**User Story 5**
> Als Betriebsleiter möchte ich alle drei Messgrössen auf einmal sehen, damit ich nicht mehrere Scripts starten muss.
 
| Kriterium | OK? |
|---|---|
| `auswertung()` zeigt alle drei Messgrössen |  |
| Am Ende kommt eine sortierte Temperaturliste |  |
| Alles startet mit einem Befehl |  |
 
---
 
## 3. Design
 
### Was ist MergeSort?
 
MergeSort teilt eine Liste immer wieder in zwei Hälften auf, bis jede Teilliste nur noch ein Element hat. Ein einzelnes Element ist schon sortiert – das ist der Basisfall (Kapitel 3).
 
Dann werden die kleinen Listen wieder zusammengesetzt. Es wird immer das kleinere Element zuerst genommen bis eine fertig sortierte Liste entsteht. Das nennt man Teile-und-herrsche (Kapitel 4).
 
| Schritt | Was passiert |
|---|---|
| 1. Teilen | Liste halbieren bis nur 1 Element übrig |
| 2. Lösen | 1 Element = schon sortiert (Basisfall) |
| 3. Zusammensetzen | Kleine Listen sortiert zusammensetzen |
 
### Ablaufdiagramm: merge_sort()
 
```
START
  |
  v
<Liste hat 0 oder 1 Element?> ──JA──> [Liste zurückgeben]  <- Basisfall
  |
 NEIN
  |
  v
[Liste in der Mitte teilen]
  |
  v
[Linke Hälfte sortieren]   <- merge_sort() nochmal aufrufen
  |
  v
[Rechte Hälfte sortieren]  <- merge_sort() nochmal aufrufen
  |
  v
[Beide Hälften zusammensetzen mit merge()]
  |
 END
 
merge():
  Immer das kleinere Element aus links oder rechts nehmen.
  Wenn eine Seite leer ist, Rest der anderen anhängen.
  Fertige Liste zurückgeben.
```
 
### Ablaufdiagramm: auswertung()
 
```
START
  |
  v
[csv_einlesen() aufrufen]
  |
  v
<Fehler?> ──JA──> [Fehlermeldung anzeigen] ──> END
  |
 NEIN
  |
  v
<Keine Daten?> ──JA──> [Hinweis anzeigen] ──> END
  |
 NEIN
  |
  v
[Min, Max, Durchschnitt für Temperatur, Wind, Schneehöhe berechnen]
  |
  v
[Bericht anzeigen und sortierte Temperaturliste]
  |
 END
```
 
### Alle Funktionen
 
| Funktion | Was sie macht | Gibt zurück |
|---|---|---|
| `csv_einlesen()` | Liest die CSV-Datei | Liste mit Messungen |
| `merge_sort()` | Sortiert die Liste | Neue sortierte Liste |
| `merge()` | Setzt zwei Listen zusammen | Eine Liste |
| `minimum()` | Kleinster Wert | Messung |
| `maximum()` | Grösster Wert | Messung |
| `durchschnitt()` | Mittelwert | Zahl oder `None` |
| `auswertung()` | Führt alles aus | Nichts (Terminal) |
 
### So sieht eine Messung im Script aus
 
```python
{
    'datum':               '2024-01-15',
    'temperatur':          -8.2,
    'windgeschwindigkeit':  34.0,
    'schneehoehe':         120.0
}
```
 
---
 
## 4. Planung
 
### Meilensteine
 
| Nr. | Ziel | Wann |
|---|---|---|
| M1 | `csv_einlesen()` funktioniert | Ende Woche 2 |
| M2 | Alle Funktionen fertig, erste Tests laufen | Ende Woche 3 |
| M3 | 100% Tests, Doku fertig, Video abgegeben | Ende Woche 4 |
 
### Wochenplan
 
| Woche | Was ich mache | Meilenstein |
|---|---|---|
| Woche 1 | Keine Zeit – ausgefallen | – |
| Woche 2 | `csv_einlesen()` nachholen · `merge_sort()` + `merge()` schreiben · Doku + Git einrichten | M1  |
| Woche 3 | `minimum()` · `maximum()` · `durchschnitt()` · `auswertung()` · Tests T01–T12 | M2  |
| Woche 4 | Tests fertig · 100% Abdeckung · Testprotokoll · Video · Abgabe | M3  |
 
---
 
## 5. Lernjournal
 
### Woche 1
 
| Frage | Antwort |
|---|---|
| Was habe ich gemacht? | Keine Zeit diese Woche. Habe das Briefing kurz gelesen. |
| Was hat gut funktioniert? | Das Briefing war einfach zu verstehen. |
| Was war schwierig? | Keine Zeit gehabt. Big-O war am Anfang schwer zu verstehen. |
| Was habe ich gelernt? | Was Big-O bedeutet und warum MergeSort schneller ist als Selectionsort. |
| Selbsteinschätzung | Note 3 – zu wenig gemacht, hole ich in Woche 2 auf. |
| Ziel nächste Woche | `csv_einlesen()` und `merge_sort()` fertig schreiben. |
 
### Woche 2
 
| Frage | Antwort |
|---|---|
| Was habe ich gemacht? | Rückstand aus Woche 1 aufgeholt. Dokumentation für Teilaufgabe 1, 2 und 3 fertiggestellt und das GitHub Repository eingerichtet. Die README mit der ganzen Dokumentation wurde direkt ins Repo hochgeladen. |
| Was hat gut funktioniert? | Das Einrichten des Git Repositories hat gut geklappt. Die Struktur der Dokumentation war klar. |
| Was war schwierig? | Git war neu für mich. Der Branch hiess master statt main, was einen Fehler beim pushen verursacht hat. |
| Was habe ich gelernt? | Wie man ein Git Repository erstellt, Dateien hinzufügt und auf GitHub hochlädt. |
| Selbsteinschätzung | Note 4 – Rückstand aufgeholt und Repo sauber eingerichtet. |
| Ziel nächste Woche | Alle Funktionen implementieren und erste Tests schreiben. |
 
### Woche 3
 
| Frage | Antwort |
|---|---|
| Was habe ich gemacht? | |
| Was hat gut funktioniert? | |
| Was war schwierig? | |
| Was habe ich gelernt? | |
| Selbsteinschätzung | |
| Ziel nächste Woche | |
 
### Woche 4
 
| Frage | Antwort |
|---|---|
| Was habe ich gemacht? | |
| Was hat gut funktioniert? | |
| Was war schwierig? | |
| Was habe ich gelernt? | |
| Selbsteinschätzung | |
| Ziel nächste Woche | – (Projekt fertig) |
