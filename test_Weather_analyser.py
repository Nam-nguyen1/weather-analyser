import pytest
from Weather_analyser import csv_einlesen, merge_sort, minimum, maximum, durchschnitt

BEISPIEL = [
    {"datum": "2024-01-15", "temperatur": -8.2,  "windgeschwindigkeit": 34.0, "schneehoehe": 120.0},
    {"datum": "2024-01-16", "temperatur": -3.1,  "windgeschwindigkeit": 18.0, "schneehoehe": 118.0},
    {"datum": "2024-01-17", "temperatur": -12.5, "windgeschwindigkeit": 52.0, "schneehoehe": 125.0},
    {"datum": "2024-01-18", "temperatur": -1.8,  "windgeschwindigkeit": 11.0, "schneehoehe": 119.0},
    {"datum": "2024-01-19", "temperatur": -6.4,  "windgeschwindigkeit": 29.0, "schneehoehe": 122.0},
    {"datum": "2024-01-20", "temperatur": -15.3, "windgeschwindigkeit": 61.0, "schneehoehe": 130.0},
    {"datum": "2024-01-21", "temperatur": -4.7,  "windgeschwindigkeit": 22.0, "schneehoehe": 128.0},
]

def test_csv_einlesen_korrekt(tmp_path):
    datei = tmp_path / "wetterdaten.csv"
    datei.write_text(
        "datum;temperatur;windgeschwindigkeit;schneehoehe\n"
        "2024-01-15;-8.2;34;120\n",
        encoding="utf-8"
    )
    result = csv_einlesen(str(datei))
    assert len(result) == 1
    assert result[0]["temperatur"] == -8.2

def test_csv_einlesen_datei_nicht_gefunden():
    with pytest.raises(FileNotFoundError):
        csv_einlesen("gibt_es_nicht.csv")

def test_csv_einlesen_ungueltige_daten(tmp_path):
    datei = tmp_path / "kaputt.csv"
    datei.write_text(
        "datum;temperatur;windgeschwindigkeit;schneehoehe\n"
        "2024-01-15;FALSCH;34;120\n",
        encoding="utf-8"
    )
    with pytest.raises(ValueError, match="Ungültige Daten"):
        csv_einlesen(str(datei))

def test_minimum_temperatur():
    result = minimum(BEISPIEL, "temperatur")
    assert result["temperatur"] == -15.3
    assert result["datum"] == "2024-01-20"

def test_maximum_temperatur():
    result = maximum(BEISPIEL, "temperatur")
    assert result["temperatur"] == -1.8
    assert result["datum"] == "2024-01-18"

def test_minimum_windgeschwindigkeit():
    assert minimum(BEISPIEL, "windgeschwindigkeit")["windgeschwindigkeit"] == 11.0

def test_maximum_schneehoehe():
    assert maximum(BEISPIEL, "schneehoehe")["schneehoehe"] == 130.0

def test_minimum_leere_liste():
    assert minimum([], "temperatur") is None

def test_maximum_leere_liste():
    assert maximum([], "temperatur") is None

def test_durchschnitt_temperatur():
    assert durchschnitt(BEISPIEL, "temperatur") == -7.43

def test_durchschnitt_schneehoehe():
    assert durchschnitt(BEISPIEL, "schneehoehe") == 123.14

def test_durchschnitt_leere_liste():
    assert durchschnitt([], "temperatur") is None

def test_merge_sort_temperatur():
    sortiert = merge_sort(BEISPIEL, "temperatur")
    werte = [e["temperatur"] for e in sortiert]
    assert werte == [-15.3, -12.5, -8.2, -6.4, -4.7, -3.1, -1.8]

def test_merge_sort_schneehoehe():
    sortiert = merge_sort(BEISPIEL, "schneehoehe")
    werte = [e["schneehoehe"] for e in sortiert]
    assert werte == [118.0, 119.0, 120.0, 122.0, 125.0, 128.0, 130.0]

def test_merge_sort_veraendert_original_nicht():
    kopie = list(BEISPIEL)
    merge_sort(BEISPIEL, "temperatur")
    assert BEISPIEL == kopie