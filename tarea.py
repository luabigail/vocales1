file = open("vocales", "r")
vocales = ('a', 'e', 'i', 'o', 'u')
cadena=file.read()
s=cadena.lower()
for letra in vocales:
   s = s.replace(letra, "")
print s
archivo=open('sin.txt','w')
archivo.write(s)
archivo.close()