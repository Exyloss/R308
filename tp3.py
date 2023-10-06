#!/usr/bin/env python3

class Heure:
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __str__(self):
        if m < 10:
            m_str = "0"+str(m)
        else:
            m_str = str(m)

        if h < 10:
            h_str = "0"+str(h)
        else:
            h_str = str(h)

        return f"{h_str}:{m_str}"
    def compareTo(self, heure):
        self_time = self.h*60+self.m
        heure_time = heure.h*60+heure.m
        if self_time < heure_time:
            return -1
        elif self_time == heure_time:
            return 0
        else:
            return 1
    def get_hour(self):
        return self.h
    def get_minute(self):
        return self.m

class Creneau:
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin
    def conflictWith(self, creneau):
        return (self.debut.compareTo(creneau.debut) == 0) \
            or (self.debut.compareTo(creneau.debut) <= 0 and self.fin.compareTo(creneau.debut) > 0) \
            or (self.debut.compareTo(creneau.debut) > 0 and self.debut.compareTo(creneau.fin) <= 0)
    def duree(self):
        return (self.fin.get_hour()+self.fin.get_minute()/60)-(self.debut.get_hour()+self.debut.get_minute()/60)

class Planning:
    def __init__(self):
        self.planning = []
    def ajouterCreneau(self, c):
        for i in self.planning:
            if c.conflictWith(i):
                return -1
        self.planning = self.planning + [c]
        return 0
    def dureeTotale(self):
        return sum([i.duree() for i in self.planning])

class CreneauCours(Creneau):
    def __init__(self, debut, fin):
        super().__init__(debut, fin)
    def dureeETD(self):
        dur = self.duree()
        return dur*1.5

class CreneauTD(Creneau):
    def __init__(self, debut, fin):
        super().__init__(debut, fin)
    def dureeETD(self):
        dur = self.duree()
        return dur

class CreneauTP(Creneau):
    def __init__(self, debut, fin):
        super().__init__(debut, fin)
    def dureeETD(self):
        dur = self.duree()
        return dur*2/3


if __name__ == "__main__":
    c = CreneauTD(Heure(10, 30), Heure(11, 30))
    print(c.dureeETD())
