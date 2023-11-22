# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

#Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "i"
posB = "abdfhjklmopqrvwxyz"
posC = "abdfhjklmopqrvwxyz"
posD = "g"
posE = "abdfhjklmopqrvwxyz"
posF = "abdfhjklmopqrvwxyz"
posG = "e"
posH = "abdfhjklmopqrvwxyz"
posI = "abdfhjklmopqrvwxyz"
posJ = "t"
posK = "abdfhjklmopqrvwxyz"
posL = "abdfhjklmopqrvwxyz"
posM = "abdfhjklmopqrvwxyz"
posN = "n"
posO = "op"
posP = "abdfhjklmopqrvwxyz"
posQ = "s"
posR = "abdfhjklmopqrvwxyz"
posS = "abdfhjklmopqrvwxyz"
posT = "abdfhjklmopqrvwxyz"
posU = "c"
posV = "u"
posW = "yc"
posX = "abdfhjklmopqrvwxyz"
posY = "abdfhjklmopqrvwxyz"
posZ = "abdfhjklmopqrvwxyz"

#Texto 1
#En ingles

dicEng = carga('./diccionarios/dicEng.txt')
dicEng = list(set(dicEng))
# print(len(dicEng))

c=0

#Como la letra g es la que mas se repite podemos decir que esta es la letra e

#posG = 'e'

#probando con qggq

# for p in dicEng:
#       if len(p)==4:
#             if p[1]==p[2] and p[1] in posG and p[0]==p[-1]:
#                   c+=1
#                   print(p)
# print(c)

#sees
#posQ = 's'

# dgjjand
# for p in dicEng:
#       if len(p)==7:
#             if p[2]==p[3] and p[1] in posG and p[-1]==p[0]:
#                   c+=1
#                   print(p)
# print(c)

#getting

#posJ = 't'
#posA = 'i'
#posN = 'n'
#posD = 'g'

# uvjjand

# for p in dicEng:
#       if len(p)==7:
#             if p[2:]=='tting':
#                   c+=1
#                   print(p)
# print(c)

#cutting

#posU = 'c'
#posV = 'u'

#probando con poon: posibles o:opmd

# for p in dicEng:
#       if len(p)==4:
#             if p[1]==p[2]:
#                   c+=1
#                   print(p)
# print(c)

#posO = 'opmd'

#probando con wov: posible palabra you

for p in dicEng:
    if len(p)==3:
         if p[1] in posO and p[2] in posV:
              c+=1
              print(p)