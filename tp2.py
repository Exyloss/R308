#!/usr/bin/env python3

class Etudiant:
    def __init__(self, nom, prenom, notes=[]):
        self.nom = nom
        self.prenom = prenom
        self.notes = notes

    def __str__(self):
        return f"nom : {self.nom.upper()}, prénom : {self.prenom}, notes: {[i[0] for i in self.notes]}, coef : {[i[1] for i in self.notes]}"

    def ajouterNote(self, note, coef):
        self.notes = self.notes+[(note, coef)]

    def nbNotes(self):
        return len(self.notes)

    def moyenne(self):
        if self.nbNotes() == 0:
            return -1
        s = 0
        n = 0
        for i in self.notes:
            s += i[0]*i[1]
            n += i[1]
        return s/n

class Promotion:
    def __init__(self, etudiants=[]):
        self.etudiants = etudiants

    def ajouterEtudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def nbEtudiants(self):
        return len(self.etudiants)

    def moyenne(self):
        if self.nbEtudiants() == 0:
            return -1
        else:
            n = 0
            s = 0
            for i in self.etudiants:
                moy = i.moyenne()
                if moy != -1:
                    s += moy
                    n += 1
            return s/n


def main():
    etud1 = Etudiant("Master (flop)", "Noob")
    etud1.ajouterNote(15, 5)
    etud1.ajouterNote(13, 7)
    etud1.ajouterNote(15, 1)
    etud1.ajouterNote(3, 2)
    print(etud1.moyenne())

    etud2 = Etudiant("lespes de chien", "bastos")
    etud2.ajouterNote(2, 5)
    etud2.ajouterNote(12, 7)
    etud2.ajouterNote(3, 1)
    etud2.ajouterNote(15, 2)
    print(etud2.moyenne())

    promo = Promotion()
    promo.ajouterEtudiant(etud1)
    promo.ajouterEtudiant(etud2)
    print(promo.moyenne())

if __name__ == "__main__":
    main()
