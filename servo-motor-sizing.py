#!/usr/bin/python3
# encoding: utf-8

"""servo-motor-sizing.py: Script to assist in the dimensioning of servomotors in electrical design."""

__author__ = "Davyd Maker"
__version__ = "1.0"
__email__ = "contato@davydmaker.com.br"

def truncate(s, n):
    i, p, d = "{}".format(s).partition('.')
    return '.'.join([i, d[:n]]).rstrip("0").rstrip(".")

def changePoint(s, decimal, thousand): return thousand.join(str(s).replace(thousand, "").split(decimal))

def splitStrVal(arr): return list(map(lambda rlv: [rlv.split("=")[0], float(changePoint(rlv.split("=")[1], ",", "."))], arr.split("|")))

listSv, listNcd, listRlv = [], [], []

confValores = open("./conf.txt", "r")
for idxL, l in enumerate(confValores):
    l = l.strip()
    if l == "": pass

    if idxL == 0: listRlv = splitStrVal(l)
    elif idxL == 1: listNcd = splitStrVal(l)
    else: listSv.append(list(map(float, [changePoint(tL, ",", ".") for tL in l.split("|")])))

for n in listNcd:
    for idxS, s in enumerate(listSv):
        for r in listRlv:
            if r[0] == "Tipo de Engrenagem": tNota = s[2]
            elif r[0] == "Peso": tNota = -0.05 * s[1] + 10
            elif r[0] == "Necessidade/Torque": tNota = float(truncate(n[1]/s[0], 2)) * 10

            print("[Servo Nº " + str(idxS+1) + " de Torque 4,8V (" + changePoint(s[0], ".", ",") + " N·cm) para " + n[0] + " de Tm " + str(n[1]) + " kg*cm]")
            print("[" + r[0] + " - Relevância: " + str(r[1]) + "]")
            print("Nota: " + changePoint(truncate(tNota, 2), ".", ","))
            print("Total:", changePoint(truncate(float(tNota) * float(r[1]), 2), ".", ","))
            print("\n")