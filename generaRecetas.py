# -*- coding: utf-8 -*-
import random
import datos

recetas = datos.crearRecetas()

# Preguntar al usuario
userInput = raw_input("Cuantas recetas quieres? (5 por defecto) > ")
try:
	if len(userInput) > 0 :
		cant_comidas = int(userInput)
	else :
		cant_comidas = 5
except:
	print "Introduce un numero valido"

# Mostrar x recetas aleatoriamente
menu = list()
carro = list()
totalRecetas = len(recetas) - 1
countRecetas = 0
countPorTipo = {datos.PASTAS:0, datos.ARROCES:0, datos.CALDOS:0, datos.ENSALADAS:0, datos.OTROS:0}
while countRecetas < cant_comidas:
	plato = random.randint(0, totalRecetas)
	# Comprobar que el plato no se ha añadido ya
	if plato not in menu :
		# Comprobar que no se ha llegado al maximo del tipo de esta receta
		tipoReceta = recetas[plato][1]
		if countPorTipo[tipoReceta] < datos.maxPorTipo[tipoReceta] :
			print "Receta", countRecetas+1, ": ", recetas[plato][0]
			menu.append(plato)
			countRecetas = countRecetas + 1
			countPorTipo[tipoReceta] = countPorTipo[tipoReceta] + 1
			# Crear carro compra
			carro = carro + recetas[plato][2]

# Crear lista de la compra segun las recetas seleccionadas (eliminar repetidos y ordenar alfabeticamente)
listaCompra = list()
for ingrediente in carro :
	if ingrediente not in listaCompra :
		listaCompra.append(ingrediente)
listaCompra.sort()
print "Ingredientes: ", listaCompra
