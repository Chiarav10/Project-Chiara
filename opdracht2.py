import pandas as pd
import numpy_financial as npf

# Zet IRR waarde om naar Percentage 
def irr_naar_percentage(irr_waarde):
    return round(irr_waarde * 100, 2)

# Bouwt de output
def bouw_irr_tekst(omschrijving, percentage):
    return omschrijving + ": " + str(percentage) + "%"

# Roept Percentage en output op en print de waarde
def print_interne_rentevoet(irr_waarde, omschrijving):
    percentage = irr_naar_percentage(irr_waarde)
    tekst = bouw_irr_tekst(omschrijving, percentage)
    print(tekst)

# Telt alle winst na belasting bij elkaar op
def bereken_winst_na_belasting(rij_nummer, sheet_data):
    rij_index = rij_nummer - 1 
    waarden = sheet_data.iloc[rij_index, 3:34].tolist()  
    waarden = [float(x) if not pd.isna(x) else 0 for x in waarden]
    return sum(waarden)

# Berekent TVT en veranderd naar Float voor afronding getal
def bereken_TVT(rij_nummer, sheet_data):
    rij_index = rij_nummer - 1
    waarden = sheet_data.iloc[rij_index, 3:16].tolist()  # kolommen D t/m P
    waarden = [float(x) if not pd.isna(x) else float('inf') for x in waarden]
    minimum_waarde = min(waarden)
    return round (minimum_waarde, 2)

# Leest Excel bestand uit, haalt benodigde rijen/colommen op, Zet alles om naar Float voor legen cellen, Berekent IRR en REV, winst na belasting en TVT
def opdracht2():
    bestand = 'PraeterBV_Case.xlsx'
    sheet3 = 'Opdracht_2_berekening en output'

    cashflow_data = pd.read_excel(bestand, sheet_name=sheet3, header=None)

    cashflow_IRR = cashflow_data.iloc[25, 3:34].tolist()
    cashflow_IRR = [float(x) if not pd.isna(x) else 0 for x in cashflow_IRR]
    irr_1 = npf.irr(cashflow_IRR)
    print_interne_rentevoet(irr_1, "IRR Cashflow")

    cashflow_rev = cashflow_data.iloc[26, 3:34].tolist()
    cashflow_rev = [float(x) if not pd.isna(x) else 0 for x in cashflow_rev]
    irr_rev = npf.irr(cashflow_rev)
    print_interne_rentevoet(irr_rev, "IRR Cashflow REV")

    totaal_winst_na_belasting = bereken_winst_na_belasting(25, cashflow_data)
    print("Winst na belasting:", round(totaal_winst_na_belasting))

    tvt = bereken_TVT(28, cashflow_data)
    print("TVT:", tvt)


if __name__ == "__main__":
    opdracht2()