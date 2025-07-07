# Energieverbruik Analyse Tool

Dit Python-script analyseert het energieverbruik van een bedrijf op basis van gegevens uit een Excel-bestand en vergelijkt dit met landelijke CBS-gemiddelden. Het resultaat wordt weergegeven in een overzichtelijke tabel en een grafiek.
Het If-statment werkt volledig, maar bevat maar op een plek de berekeningen en het ophalen van de data

## 📁 Bestandsstructuur

- `PraeterBV_Case.xlsx` – Excelbestand met inputgegevens
- `main.py` – Hoofdscript voor analyse
- `requirements.txt` – Benodigde Python-pakketten

## ⚙️ Functionaliteiten

- Leest bedrijfsinformatie uit een Excelbestand
- Berekent huidig gas- en elektriciteitsverbruik per m² en m³
- Vergelijkt huidig verbruik met CBS-gemiddelden op basis van bouwjaar, type pand en oppervlakte
- Visualiseert vergelijking met een grafiek
- Ondersteunt meerdere categorieën zoals:
  - Detailhandel (met/zonder koeling)
  - Groothandel
  - Autobedrijf

## 🚀 Installatie

1. Clone dit project of download de bestanden.
2. Zorg dat Python 3.9+ is geïnstalleerd.
3. Installeer de benodigde packages:


```bash
pip install -r requirements.txt
python main.py
