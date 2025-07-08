import pandas as pd
import numpy as np

def vert_zoeken_bouwjaar_en_oppervlakte(df, bouwjaar, categorie, oppervlakte_waarde):
    print("Kolomnamen in df:")
    print(df.columns.tolist())

    # Stap 1: filter op categorie
    df_cat = df[df['Energiekentallen utiliteitsbouw dienstensector; bouwjaarklasse'] == categorie].copy()
    print(f"Aantal rijen na filter op categorie '{categorie}': {len(df_cat)}")

    # Stap 2: converteer MIN en MAX kolommen naar numeriek
    df_cat['Unnamed: 1'] = pd.to_numeric(df_cat['Unnamed: 1'], errors='coerce')
    df_cat['Unnamed: 2'] = pd.to_numeric(df_cat['Unnamed: 2'], errors='coerce')

    print("MIN waarden voorbeeld:", df_cat['Unnamed: 1'].dropna().head())
    print("MAX waarden voorbeeld:", df_cat['Unnamed: 2'].dropna().head())

    # Stap 3: filter op bouwjaar tussen MIN en MAX
    df_bouwjaar = df_cat[
        (df_cat['Unnamed: 1'] <= bouwjaar) & (df_cat['Unnamed: 2'] >= bouwjaar)
    ]
    print(f"Aantal rijen na filter op bouwjaar {bouwjaar}: {len(df_bouwjaar)}")
    if df_bouwjaar.empty:
        print("Geen rijen gevonden met bouwjaar binnen MIN/MAX.")
        return None

    # Stap 4: zoek juiste kolommen op basis van oppervlakte-waarde (numeriek)
    # Hier staat de oppervlakteklasse in rij 11 (pas indien nodig)
    oppervlakte_rij = df.iloc[11]  

    kolommen = []

    for i, (kolomnaam, cel) in enumerate(oppervlakte_rij.items()):
        if pd.notna(cel):
            cel_str = str(cel).replace("–", "-").replace("\xa0", " ").lower().strip()
            # cel_str is bv "250 tot 500 m²"
            # Maak er 2 getallen van:
            if "tot" in cel_str:
                delen = cel_str.replace("m²", "").strip().split("tot")
                try:
                    min_waarde = int(delen[0].strip().replace(" ", ""))
                    max_waarde = int(delen[1].strip().replace(" ", ""))
                    # Check of oppervlakte_waarde binnen het bereik valt:
                    if min_waarde <= oppervlakte_waarde <= max_waarde:
                        kolommen.append(kolomnaam)
                except Exception as e:
                    # Als het niet lukt om te parsen, gewoon verder
                    continue

    if not kolommen:
        print(f"Geen kolommen gevonden voor oppervlakte waarde {oppervlakte_waarde}")
        return None

    # Stap 5: print waarden uit de juiste kolommen
    resultaten = {}
    for kolom in kolommen:
        waarde = df_bouwjaar.iloc[0][kolom]
        if waarde != '.':
            resultaten[kolom] = waarde

    return resultaten if resultaten else None


# Voorbeeld gebruik:
df = pd.read_excel("PraeterBV_Case.xlsx", sheet_name="Opdracht_1_CBS", header=0)

bouwjaar = 1980
categorie = "Detailhandel met koeling"
oppervlakte_waarde = 800  # nu als getal

resultaat = vert_zoeken_bouwjaar_en_oppervlakte(df, bouwjaar, categorie, oppervlakte_waarde)

if resultaat:
    print("\n✅ Resultaten voor oppervlakteklasse:")
    for kolom, waarde in resultaat.items():
        print(f"{kolom}: {waarde}")
else:
    print("\n❌ Geen resultaten gevonden.")
