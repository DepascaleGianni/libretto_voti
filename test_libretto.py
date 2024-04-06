from voto import Libretto, Voto

lib = Libretto()

v1 = Voto("analisi 1", 10, 20, False, '2022-01-30')
lib.append(Voto('Fisica 1', 10, 25, False, '2022-07-12'))
lib.append(Voto('Analisi 2', 8, 30,True,'2023-02-15'))

voti25 = lib.findByPunteggio(25,False)
for v in voti25:
    print(v.esame)
try:
    voto_analisi2 = lib.findByEsame2("Analisi 2")
    print(f"Hai preso {voto_analisi2.str_punteggio()}")
except ValueError:
    print("nessun voto trovato")

lib.append(Voto('Basi dari 1', 8, 26, False, '2023-09-11'))
lib.append(Voto('info 1', 6, 29, False, '2022-02-12'))
lib.append(Voto('tdp 1', 10, 21, False, '2022-01-31'))

migliorato = lib.crea_migliorato()

ordinato_punteggio = lib.crea_ord_per_punteggio()
print("\noriginale")
lib.stampa()
print("\nmigliorato")
migliorato.stampa()
print("\nordinato per punteggio")
ordinato_punteggio.stampa()
ordinato_punteggio.cancella_inferiori(24)
print("\nordinato per punteggio senza voti brutti")
ordinato_punteggio.stampa()

