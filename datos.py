# -*- coding: utf-8 -*-

# Definir "constantes" para los tipos de plato
PASTAS = "PASTAS"
ARROCES = "ARROCES"
CALDOS = "CALDOS"
ENSALADAS = "ENSALADAS"
OTROS = "OTROS"

# Definir constantes para los ingredientes
ACELGAS = "acelgas"
AJOS = "ajos"
ALBAHACA = "albahaca"
ALBONDIGAS = "albondigas"
ARROZ = "arroz"
ATUN = "atun"
AVECREM = "avecrem"
BACON = "bacon"
BECHAMEL = "bechamel"
BERENJENAS = "berenjenas"
BROCOLI = "brocoli"
BROTES_SOJA = "brotes soja"
CALABACIN = "calabacin"
CARNE_PICADA = "carne picada"
CEBOLLA = "cebolla"
CHAMPINYONES = "champinyones"
CHORIZO = "chorizo"
GAMBAS = "gambas"
GARBANZOS = "garbanzos"
GUISANTES = "guisantes"
HABICHUELAS = "habichuelas"
HOJALDRE = "hojaldre"
HUEVOS = "huevos"
JAMON_YORK = "jamon york"
LECHUGA = "lechuga"
LASANYA = "lasanya"
LENTEJAS = "lentejas"
MANZANAS = "manzanas"
MORCILLA = "morcilla"
MOZZARELLA = "mozzarella"
NABO = "nabo"
NATA = "nata"
NYOKIS = "nyokis"
PARMESANO = "parmesano"
PASTA = "pasta"
PATATAS = "patatas"
PATE = "pate"
PEPINO = "pepino"
PESTO = "pesto"
PICATOSTES = "picatostes"
PIMIENTO_ROJO = "pimiento rojo"
PIMIENTO_VERDE = "pimiento verde"
PLATANO = "platano"
POLLO = "pollo"
QUESITOS = "quesitos"
QUESO_RALLAR = "queso rallar"
QUINOA = "quinoa"
SALCHICHA_FRANKFURT = "salchicha frankfurt"
SALSA_CESAR = "salsa cesar"
SALSA_SOJA = "salsa soja"
SETAS = "setas"
SPAGETI = "spageti"
SPAM = "spam"
TOMATES = "tomates"
TOMATE_FRITO = "tomate frito"
TORTELLINI = "tortellini"
ZANAHORIAS = "zanahorias"

# Generar lista de recetas
def crearRecetas():
    recetas = list()
    recetas.append(["pasta carbonara", PASTAS, [SPAGETI, NATA, BACON, CEBOLLA, CHAMPINYONES]])
    recetas.append(["pasta boloñesa", PASTAS, [PASTA, TOMATE_FRITO, CARNE_PICADA, CEBOLLA, PARMESANO]])
    recetas.append(["pasta con atun y calabacin", PASTAS, [PASTA, TOMATE_FRITO, ATUN, CALABACIN, PARMESANO]])
    recetas.append(["pasta con pesto", PASTAS, [PASTA, PESTO, ATUN, PARMESANO]])
    recetas.append(["pasta con gambas", PASTAS, [SPAGETI, GAMBAS, AJOS, PARMESANO]])
    recetas.append(["noodles", PASTAS, [SPAGETI, ZANAHORIAS, BROTES_SOJA, PIMIENTO_ROJO, POLLO, SALSA_SOJA]])
    recetas.append(["tortelini con nata", PASTAS, [TORTELLINI, NATA, CEBOLLA]])
    recetas.append(["tortelini con tomate", PASTAS, [TORTELLINI, TOMATE_FRITO, CEBOLLA]])
    recetas.append(["arroz 3 delicias", ARROCES, [ARROZ, GUISANTES, HUEVOS, JAMON_YORK, ZANAHORIAS]])
    recetas.append(["arroz con curry de pollo", ARROCES, [ARROZ, CHAMPINYONES, PIMIENTO_VERDE, CEBOLLA, CALABACIN, POLLO, SALSA_SOJA]])
    recetas.append(["arroz con tomate y pollo", ARROCES, [ARROZ, TOMATE_FRITO, POLLO, CEBOLLA, PIMIENTO_ROJO]])
    recetas.append(["arroz con spam", ARROCES, [ARROZ, TOMATE_FRITO, SPAM, CEBOLLA, PIMIENTO_ROJO]])
    recetas.append(["arroz a la cubana", ARROCES, [ARROZ, TOMATE_FRITO, SALCHICHA_FRANKFURT, CEBOLLA, HUEVOS, PLATANO]])
    recetas.append(["lentejas", CALDOS, [LENTEJAS, CHORIZO, PATATAS, HUEVOS, ZANAHORIAS, CEBOLLA, TOMATES]])
    recetas.append(["habichuelas", CALDOS, [HABICHUELAS, CHORIZO, MORCILLA, BACON, PATATAS]])
    recetas.append(["arroz de los 3 puñaos", CALDOS, [HABICHUELAS, LENTEJAS, GARBANZOS, NABO, ZANAHORIAS, ACELGAS, PATATAS, TOMATES, AJOS, ARROZ]])
    recetas.append(["ensalada de pasta", ENSALADAS, [PASTA, MOZZARELLA, LECHUGA, TOMATES, PEPINO, HUEVOS, ATUN]])
    recetas.append(["ensalada cesar", ENSALADAS, [LECHUGA, POLLO, SALSA_CESAR, PICATOSTES, PARMESANO, BACON]])
    recetas.append(["ensalada con habichuelas", ENSALADAS, [HABICHUELAS, MOZZARELLA, LECHUGA, TOMATES, PEPINO, HUEVOS, ATUN]])
    recetas.append(["lasaña", OTROS, [LASANYA, CARNE_PICADA, PIMIENTO_ROJO, PIMIENTO_VERDE, CEBOLLA, PATE, HUEVOS, TOMATES, TOMATE_FRITO, BECHAMEL, QUESO_RALLAR]])
    recetas.append(["berenjenas con atun", OTROS, [BERENJENAS, ATUN, PIMIENTO_ROJO, CEBOLLA, QUESO_RALLAR]])
    recetas.append(["ñokis con nata", OTROS, [NYOKIS, NATA, CEBOLLA]])
    recetas.append(["ñokis con tomate", OTROS, [NYOKIS, TOMATE_FRITO, CEBOLLA]])
    recetas.append(["empanada de atun", OTROS, [HOJALDRE, CEBOLLA, PIMIENTO_ROJO, TOMATE_FRITO, ATUN, HUEVOS]])
    recetas.append(["brocoli con jamon york y queso", OTROS, [BROCOLI, JAMON_YORK, QUESO_RALLAR, NATA, TOMATES]])
    recetas.append(["pure zanahorias y manzanas", OTROS, [ZANAHORIAS, MANZANAS, QUESITOS]])
    recetas.append(["quinoa con setas", OTROS, [QUINOA, CEBOLLA, SETAS, TOMATES, ALBAHACA]])
    recetas.append(["albondigas con salsa de cebolla", OTROS, [ALBONDIGAS, CEBOLLA, AVECREM]])
    recetas.append(["tortilla patatas", OTROS, [HUEVOS, CEBOLLA, PATATAS]])
    recetas.append(["patatas con pollo con tomate", OTROS, [PATATAS, POLLO, TOMATE_FRITO, PIMIENTO_ROJO]])
    recetas.append(["patatas con bacon y cebolla y queso y nata", OTROS, [PATATAS, BACON, CEBOLLA, NATA, QUESO_RALLAR]])
    recetas.append(["patatas con huevo y verduras", OTROS, [PATATAS, BACON, CEBOLLA, PIMIENTO_VERDE, PIMIENTO_ROJO, QUESO_RALLAR, HUEVOS]])

    return recetas


# Definir diccionario de maximo de repeticiones por tipo
maxPorTipo = {PASTAS:1, ARROCES:1, CALDOS:1, ENSALADAS:1, OTROS:999}
