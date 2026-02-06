# 🧪 Chromatography Column Selector

Ein interaktives Tool zur Auswahl der optimalen Chromatographie-Säule für euer Labor.

## Features

- ✅ Auswahl zwischen Affinity und Size Exclusion Chromatographie
- ✅ Spezifische Empfehlungen für verschiedene Affinity Tags (His, GST, Strep, FLAG, MYC)
- ✅ **Wichtig für Antibody-Reinigung:** Detaillierte Subtyp-spezifische Bindungsinformationen für IgG1-4 (human und mouse), plus Rat IgG
- ✅ Übersichtliche Darstellung von Binding Capacity, Features und Anwendungsempfehlungen
- ✅ SEC-Säulen mit Trenngröße und Anwendungsbereich

## Installation

### Voraussetzungen
- Python 3.7 oder höher
- pip

### Schritt 1: Repository klonen (wenn auf GitHub)
```bash
git clone https://github.com/euer-username/column-selector.git
cd column-selector
```

### Schritt 2: Streamlit installieren
```bash
pip install streamlit
```

Oder erstelle eine `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Verwendung

### Lokal starten
```bash
streamlit run column_selector.py
```

Die App öffnet sich automatisch im Browser unter `http://localhost:8501`

### Online deployen (Streamlit Cloud)

1. Push deinen Code auf GitHub
2. Gehe zu [share.streamlit.io](https://share.streamlit.io)
3. Verbinde dein GitHub Repository
4. Wähle dein Repository und `column_selector.py`
5. Deploy!

Die App ist dann öffentlich verfügbar und ihr könnt sie im Team teilen.

## Workflow

1. **Schritt 1:** Wähle Chromatographie-Art (Affinity oder Size Exclusion)
2. **Schritt 2 (bei Affinity):** Wähle deinen Tag-Typ
3. **Schritt 3 (bei Antibody):** Wähle den spezifischen IgG-Subtyp
4. **Ergebnis:** Erhalte maßgeschneiderte Säulenempfehlungen mit Begründung

## Anpassung

Die Säulen-Datenbank befindet sich in der Variable `COLUMN_DATABASE` am Anfang der `column_selector.py`. 

### Beispiel: Neue Säule hinzufügen

```python
"HisTag": {
    "columns": [
        # Bestehende Säulen...
        {
            "name": "Eure neue Säule",
            "binding_capacity": "30 mg/mL",
            "features": "Besondere Eigenschaften",
            "best_for": "Spezifische Anwendungen"
        }
    ]
}
```

### Beispiel: Neuen Tag hinzufügen

```python
"Neuer-Tag": {
    "columns": [
        {
            "name": "Säulenname",
            "binding_capacity": "Kapazität",
            "features": "Features",
            "best_for": "Anwendung"
        }
    ]
}
```

## Wichtige Hinweise zu Antibody-Subtypen

Das Tool enthält spezifische Bindungsinformationen für:

### Human IgG
- **IgG1:** Protein A (sehr stark), Protein G (stark)
- **IgG2:** Protein G bevorzugt (stark), Protein A schwächer (mittel)
- **IgG3:** Protein G (sehr stark), Protein A vermeiden (schwach)
- **IgG4:** Beide gut (stark)

### Mouse IgG
- **IgG1:** Protein G bevorzugt (sehr stark)
- **IgG2a:** Protein A exzellent (sehr stark)
- **IgG2b:** Protein G leicht besser (sehr stark)
- **IgG3:** ⚠️ WICHTIG! Anti-Mouse IgG verwenden, Protein A bindet NICHT

### Rat IgG
- Protein G bevorzugt (stark)

## Team-Zusammenarbeit

### Option 1: GitHub
1. Erstellt ein gemeinsames Repository
2. Jeder klont das Repo
3. Änderungen werden gepusht und von allen gepullt
4. Pull Requests für größere Änderungen

### Option 2: Streamlit Cloud (empfohlen)
1. Deploy auf Streamlit Cloud
2. Link teilen: `https://euer-app-name.streamlit.app`
3. Alle können direkt nutzen ohne Installation
4. Updates automatisch nach Git-Push

## Lizenz

Für euer Labor entwickelt - freie Nutzung und Anpassung!

## Kontakt

Bei Fragen oder Verbesserungsvorschlägen: Einfach ein Issue erstellen oder direkt im Code anpassen 😊
