sNum=input("Introducir un numero de maximo de 4 digitos al menos 2 diferentes")
print(sNum)
num=int(sNum)
numR=0
for k in range(99): #Maximo 99 iteraciones
    sNum="{:04d}".format(num)                       #123 --> "0123"
    sNumG="".join(sorted(sNum,reverse=True))        #"0123" --> "3210"
    sNumP="".join(sorted(sNum))                     #"0123" --> "0123", "4563", --> "3456", "8703" --> "0378"
    num=int(sNumG)-int(sNumP)
    print(sNumG, sNumP, num,"({:02d})".format(k+1))
    if num==numR:
        break
    numR=num
print ("----------")
print ("FINAL", num, numR, "Iteraciones: ", k+1)
