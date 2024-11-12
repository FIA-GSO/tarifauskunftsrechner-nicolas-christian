preis_erwachsene = 5.0
preis_kinder = 2.5
preis_jugendliche = 3.5
preis_premium = 3.0
preis_basis = 4.0
preis_sekt = 0.75

while (True):
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
    if alter_gast <18 and alter_gast >14:
        print(" ### Eintritt Jugendliche ###")
        print(" Preis: ",preis_jugendliche, " Euro ")
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input()
        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Preis: ", preis_premium, " Euro ")
            glas_sekt = input(" Wollen Sie für 0.75 Euro noch ein Glas Sekt dazu? (ja/nein): ")
            if glas_sekt == "nein":
                continue
            if glas_sekt == "ja":
                zusammen = [preis_premium, preis_sekt, ]
                plus = sum(zusammen)
                print(" Preis: ", plus, "Euro")
                break
    if antwort_rabatt == "b":
        print(" ### Eintritt Basis-Mitglied ### ")
        print(" Preis: ", preis_basis, " Euro ")
    else:
        print(" ### Eintritt Erwachsene (voller Preis) ### ")
        print(" Preis: ", preis_erwachsene, " Euro")
    print("Wollen Sie einen weiteren Tarif abfragen?\n")
    print("für eine weitere abfrage geben sie 'ja' ein für keine weitere Abfrage geben sie 'nein' ein.")
    neustart = input()
    if neustart == "ja":
        preis_neu_berechnen = "ja"
    if neustart == "nein":
        preis_neu_berechnen = "nein"
    print("Viel Spaß!")