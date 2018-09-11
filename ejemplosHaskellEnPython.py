#? length [1,3,10]
#3
lista=[1,3,10]
print(len(lista))
#? [1,3,10] ++ [2,6,5,7]
#[1, 3, 10, 2, 6, 5, 7]
lista2=[2,6,5,7]
print(lista + lista2)
#? concat [[1], [2,3], [], [4,5,6]]
#[1, 2, 3, 4, 5, 6]
a=[1]
b=[2,3]
c=[]
d=[4,5,6]
print(a+b+c+d)
#? map fromEnum ['H', 'o', 'l', 'a']
#[104, 111, 108, 97]
carac=['h','o','l','a']
carac2=[]
for x in carac:
	carac2.append(ord(x))
print(carac2)

###############################SECUENCIAS#####################################
#? [1..]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, etc...
##inf=[1]
##for x in inf:
##	inf.append(x+1)
##print(inf)	#ciclo infinito, no compila bien, pausar compilacion

#? [-3..3]
#[-3, -2, -1, 0, 1, 2, 3]
lista=[]
x=-3
while x <=3:
	lista.append(x)
	x+=1
print(lista)
#? [1..1]
#[1]
lista=[]
x=1
while x<=1:
	lista.append(x)
	x+=1
print(lista)
#? [9..0]
#[]
lista=[]
x=9
while x<=0:
	lista.append(x)
	x+=1
print(lista)
#RESUMIENDO EN UNA FUNCION
#def llenarLista(self, a, b, lista):
#	x=a
#	while x<=b:
#		lista.append(x)
#		x+=1

#? [1,3..]
#[1, 3, 5, 7, 9, 11, 13, etc...
##inf=[1,3]
##x=inf[1]-inf[0]
##while len(inf)>=2:
##	inf.append(inf[len(inf)-1]+x)	#ciclo infinito, no compila bien, pausar compilacion

#? [0,0..]
#[0, 0, 0, 0, 0, 0, 0, etc...
##inf=[0,0]
##x=inf[1]-inf[0]
##while len(inf)>=2:
##	inf.append(inf[len(inf)-1]+x)	#ciclo infinito, no compila bien, pausar compilacion

#? [5,4..]
#[5, 4, 3, 2, 1, 0, -1, etc...
##inf=[5,4]
##x=inf[1]-inf[0]
##while len(inf)>=2:
##	inf.append(inf[len(inf)-1]+x)	#ciclo infinito, no compila bien, pausar compilacion

#RESUMIENDO EN UNA FUNCION
#def llenarLista(self, lista):
#	x=lista[1]-lista[0]
#	while len(lista)>=2:
#		lista.append(lista[len(lista)-1]+x)

#? [1,3..12]
#[1, 3, 5, 7, 9, 11]
lista=[1,3]
x=lista[1]-lista[0]
while lista[len(lista)-1]+x <=12:
	lista.append(lista[len(lista)-1]+x)
print(lista)

#? [0,0..10]
#[0, 0, 0, 0, 0, 0, 0, etc...
##lista=[0,0]
##x=lista[1]-lista[0]
##while lista[len(lista)-1]+x <=10:
##	lista.append(lista[len(lista)-1]+x)
##print(lista)	#ciclo infinito, no compila bien, pausar compilacion

#? [5,4..1]
#[5, 4, 3, 2, 1]
lista=[5,4]
x=lista[1]-lista[0]
while lista[len(lista)-1]+x >=1:
	lista.append(lista[len(lista)-1]+x)
print(lista)

##RESUMIENDO EN UNA FUNCION
#def llenarLista(self, lista, max):
#	x=lista[1]-lista[0]
#	if(x>=0):
#		while lista[len(lista)-1]+x <=max:
#			lista.append(lista[len(lista)-1]+x)
#		print(lista)
#	else:
#		while lista[len(lista)-1]+x >=max:
#			lista.append(lista[len(lista)-1]+x)
#		print(lista)	

#? ['0'..'9'] ++ ['A'..'Z']
#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
carac=['0']
carac2=['A']
x=ord(carac[0])
while x<57:
	x+=1
	carac.append(chr(x))
print(carac)
x=ord(carac2[0])
while x<90:
	x+=1
	carac2.append(chr(x))
print(carac2)
print(carac+carac2)
#? [1.2, 1.35 .. 2.00]
#[1.2, 1.35, 1.5, 1.65, 1.8, 1.95]
lista=[1.2,1.35]
x=lista[1]-lista[0]
while lista[len(lista)-1]+x <=2.00:
	lista.append(lista[len(lista)-1]+x)
print(lista)

##################LISTAS POR COMPREHENSION####################################

#? [x | x <- [1 .. 12]]
#[1,2,3,4,5,6,7,8,9,10,11,12]
lista=[]
x=1
while x<=12:
	lista.append(x)
	x+=1
print(lista)
#? [x+x | x <- [1 .. 12]]
#[2,4,6,8,10,12,14,16,18,20,22,24]
lista=[]
x=1
while x<=12:
	lista.append(x+x)
	x+=1
print(lista)
#? [x*x | x <- [1..10]]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista=[]
x=1
while x<=10:
	lista.append(x*x)
	x+=1
print(lista)

#? [x*x |x<-[1..10], even x ]
#[4,16,36,64,100]
lista=[]
x=1
while x<=10:
	if((x*x)%2 == 0): 
		lista.append(x*x)
	x+=1
print(lista)
#? [x | x <- [1..10], mod x 5 ==0]
#[5,10]
lista=[]
x=1
while x<=10:
	if(x%5 == 0):
		lista.append(x)
	x+=1
print(lista)