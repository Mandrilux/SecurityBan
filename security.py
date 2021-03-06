#!/usr/bin/env python3
# -*- coding: latin-1 -*-

class Security:
    def __init__(self):
        self._ips = []
        self._flags = ["Failed", "Invalid", "error", "not", "failure"]
        self._lines = []

    def extractIp(self, line):
        return True


    """ Fonction qui permet de detecter un flag,
    Si le flag est present dans la string, la fonction
    retourne la valeur 1 , sinon elle retourne la valeur 0 """


    def detectFlag(self, s, key):
        if s.find(key) == -1:
            return 0
        else:
            return 1


    """ Cette fonction permet d'effectuer un controle sur
    les nouvelles lignes trouvées dans un fichier de log """


    def controlLines(self, lines):
        self._lines = lines
        for i in range(0, len(self._lines)):
            print(self._lines[i])
            for z in range(0, len(self._flags)):
                if self.detectFlag(self._lines[i], self._flags[z]) == 1:
                    print ("extraction ip")
                    self.extractIp(lines[i])


    """ Setter / getter """

    def setLines(self, lines):
        self._lines = lines

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value

    @property
    def flags(self):
        return self._flags
