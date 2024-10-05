import re
from itertools import chain, combinations

# Función para cargar la gramática desde un archivo
def cargar_gramatica(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            gramaticas = archivo.readlines()
            return [linea.strip() for linea in gramaticas if linea.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
        return []

# Función para validar la sintaxis de una producción
def validar_produccion(produccion):
    regex = r"^[A-Z]\s*->\s*([a-zA-Z0-9]+(\s*\|\s*[a-zA-Z0-9]+)*)*$"
    return re.match(regex, produccion)

# Función para validar una gramática completa
def validar_gramatica(gramatica):
    for produccion in gramatica:
        if not validar_produccion(produccion):
            print(f"Error: La producción '{produccion}' no está bien escrita.")
            return False
    return True

# Función para encontrar los no-terminales anulables (que producen epsilon)
def encontrar_anulables(gramatica):
    anulables = set()
    for produccion in gramatica:
        no_terminal, cuerpo = produccion.split("->")
        no_terminal = no_terminal.strip()
        cuerpos = [p.strip() for p in cuerpo.split('|')]
        for c in cuerpos:
            if c == 'epsilon':
                anulables.add(no_terminal)
                break
    return anulables

# Generador de subconjuntos para eliminar producciones-𝜀
def obtener_subconjuntos(simbolos):
    return chain.from_iterable(combinations(simbolos, r) for r in range(len(simbolos)+1))

# Función para eliminar las producciones-𝜀 de la gramática
def eliminar_producciones_epsilon(gramatica):
    anulables = encontrar_anulables(gramatica)
    nuevas_producciones = []

    for produccion in gramatica:
        no_terminal, cuerpo = produccion.split("->")
        no_terminal = no_terminal.strip()
        cuerpos = [p.strip() for p in cuerpo.split('|')]

        # Eliminar cuerpos que contienen epsilon
        cuerpos = [c for c in cuerpos if c != 'epsilon']
        
        # Generar nuevas producciones sin los símbolos anulables
        nuevas_subproducciones = set(cuerpos)
        for c in cuerpos:
            simbolos = list(filter(lambda x: x in anulables, c))
            for subconjunto in obtener_subconjuntos(simbolos):
                nueva_produccion = c
                for simbolo in subconjunto:
                    nueva_produccion = nueva_produccion.replace(simbolo, "")
                if nueva_produccion and nueva_produccion != no_terminal:
                    nuevas_subproducciones.add(nueva_produccion)
        
        # Agregar la producción resultante si no está vacía
        if nuevas_subproducciones:
            nuevas_producciones.append(f"{no_terminal} -> {' | '.join(nuevas_subproducciones)}")

    # Eliminar las producciones que ya no tienen cuerpo
    nuevas_producciones_finales = []
    for produccion in nuevas_producciones:
        no_terminal, cuerpo = produccion.split("->")
        cuerpos = [p.strip() for p in cuerpo.split('|')]
        if cuerpos:
            nuevas_producciones_finales.append(produccion)

    return nuevas_producciones_finales

# Función para eliminar producciones unarias (A -> B)
def eliminar_producciones_unarias(gramatica):
    nuevas_producciones = []
    unarias = {}

    # Identificar las producciones unarias
    for produccion in gramatica:
        no_terminal, cuerpo = produccion.split("->")
        no_terminal = no_terminal.strip()
        cuerpos = [p.strip() for p in cuerpo.split('|')]

        for c in cuerpos:
            if len(c) == 1 and c.isupper():
                if no_terminal not in unarias:
                    unarias[no_terminal] = set()
                unarias[no_terminal].add(c)
            else:
                nuevas_producciones.append(f"{no_terminal} -> {c}")

    # Expandir las producciones unarias
    for no_terminal, derivados in unarias.items():
        nuevas_cuerpos = set()
        for derivado in derivados:
            for produccion in nuevas_producciones:
                prod_no_terminal, prod_cuerpo = produccion.split("->")
                prod_no_terminal = prod_no_terminal.strip()
                prod_cuerpos = [p.strip() for p in prod_cuerpo.split('|')]

                if prod_no_terminal == derivado:
                    nuevas_cuerpos.update(prod_cuerpos)

        if nuevas_cuerpos:
            nuevas_producciones.append(f"{no_terminal} -> {' | '.join(nuevas_cuerpos)}")

    return nuevas_producciones

# Función principal para ejecutar el programa
def main():
    # Cargar gramáticas desde archivos
    gramatica1 = cargar_gramatica("gramatica1.txt")
    gramatica2 = cargar_gramatica("gramatica2.txt")

    # Validar gramáticas
    if not validar_gramatica(gramatica1):
        print("Gramática 1 contiene errores. La ejecución se detiene.")
        return

    if not validar_gramatica(gramatica2):
        print("Gramática 2 contiene errores. La ejecución se detiene.")
        return

    # Mostrar Gramática 1 original
    print("\nGramática 1 original:")
    for produccion in gramatica1:
        print(produccion)

    # Eliminar producciones-𝜀 de Gramática 1
    print("\nEliminando producciones-𝜀 de Gramática 1...")
    nueva_gramatica1 = eliminar_producciones_epsilon(gramatica1)

    # Eliminar producciones unarias de Gramática 1
    print("\nEliminando producciones unarias de Gramática 1...")
    nueva_gramatica1 = eliminar_producciones_unarias(nueva_gramatica1)

    # Mostrar la gramática resultante sin producciones-𝜀 y sin unarias
    print("\nGramática 1 sin producciones-𝜀 y sin producciones unarias:")
    for produccion in nueva_gramatica1:
        print(produccion)

    # Mostrar Gramática 2 original
    print("\nGramática 2 original:")
    for produccion in gramatica2:
        print(produccion)

    # Eliminar producciones-𝜀 de Gramática 2
    print("\nEliminando producciones-𝜀 de Gramática 2...")
    nueva_gramatica2 = eliminar_producciones_epsilon(gramatica2)

    # Eliminar producciones unarias de Gramática 2
    print("\nEliminando producciones unarias de Gramática 2...")
    nueva_gramatica2 = eliminar_producciones_unarias(nueva_gramatica2)

    # Mostrar la gramática resultante sin producciones-𝜀 y sin unarias
    print("\nGramática 2 sin producciones-𝜀 y sin producciones unarias:")
    for produccion in nueva_gramatica2:
        print(produccion)

if __name__ == "__main__":
    main()
