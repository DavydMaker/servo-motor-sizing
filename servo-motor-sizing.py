#!/usr/bin/python3
# encoding: utf-8

"""servo-motor-sizing.py: Script to assist in the dimensioning of servomotors in electrical design."""

__author__ = "Davyd Maker"
__version__ = "1.3"
__email__ = "contato@davydmaker.com.br"

def truncate(s, n):
    i, p, d = "{}".format(s).partition('.')
    return '.'.join([i, d[:n]]).rstrip("0").rstrip(".")

def changePoint(s, decimal, thousand): return thousand.join(str(s).replace(thousand, "").split(decimal))

def splitStrVal(arr): return list(map(lambda rlv: [rlv.split("=")[0], float(changePoint(rlv.split("=")[1], ",", "."))], arr.split("|")))

listSv, listSprf, listRlv = [], [], []

confValores = open("./conf.txt", "r")
for idxL, l in enumerate(confValores):
    l = l.strip()
    if l == "": pass

    if l.count("=") > 1:
        l = l.split("|")
        listSprf.append(splitStrVal(l[0])[0])
        listRlv.append(splitStrVal("|".join(l[1:])))
    else: listSv.append(list([l.split("=")[0], [float(changePoint(tL, ",", ".")) for tL in l.split("=")[1].split("|")]]))


arq = open("./result.txt", "w+")
for n, rList in zip(listSprf, listRlv):
    for idxS, s in enumerate(listSv):
        for idxR, r in enumerate(rList):
            if r[0] == "Confiabilidade": tNota = s[1][3]
            elif r[0] == "Tipo de Engrenagem": tNota = s[1][2]
            elif r[0] == "Peso": tNota = -0.05 * s[1][1] + 10
            elif r[0] == "Necessidade/Torque": tNota = float(truncate(n[1]/s[1][0], 2)) * 10

            arq.write("[Servo " + s[0] + " de Torque (4,8V) " + changePoint(s[1][0], ".", ",") + " N·cm para " + n[0] + " de Tm " + str(n[1]) + " kg*cm]\n")
            arq.write("[" + r[0] + " - Relevância: " + str(r[1]) + "]\n")
            arq.write("Nota: " + changePoint(truncate(tNota, 2), ".", ",") + "\n")
            arq.write("Total: " + str(changePoint(truncate(float(tNota) * float(r[1]), 2), ".", ",")) + "\n")
            arq.write("\n")

arq.close()