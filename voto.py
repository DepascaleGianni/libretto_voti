from dataclasses import dataclass
@dataclass
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
            return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"


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

