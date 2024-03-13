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