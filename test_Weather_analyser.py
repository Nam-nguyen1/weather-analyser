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

def test_csv_einlesen(tmp_path):
    datei = tmp_path / "test.csv"
    datei.write_text("datum;temperatur;windgeschwindigkeit;schneehoehe\n2024-01-15;-8.2;34;120\n", encoding="utf-8")
    res = csv_einlesen(str(datei))
    assert len(res) == 1 and res[0]["temperatur"] == -8.2
    
    with pytest.raises(FileNotFoundError):
        csv_einlesen("null.csv")
    
    datei.write_text("datum;temperatur;windgeschwindigkeit;schneehoehe\n2024-01-15;X;34;120\n")
    with pytest.raises(ValueError):
        csv_einlesen(str(datei))

def test_min_max():
    assert minimum(BEISPIEL, "temperatur")["temperatur"] == -15.3
    assert maximum(BEISPIEL, "temperatur")["temperatur"] == -1.8
    assert minimum(BEISPIEL, "windgeschwindigkeit")["windgeschwindigkeit"] == 11.0
    assert maximum(BEISPIEL, "schneehoehe")["schneehoehe"] == 130.0
    assert minimum([], "t") is None
    assert maximum([], "t") is None

def test_durchschnitt():
    assert durchschnitt(BEISPIEL, "temperatur") == -7.43
    assert durchschnitt(BEISPIEL, "schneehoehe") == 123.14
    assert durchschnitt([], "t") is None

def test_merge_sort():
    sort = merge_sort(BEISPIEL, "temperatur")
    assert [e["temperatur"] for e in sort] == [-15.3, -12.5, -8.2, -6.4, -4.7, -3.1, -1.8]
    
    sort2 = merge_sort(BEISPIEL, "schneehoehe")
    assert [e["schneehoehe"] for e in sort2] == [118.0, 119.0, 120.0, 122.0, 125.0, 128.0, 130.0]
    
    orig = list(BEISPIEL)
    merge_sort(BEISPIEL, "temperatur")
    assert BEISPIEL == orig