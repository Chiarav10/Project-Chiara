# ⚡ Energieverbruik en Financiele  Analyse Tool
Dit Python Project bestaat uit twee onderdelen:
1. Opdracht1.py -> Energieverbruik van een bedrijfspand en vergelijkt dit met CBS-gemiddelden (op basis van oppervlakte, bouwjaar en type onderneming).
2. Opdracht2.py -> Financiële cashflow-berekeningen van IRR, REV, Winst na belasting en TVT
Het If-statment werkt volledig, maar bevat maar op een plek de berekeningen en het ophalen van de data

Extra -- test.py -> Filterd door de database heen om gelijk de juiste Categorie te krijgen (vergelijk opdracht1.py) bevat niet de desbeteffende formules

## 📁 Bestandsstructuur

- `PraeterBV_Case.xlsx` – Excelbestand met inputgegevens
- `oprdacht1.py` – Hoofdscript voor Energieverbuik analyse
- `oprdacht2.py` – Hoofdscript voor Financiele analyse
- `requirements.txt` – Benodigde Python-pakketten

## ⚙️ Functionaliteiten
opdracht1.py - Energieverbruik
- Leest gegevens uit Excel (Opdracht_1_voorbeeld en Opdracht_1_CBS)
- Herkent automatisch type pand (zoals detailhandel met/zonder koeling) -> het If-statment werkt volledig, helaas heeft maar een optie alle nodige instanties 
- Berekent huidig verbruik per m² en m³ (gas, elektra, totaal)
- Vergelijkt huidig verbruik met CBS-gemiddelden
- Laat verschillen zien in tabellen en grafiek

opdracht2.py – financiële berekeningen
- Haalt cashflows op uit Excel (Opdracht_2_berekening en output)
- Berekent:
  - IRR 
  - REV
  - Winst na belasting 
  - TVT
- Alle berekeningen in losse functies


## 🚀 Installatie

1. Clone dit project of download de bestanden.
2. Zorg dat Python 3.9+ is geïnstalleerd.
3. Instaleer de benodigde packages:
```bash
  ip install -r requirements.txt 
```
4. Run een van de scripts:
```bash
  python opdracht1.py
  python opdracht2.py
```
