import pandas as pd
import matplotlib.pyplot as plt


def main():
    bestand = pd.ExcelFile("PraeterBV_Case.xlsx")
    sheet2 = pd.read_excel(bestand, sheet_name="Opdracht_1_CBS")
    sheet1 = pd.read_excel(bestand, sheet_name="Opdracht_1_voorbeeld")

    try:
        # Input gegevens vanuit het Excel bestand
        naam = sheet1.iloc[4, 3]
        straat = sheet1.iloc[5, 3]
        postcode = sheet1.iloc[6, 3]
        plaats = sheet1.iloc[7, 3]
        gas = sheet1.iloc[11, 3]
        elektriciteit = sheet1.iloc[12, 3]
        energetische_waarde = sheet1.iloc[13, 3]
        totaal = sheet1.iloc[14, 3]
        verdieping = sheet1.iloc[17, 3]
        bouwjaar = 1919
        categorie = sheet1.iloc[19, 3]
        oppervlakte = sheet1.iloc[20, 3]
        hoogte = sheet1.iloc[21, 3]
        totaal_gemiddeld_m2 = None
        totaal_gemiddeld_m3 = None

            # Categorie: detailhandel met koeling
        def detailhandel_koeling(totaal_berekeningen):
            if 0 < bouwjaar < 1922:
                print("0-1921")
                if 0 < oppervlakte <= 250:
                    pass
                elif 251 <= oppervlakte <= 500:
                    gemiddeld_gas_verbruik = sheet2.iloc[14, 4]
                    return gemiddeld_gas_verbruik
                elif 501 <= oppervlakte <= 1000:
                    print("test2")
                elif 1001 <= oppervlakte <= 2500:
                    print("test3")
                elif 2501 <= oppervlakte <= 5000:
                    print("test4")
                elif oppervlakte >= 5001:
                    print("het werkt!")
                else:
                    print("Onbekend oppervlak")
            elif 1922 <= bouwjaar < 1977:
                print("1922-1976")
                if 0 < oppervlakte <= 250:
                    print("test")
                elif 251 <= oppervlakte <= 500:
                    print("test2")
                elif 501 <= oppervlakte <= 1000:
                    print("test3")
                elif 1001 <= oppervlakte <= 2500:
                    print("test4")
                elif 2501 <= oppervlakte <= 5000:
                    print("het werkt!")
                else:
                    print("Onbekend oppervlak")
            elif 1977 <= bouwjaar < 1994:
                print("1977-1993")
                if 0 < oppervlakte <= 250:
                    print("test")
                elif 251 <= oppervlakte <= 500:
                    print("test2")
                elif 501 <= oppervlakte <= 1000:
                    print("test3")
                elif 1001 <= oppervlakte <= 2500:
                    print("test4")
                elif 2501 <= oppervlakte <= 5000:
                    print("het werkt!")
                else:
                    print("Onbekend oppervlak")
            elif 1994 <= bouwjaar < 2026:
                print("1994-2025")
                if 0 < oppervlakte <= 250:
                    print("test")
                elif 251 <= oppervlakte <= 500:
                    print("test2")
                elif 501 <= oppervlakte <= 1000:
                    print("test3")
                elif 1001 <= oppervlakte <= 2500:
                    print("test4")
                elif 2501 <= oppervlakte <= 5000:
                    print("het werkt!")
                else:
                    print("Onbekend oppervlak")
            else:
                print("Dit is geen bekend bouwjaar")

        # Categorie: detailhandel zonder koeling
        def detailhandel_zonder_koeling():
            if 0 < bouwjaar < 1922:
                if 0 < oppervlakte < 251:
                    print("test")
                elif 250 < oppervlakte < 501:
                    print("test2")
                elif 500 < oppervlakte < 1001:
                    print("test3")
                elif 1000 < oppervlakte < 2501:
                    print("test4")
                elif 2500 < oppervlakte < 5001:
                    # Berekening gemiddeld gebruik
                    gemiddeld_gas_m2 = sheet2.iloc[18, 8]
                    gemiddeld_gas_m3 = gemiddeld_gas_m2 / 2.7
                    totaal_gas = gemiddeld_gas_m2 * oppervlakte

                    gemiddeld_elektriciteit_m2 = sheet2.iloc[19, 13]
                    totaal_elektriciteit = gemiddeld_elektriciteit_m2 + gemiddeld_gas_m3 * 10
                    gemiddeld_elektriciteit_m3 = gemiddeld_elektriciteit_m2 / 2.7

                    totaal_gemiddeld_m2 = (gemiddeld_gas_m2 + gemiddeld_elektriciteit_m2) * energetische_waarde
                    totaal_gemiddeld_m3 = (gemiddeld_gas_m3 + gemiddeld_elektriciteit_m3) * energetische_waarde
                    totaal_gemiddeld = (totaal_gas + totaal_elektriciteit) * energetische_waarde

                    data = {
                        "Gemiddeld verbruik": ["Per m2", "Per m3", "Totaal"],
                        "Gas (m³)": [gemiddeld_gas_m2, gemiddeld_gas_m3, totaal_gas],
                        "Elektriciteit (kWh)": [gemiddeld_elektriciteit_m2, gemiddeld_elektriciteit_m3, totaal_elektriciteit],
                        "Totaal": [totaal_gemiddeld_m2, totaal_gemiddeld_m3, totaal_gemiddeld]
                    }

                    tabel = pd.DataFrame(data)
                    print(tabel)

                    return totaal_gemiddeld_m2, totaal_gemiddeld_m3
                else:
                    print("Er is geen bekend oppervlak aanwezig")
            else:
                print("Onbekend bouwjaar of oppervlakte")
            return totaal_gemiddeld_m2, totaal_gemiddeld_m3

        def groothandel_zonder_koeling():
            print("groothandel zonder koeling")  # Plaatsvervanger voor echte berekening

        def autobedrijf():
            print("autobedrijf: showroom en garage")  # Plaatsvervanger voor echte berekening

        def onbekend():
            print("Dit is geen erkende categorie")

        # Switch-case logica
        switch = {
            "detailhandel met koeling": detailhandel_koeling,
            "detailhandel zonder koeling": detailhandel_zonder_koeling,
            "groothandel zonder koeling": groothandel_zonder_koeling,
            "autobedrijf: showroom en garage": autobedrijf
        }

        categorie_key = categorie.strip().lower()
        functie = switch.get(categorie_key, onbekend)
        totaal_gemiddeldes = functie()

        if totaal_gemiddeldes is None:
            totaal_gemiddeld_m2, totaal_gemiddeld_m3 = None, None
        else:
            totaal_gemiddeld_m2, totaal_gemiddeld_m3 = totaal_gemiddeldes

        # Bereken huidig verbruik
        def totaal_berekeningen():
            m2_gas = gas / oppervlakte
            m2_el = elektriciteit / oppervlakte
            m2_totaal = (elektriciteit + gas * energetische_waarde) / oppervlakte

            m3_gas = gas / (oppervlakte * hoogte)
            m3_el = elektriciteit / (oppervlakte * hoogte)
            m3_totaal = (elektriciteit + gas * energetische_waarde) / (oppervlakte * hoogte)

            totaal_huidig = gas + elektriciteit * energetische_waarde

            data = {
                "Huidig verbruik": ["Per m2", "Per m3", "Totaal"],
                "Gas (m³)": [m2_gas, m3_gas, gas],
                "Elektriciteit (kWh)": [m2_el, m3_el, elektriciteit],
                "Totaal": [m2_totaal, m3_totaal, totaal_huidig]
            }

            tabel = pd.DataFrame(data)
            print(tabel)

            return m2_totaal, m3_totaal

        m2_totaal, m3_totaal = totaal_berekeningen()

        def grafiek(m2_totaal, gem_m2, m3_totaal, gem_m3):
            categorieen = ['Huidig verbruik m2', 'Gemiddeld verbruik m2', 'Huidig verbruik m3', 'Gemiddeld verbruik m3']
            verbruik = [m2_totaal, gem_m2, m3_totaal, gem_m3]

            plt.bar(categorieen, verbruik, color='skyblue')
            plt.title('Huidig verbruik vs Gemiddeld verbruik (kWh)')
            plt.xlabel('Categorie')
            plt.ylabel('Verbruik (kWh)')
            plt.tight_layout()
            plt.show()

        grafiek(m2_totaal, totaal_gemiddeld_m2, m3_totaal, totaal_gemiddeld_m3)

    except FileNotFoundError:
        print(f"Fout: Het bestand '{bestand}' is niet gevonden.")
    except Exception as e:
        print("Er is een fout opgetreden:", e)


if __name__ == "__main__":
    main()
