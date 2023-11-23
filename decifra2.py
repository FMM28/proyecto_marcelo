# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

# Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "abcdefghijklmnopqrstuvwxyz"
posB = "sc"
posC = "abcdefghijklmnopqrstuvwxyz"
posD = "u"
posE = "abcdefghijklmnopqrstuvwxyz"
posF = "abcdefghijklmnopqrstuvwxyz"
posG = "abcdefghijklmnopqrstuvwxyz"
posH = "abcdefghijklmnopqrstuvwxyz"
posI = "abcdefghijklmnopqrstuvwxyz"
posJ = "e"
posK = "rl"
posL = "abcdefghijklmnopqrstuvwxyz"
posM = "abcdefghijklmnopqrstuvwxyz"
posN = "abcdefghijklmnopqrstuvwxyz"
posO = "abcdefghijklmnopqrstuvwxyz"
posP = "abcdefghijklmnopqrstuvwxyz"
posQ = "abcdefghijklmnopqrstuvwxyz"
posR = "gq"
posS = "abcdefghijklmnopqrstuvwxyz"
posT = "abcdefghijklmnopqrstuvwxyz"
posU = "abcdefghijklmnopqrstuvwxyz"
posV = "abcdefghijklmnopqrstuvwxyz"
posW = "abcdefghijklmnopqrstuvwxyz"
posX = "abcdefghijklmnopqrstuvwxyz"
posY = "abcdefghijklmnopqrstuvwxyz"
posZ = "abcdefghijklmnopqrstuvwxyz"

dicFr=carga('./diccionarios/dicFr.txt')
dicFr=list(set(dicFr))
# print(len(dicFr))

#igual que el texto 1 deducimos que la j es una e por ser la que tiene mayor frecuencia

c=0

#rdjkkjb
# for p in dicFr:
#     if len(p)==7:
#          if p[2]==p[5] and p[2] in posJ and p[3]==p[4]:
#               c+=1
#               print(p)

# guerres quelles querrec

#posR = 'gq'
#posD = 'u'
#posK = 'rl'
#posB = 'sc'

#rkpgajzrj
for p in dicFr:
      if len(p) == 9:
        if p[5] == p[-1] and p[5] == posJ and p[0] in posR:
             c += 1
             print(p)