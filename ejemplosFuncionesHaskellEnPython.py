#sumar::[Int]->Int
#sumar [ ] = 0
#sumar (x:xs) = x + sumar(xs)
#Main> sumar [5,4,7,8]
#24

def sumar(lista):
	y=0
	for x in lista:
		y+=x
	return y

print(sumar(lista=[5,4,7,8]))

#invertir::Ord a=>[a]->[a]
#invertir [ ] = [ ]
#invertir (x:xs) = (invertir xs)++[x]
#Main> invertir [5,4,7,8]
#[8,7,4,5]

def invertir(lista):
	listaInv=[]
	y=(len(lista)-1)
	for x in range (len(lista)):
		listaInv.append(lista[y])
		y-=1
	return listaInv

print(invertir(lista=[5,4,7,8]))

#igualLista:: Eq a => [a]->[a]->Bool
#igualLista l1 l2 = l1 == l2
#Main> igualLista ["Hola","Mundo"] ["Mundo","Hola"]
#False

def igualLista(lista1, lista2):
	si=True
	if (len(lista1)!=len(lista2)):
		si=False
	elif (len(lista1)>=len(lista2)):
		largo=len(lista1)
	else:
		largo=len(lista2)
	if(si):
		for x in range (largo):
			if(lista1[x] != lista2[x]):
				si=False
				break
	return si

print(igualLista(lista1=["Hola","Mundo"], lista2=["Mundo","Hola"]))

#lista_ordenada::Ord a=>[a]->Bool
#lista_ordenada [] = True
#lista_ordenada [_] = True
#lista_ordenada (x:y:xs) = (x<=y) && lista_ordenada
#(y:xs)
#Main> lista_ordenada ['a','b','c','d']
#True

def listaOrdenada(lista):
	y=ord(lista[0])
	si=True
	for x in lista:
		if(y>ord(x)):
			si=False
			break
		y=ord(x)
	return si

print(listaOrdenada(lista=['a','b','c','d']))

#mostrar_ubicacion::Ord a=>[a]->Int->a
#mostrar_ubicacion l n = l!!n
#Main> mostrar_ubicacion [15,25,26,28] 2
#26

def mostrarUbicacion(lista, posicion):
	return lista[posicion]

print(mostrarUbicacion(lista=[15,25,26,28], posicion = 2))

#mayor::[Int]->Int
#mayor (x:xs)
#| x > mayor(xs) = x
#| otherwise = mayor(xs)
#Main> mayor [78,24,56,93,21,237,46,74,125]
#237

def mayor(lista):
	may = lista[0]
	for x in lista:
		if(may<x):
			may=x
	return may

print(mayor(lista=[78,24,56,93,21,237,46,74,125]))

#contarpares::[Int]->Int
#contarpares []=0
#contarpares lista= length [x | x <- lista, mod x 2 ==0]
#Main> contarpares [5,4,7,8]
#2

def contarPares(lista):
	pares=0
	for x in lista:
		if(x%2==0):
			pares+=1
	return pares

print(contarPares(lista=[5,4,7,8]))

#cuadrados::[Int]->[Int]
#cuadrados [ ] = [ ]
#cuadrados l = [x*x| x <- l]
#Main> cuadrados [1..10]
#[1,4,9,16,25,36,49,64,81,100]

def cuadrados(lista):
	x=1
	while x<=10:
		lista.append(x*x)
		x+=1
	return lista

print(cuadrados(lista=[]))

#divisible::Int->Int->Bool
#divisible x y = (mod x y) ==0
#divisibles::Int->[Int]
#divisibles x = [y | y <-[1..x],divisible x y]
#esPrimo::Int->Bool
#esPrimo n = length (divisibles n) <=2
#primos::Int->[Int]
#primos n = [x | x <-[1..n],esPrimo x]
#Main> primos 100
#[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,
#71,73,79,83,89,97]

def divisible(x, y):
	return (x%y==0)

def divisibles(n):
	listaDiv = []
	listaY = []
	y=1
	while y<=n:
		listaY.append(y)
		y+=1
	for i in listaY:
		if(divisible(n,i)):
			listaDiv.append(i)
	return listaDiv

def esPrimo(n):
	return (len(divisibles(n))<=2)

def primos(n):
	lista = []
	x=1
	while x<=n:
		if(esPrimo(x)):
			lista.append(x)
		x+=1
	return lista

print(primos(n=100))
