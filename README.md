# weather-analyser

**Auftraggeber:** Bergbahnen Flumserberg AG, Flums 

## Inhaltsverzeichnis
 
1. [Projektbeschreibung](#1-projektbeschreibung)
2. [Teilaufgabe 1 – Analyse](#2-teilaufgabe-1--analyse)
3. [Teilaufgabe 2 – Design](#3-teilaufgabe-2--design)
4. [Teilaufgabe 3 – Planung](#4-teilaufgabe-3--planung)
5. [Lernjournal](#5-lernjournal)

## 1. Projektbeschreibung
 
Die Bergbahnen Flumserberg AG betreibt mehrere automatische Wettermessstationen auf bis zu 2 220 m ü. M. im Kanton St. Gallen. Jede Station zeichnet stündlich drei Messgrössen auf: Temperatur (°C), Windgeschwindigkeit (km/h) und Schneehöhe (cm). Die Daten werden als CSV-Dateien lokal gespeichert.
 
**Problem:** Das Technik-Team öffnet die Dateien manuell in Excel – bei mehreren Hundert Zeilen dauert das viel zu lange.
 
**Lösung:** Ein Python-Script `weather_analyser.py`, das eine CSV-Datei einliest, die Messwerte mit MergeSort sortiert und automatisch Minimum, Maximum und Durchschnitt berechnet. Alle Funktionen sind mit Unit-Tests (pytest) auf 100% Statement Coverage geprüft.

