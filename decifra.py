# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

#Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "i"
posB = "l"
posC = "r"
posD = "g"
posE = "a"
posF = "m"
posG = "e"
posH = "k"
posI = "h"
posJ = "t"
posK = "fhjkqrvwxz"
posL = "fhjkqrvwxz"
posM = "p"
posN = "n"
posO = "o"
posP = "fhjkqrvwxz"
posP = "fhjkqrvwxz"
posQ = "d"
posR = "fhjkqrvwxz"
posS = "fhjkqrvwxz"
posP = "fhjkqrvwxz"
posQ = "fhjkqrvwxz"
posR = "fhjkqrvwxz"
posS = "fhjkqrvwxz"
# posK = "jqxz"
posL = "f"
posM = "p"
posN = "n"
posO = "o"
posP = "v"
posQ = "d"
# posR = "jqxz"
# posS = "jqxz"
posT = "s"
posU = "c"
posV = "u"
posW = "y"
posX = "fhjkqrvwxz"
posY = "fhjkqrvwxz"
posZ = "fhjkqrvwxz"
posX = "fhjkqrvwxz"
posY = "fhjkqrvwxz"
posZ = "fhjkqrvwxz"
posX = "fhjkqrvwxz"
posY = "b"
# posZ = "jqxz"

#Texto 1
#En ingles

dicEng = carga('./diccionarios/dicEng.txt')
dicEng = list(set(dicEng))
# print(len(dicEng))

c=0

#Como la letra g es la que mas se repite podemos decir que esta es la letra e

#posG = 'e'

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

#habband

# for p in dicEng:
#       if len(p)==7:
#             if p[1]==p[4] and p[2]==p[3] and p[-2] in posN and p[1] in posA and p[2] in posB:
#                   c+=1
#                   print(p)
# print(c)

#posH = 'rfb'
#posB = 'pl'

#probando con wov: posible palabra you

# for p in dicEng:
#     if len(p)==3:
#          if p[1] in posO and p[2] in posV:
#               c+=1
#               print(p)

#probando con mottgttgq = possessed
#posM=p
#PosQ=d
#PosT=s
# for p in dicEng:
#     if len(p)==9:
#          if p[2]==p[3]and p[5]==p[6]  and p[4]==p[7] and p[4] in posG and p[1] in posO:
#               c+=1
#               print(p)
#posW = 'y'
#posO = 'o'

#afedang
# for p in dicEng:
#     if len(p)==7:
#          if p[0]==p[4] and p[-1] in posG and p[0] in posA:
#               c+=1
#               print(p)

#yguevtg
# for p in dicEng:
#     if len(p)==7:
#          if p[0] in posY and p[1] in posG and p[2] in posU and p[1] == p[-1] and p[3] in posE:
#               c+=1
#               print(p)

#xign
# for p in dicEng:
#     if len(p)==4:
#          if p[2:]=='en' and p[0] in posX and p[1] in posI:
#               c+=1
#               print(p)

#lanq
# for p in dicEng:
#     if len(p)==4:
#          if p[1:]=='ind' and p[0] in posL:
#               c+=1
#               print(p)

#yglocg
# for p in dicEng:
#     if len(p)==6:
#          if p[0:2]=='be' and p[3] in posO and p[-1] in posG:
#               c+=1
#               print(p)

#fechgj
# for p in dicEng:
#     if len(p)==6:
#          if p[:3]=='mar':
#               c+=1
#               print(p)

letras = {"a" : "i","b" : "l","c" : "r","d" : "g","e" : "a","f" : "m","g" : "e","h" : "k","i" : "h","j" : "t","k" : "K","l" : "f","m" : "p","n" : "n","o" : "o","p" : "v","q" : "d","r" : "R","s" : "S","t" : "s","u" : "c","v" : "u","w" : "y","x" : "w","y" : "b","z" : "Z"}
texto1='Jigcg xet onug e Uovnjcwfen xio mottgttgq jig fotj xonqgclvb Dootg wov uen afedang, loc gpgcw qew xign ig patajgq jig ngtj, jig Dootg ieq beaq e ygevjalvb, dbajjgcand, dobqgn gdd. Jig Uovnjcwfen jooh jig gddt jo fechgj enq toon ygden jo dgj caui. Yvj aj xet noj bond yglocg ig dcgx afmejagnj xaji jig Dootg yguevtg tig depg iaf onbw e tandbg dobqgn gdd e qew. Ig xet noj dgjjand caui letj gnovdi. Jign ong qew, eljgc ig ieq lanatigq uovnjand iat fongw, jig aqge uefg jo iaf jiej ig uovbq dgj ebb jig dobqgn gddt ej onug yw habband jig Dootg enq uvjjand aj omgn. Yvj xign jig qggq xet qong, noj e tandbg dobqgn gdd qaq ig lanq, enq iat mcguaovt Dootg xet qgeq'.lower()
texto=''
for i in texto1:
    if i in letras:
        texto+=letras[i]
    else:
        texto+=i

print(texto)