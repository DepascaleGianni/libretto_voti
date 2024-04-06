import operator
from dataclasses import dataclass
from operator import attrgetter
@dataclass()
class Voto:
    esame: str
    cfu : int
    punteggio:int
    lode :bool
    data : str

    # def __eq__(self, other):
    #     if self.esame == other.esame and self.punteggio == other.punteggio and
    #         self.lode == other.lode
    #         return True
    #     else:
    #         return False

    def str_punteggio(self):
        if self.punteggio == 30 and self.lode:
            return f"30 e lode"
        else:
            return f"{self.punteggio}"

    def __str__(self):
            return f"Esame {self.esame} ({self.cfu} cfu) superato con {self.punteggio} in {self.data}"

    def __repr__(self):
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"

    def copy(self):
        return Voto(self.esame,self.cfu,self.punteggio,self.lode,self.data)


class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        if not self.has_voto(voto) and not self.has_conflitto(voto):
            self._voti.append(voto)
        else:
            raise ValueError("Voto non valido")

    def media(self):
        if len(self._voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)


    def findByPunteggio(self, punteggio, lode):
        """
        Seleziona i soli esami con punteggio definito
        :param punteggio: intero che rappresenta il punteggio
        :param lode: booleano che indica la presenza di lode
        :return: lista di oggetti di tipo voto con punteggio specificato
        """
        voti_scelti = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                voti_scelti.append(v)
        return voti_scelti

    def findByEsame(self,esame):
        """
        Seleziona esame dato il suo nome
        :param esame: stringa col nome dell'esame
        :return: ritorno l'oggetto voto corrispondente oppure None se non trovato
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        return None

    def findByEsame2(self,esame):
        """
        Seleziona esame dato il suo nome
        :param esame: stringa col nome dell'esame
        :return: ritorno l'oggetto voto corrispondente oppure scatena una eccezione ValueError
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError("Esame non trovato")

    def has_voto(self,voto):
        for v in self._voti:
            if v.esame == voto.esame and v.lode == voto.lode and v.punteggio == voto.punteggio:
                return True
        return False

    def has_conflitto(self,voto):
        for v in self._voti:
            if v.esame == voto.esame and not (v.lode == voto.lode and v.punteggio == voto.punteggio):
                return True
        return False

    def copy(self):
        l = Libretto()
        for v in self._voti:
            l._voti.append(v.copy())
        return l

    def crea_migliorato(self):
        """
        Crea una copia del libretto migliorandone i voti presenti
        :return:
        """
        # l._voti = self._voti.copy() posso usare se cambio la lista ma qui
        # cambio i contenuti quindi non va bene perchè cambio anche l'originale
        l = self.copy()
        for el in l._voti:
            if 18 <=el.punteggio <= 23:
                el.punteggio += 1
            elif 24 <=el.punteggio <= 28:
                el.punteggio += 2
            elif el.punteggio == 29:
                el.punteggio = 30

        return l

    def stampa(self):
        print(f"Hai {len(self._voti)} voti:")
        for v in self._voti:
            print(v)
        print(f"la media vale {self.media()}")

    def stampaGUI(self):
        outList = []
        outList.append(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            outList.append(v)
        outList.append(f"la media vale {self.media()}")
        return outList

    """
    opzione 1 : stampaPerNome e stampaPerPunteggio che stampano e non modificano nulla
    
    pzione 2 : crea_lib_per_nome e crea_lib_ord_per_voto
    
    opzione 3 : crea metodo ordina_per_nome o per punt che modificano il libretto stesso aggiungendo metodo copy()
    
    """
    def crea_ord_per_esame(self):
        nuovo = self.copy()
        nuovo.ordina_per_esame()
        return nuovo

    def ordina_per_esame(self):
        self._voti.sort(key=operator.attrgetter('esame'))
        #self._voti.sort(key=lambda v:v.esame) quando devo ordinare non direttamente con attr
        return self

    """
    opzioni
    1: creo lt per l'oggetto che voglio ordinare e chiamo direttamente sort
    2: chiamo sort passandogli una funziona che estrae elementi definiti e su cui viene applicato il metodo lt
    """
    def crea_ord_per_punteggio(self):
        nuovo = self.copy()
        nuovo._voti.sort(key=lambda v: (v.punteggio,v.lode),reverse=True)
        return nuovo

    def cancella_inferiori(self,punteggio):
        self._voti = [v for v in self._voti if v.punteggio >= punteggio]


