# Proyecto 3 - Katas Python
from functools import reduce
import math

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_letras(cadena):
    # Diccionario por comprensión para contar las apariciones de cada letra, ignorando espacios.
    cadena_limpia = cadena.replace(" ", "")
    return {letra: cadena_limpia.count(letra) for letra in set(cadena_limpia)}

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa map().
def doble_valores(lista):
    # map aplica una función lambda a cada elemento de la lista.
    return list(map(lambda x: x * 2, lista))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo.
# Devuelve una lista con las palabras de la original que contengan la objetivo.
def buscar_palabra(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa map().
def diferencia_listas(lista1, lista2):
    # map recibe multiples iterables, la función lambda toma un elemento de cada uno.
    return list(map(lambda x, y: x - y, lista1, lista2))

# 5. Calcular media y estado (aprobado/suspenso) devolviendo tupla.
def calcular_media_estado(numeros, nota_aprobado=5):
    media = sum(numeros) / len(numeros) if numeros else 0
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial_recursivo(n):
    # Caso base: 0! y 1! son 1. Llamada recursiva n * (n-1)!
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa map().
def tuplas_a_strings(lista_tuplas):
    # Transforma cada elemento de la tupla en string y los une.
    return list(map(lambda tupla: "".join(str(e) for e in tupla), lista_tuplas))

# 8. Programa que pida dos números e intente dividirlos, manejando excepciones.
def division_segura():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print(f"División exitosa: {resultado}")
    except ValueError:
        print("Error: Has ingresado un valor no numérico.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

# 9. Función que excluya mascotas prohibidas usando filter().
def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # filter mantiene solo los elementos para los cuales la lambda devuelve True.
    return list(filter(lambda m: m not in prohibidas, mascotas))

# 10. Calcular promedio de lista. Si está vacía lanza excepción personalizada.
class ListaVaciaError(Exception):
    pass

def promedio_excepcion(lista):
    if not lista:
        raise ListaVaciaError("La lista de números está vacía, no se puede calcular el promedio.")
    return sum(lista) / len(lista)

# 11. Programa que pida la edad y maneje excepciones si no es numérico o está fuera de rango (0-120).
def validar_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango válido (0-120).")
        print(f"Edad registrada: {edad}")
    except ValueError as e:
        print(f"Entrada inválida: {e}")

# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa map().
def longitud_palabras(frase):
    return list(map(len, frase.split()))

# 13. Para un conjunto de caracteres, devolver lista de tuplas (mayus, minus). Sin repetidos, usar map().
def letras_mayus_minus(caracteres):
    # set(caracteres) asegura que no haya repeticiones.
    return list(map(lambda c: (c.upper(), c.lower()), set(caracteres)))

# 14. Retorna palabras que comiencen con letra específica usando filter().
def empiezan_con_letra(lista, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista))

# 15. Función lambda que sume 3 a cada número de una lista.
sumar_tres_lista = lambda lista: list(map(lambda x: x + 3, lista))

# 16. Devuelve palabras más largas que n usando filter().
def palabras_mas_largas(cadena, n):
    return list(filter(lambda p: len(p) > n, cadena.split()))

# 17. Convierte lista de dígitos a número usando reduce().
def lista_a_numero(digitos):
    # reduce acumula el valor: a=5, b=7 -> 5*10+7=57. Luego a=57, b=2 -> 57*10+2=572.
    return reduce(lambda a, b: a * 10 + b, digitos)

# 18. Filtra estudiantes con calificación >= 90.
def estudiantes_destacados(estudiantes):
    # estudiantes es una lista de diccionarios: [{'nombre': 'A', 'edad': 20, 'calificacion': 95}, ...]
    return list(filter(lambda est: est.get('calificacion', 0) >= 90, estudiantes))

# 19. Función lambda que filtre impares de una lista.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# 20. Filtra solo los values int de una lista mixta con filter().
def filtrar_integers(lista):
    return list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), lista))

# 21. Función lambda que calcule el cubo de un número.
cubo = lambda x: x ** 3

# 22. Producto total de una lista numérica usando reduce().
def producto_total(lista):
    return reduce(lambda a, b: a * b, lista)

# 23. Concatena lista de palabras con reduce().
def concatenar_palabras(lista):
    return reduce(lambda a, b: a + b, lista)

# 24. Diferencia total en valores de una lista usando reduce().
def diferencia_total(lista):
    if not lista: return 0
    return reduce(lambda a, b: a - b, lista)

# 25. Crea una función que cuente el número de caracteres en una cadena.
def contar_caracteres(cadena):
    return len(cadena)

# 26. Función lambda que calcule el resto de la división entre dos números.
resto = lambda x, y: x % y

# 27. Promedio de lista de números.
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

# 28. Devuelve el primer elemento duplicado en una lista.
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# 29. Convierte a texto y enmascara con '#' excepto últimos 4.
def enmascarar(variable):
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

# 30. Determina si dos palabras son anagramas.
def son_anagramas(palabra1, palabra2):
    # Se normalizan los espacios y se ordenan los caracteres para compararlos directamente.
    return sorted(palabra1.replace(" ", "").lower()) == sorted(palabra2.replace(" ", "").lower())

# 31. Busca nombre en lista (ingresados por usuario) e imprime o lanza excepción.
def buscar_nombre_interactivo():
    nombres = input("Ingresa una lista de nombres separados por coma: ").split(",")
    nombres = [n.strip() for n in nombres]
    objetivo = input("Ingresa el nombre a buscar: ").strip()
    
    if objetivo in nombres:
        print("El nombre fue encontrado.")
    else:
        raise ValueError(f"Excepción: El nombre '{objetivo}' no se encuentra en la lista.")

# 32. Busca empleado por nombre y devuelve su puesto, o mensaje si no existe.
def buscar_empleado(nombre, empleados):
    # Asume que empleados es un diccionario { 'Nombre': 'Puesto' }
    return empleados.get(nombre, "La persona no trabaja aquí")

# 33. Función lambda que sume elementos correspondientes de dos listas dadas.
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

# 34. Clase Arbol
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, pos):
        if 0 <= pos < len(self.ramas):
            self.ramas.pop(pos)

    def info_arbol(self):
        return f"Tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes ramas: {self.ramas}"

# Caso de uso Arbol
# a = Arbol()
# a.crecer_tronco()
# a.nueva_rama()
# a.crecer_ramas()
# a.nueva_rama(); a.nueva_rama()
# a.quitar_rama(2)
# print(a.info_arbol())

# 35. Clase UsuarioBanco
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"Saldo insuficiente para {self.nombre}.")
        self.saldo -= cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # Se reutilizan los métodos de la propia clase para asegurar validaciones.
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)

# Caso de uso UsuarioBanco
# alicia = UsuarioBanco("Alicia", 100, True)
# bob = UsuarioBanco("Bob", 50, True)
# bob.agregar_dinero(20)
# bob.transferir_dinero(alicia, 80) # Lanza ValueError por saldo (50+20=70 < 80)
# alicia.retirar_dinero(50)

# 36. Función procesar_texto con submétodos.
def procesar_texto(texto, opcion, *args):
    def contar_palabras(t):
        palabras = t.split()
        return {p: palabras.count(p) for p in set(palabras)}
        
    def reemplazar_palabras(t, orig, nueva):
        return t.replace(orig, nueva)
        
    def eliminar_palabra(t, pal):
        # Filtra las palabras asegurando que coincidan exactamente (no subcadenas)
        return " ".join([p for p in t.split() if p != pal])
        
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"

# 37. Indica día, tarde o noche según hora.
def momento_dia(hora):
    if 6 <= hora < 13:
        return "Es de día"
    elif 13 <= hora < 20:
        return "Es de tarde"
    else:
        return "Es de noche"

# 38. Calificación en texto según calificación numérica.
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota fuera de rango"

# 39. Calcular área según figura y tupla de datos.
def calcular_area(figura, datos):
    if figura == "rectangulo":
        # datos = (base, altura)
        return datos[0] * datos[1]
    elif figura == "circulo":
        # datos = (radio,)
        return math.pi * (datos[0] ** 2)
    elif figura == "triangulo":
        # datos = (base, altura)
        return (datos[0] * datos[1]) / 2
    else:
        raise ValueError("Figura no soportada")

# 40. Calcula monto final de compra en tienda online con condicionales.
def calcular_descuento_compra():
    try:
        precio_original = float(input("Ingrese el precio original del artículo: "))
        tiene_cupon = input("¿Tiene un cupón de descuento? (sí/no): ").strip().lower()
        
        if tiene_cupon == "sí" or tiene_cupon == "si":
            descuento = float(input("Ingrese el valor del cupón de descuento: "))
            if descuento > 0:
                precio_final = precio_original - descuento
                print(f"Precio con descuento: {max(0, precio_final):.2f}")
            else:
                print(f"Cupón inválido. Precio final: {precio_original:.2f}")
        elif tiene_cupon == "no":
            print(f"Precio final: {precio_original:.2f}")
        else:
            print(f"Respuesta no válida. Precio final: {precio_original:.2f}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para el precio y descuento.")