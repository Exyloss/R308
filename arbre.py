#!/usr/bin/env python3


class Expression:
    def __init__(self, g, d):
        self.g = g
        self.d = d

class Constante(Expression):
    def __init__(self, valeur):
        self.valeur = valeur

    def notationInFixee(self):
        return str(self.valeur)

    def notationPostFixee(self):
        return str(self.valeur)

    def evaluer(self):
        return self.valeur

class OperateurBinaire(Expression):
    def __init__(self, g, d):
        super().__init__(g, d)

class Plus(OperateurBinaire):
    def __init__(self, g, d):
        super().__init__(g, d)

    def opname(self):
        return "+"

    def notationInFixee(self):
        return "( "+self.g.notationInFixee()+" + "+self.d.notationInFixee()+" )"

    def notationPostFixee(self):
        return self.g.notationPostFixee()+" "+self.d.notationPostFixee()+" + "

    def evaluer(self):
        return self.g.evaluer()+self.d.evaluer()

class Moins(OperateurBinaire):
    def __init__(self, g, d):
        super().__init__(g, d)

    def opname(self):
        return "-"

    def notationInFixee(self):
        return "( "+self.g.notationInFixee()+" - "+self.d.notationInFixee()+" )"

    def notationPostFixee(self):
        return self.g.notationPostFixee()+" "+self.d.notationPostFixee()+" - "

    def evaluer(self):
        return self.g.evaluer()-self.d.evaluer()

class Diviser(OperateurBinaire):
    def __init__(self, g, d):
        super().__init__(g, d)

    def opname(self):
        return "/"

    def notationInFixee(self):
        return self.g.notationInFixee()+" / "+self.d.notationInFixee()

    def notationPostFixee(self):
        return self.g.notationPostFixee()+" "+self.d.notationPostFixee()+" / "

    def evaluer(self):
        return self.g.evaluer()/self.d.evaluer()

class Multiplier(OperateurBinaire):
    def __init__(self, g, d):
        super().__init__(g, d)

    def opname(self):
        return "*"

    def notationInFixee(self):
        return self.g.notationInFixee()+" * "+self.d.notationInFixee()

    def notationPostFixee(self):
        return self.g.notationPostFixee()+" "+self.d.notationPostFixee()+" * "

    def evaluer(self):
        return self.g.evaluer()*self.d.evaluer()

arbre = Moins(Plus(Constante(3), Multiplier(Constante(2), Constante(6))), Multiplier(Constante(2), Plus(Constante(4), Constante(9))))
print(arbre.notationInFixee()," = ",arbre.evaluer())
