#!/usr/bin/env python3
# -*- coding: latin-1 -*-

class Security:
    def __init__(self):
        ips = []
        flags = []

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

    def ControlLines(self, lines):
        print(lines)
