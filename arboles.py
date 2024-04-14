class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        inorden(nodo.derecha)

def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izquierda)
        postorden(nodo.derecha)
        print(nodo.valor, end=" ")

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

# Ejemplo de uso:
# Creamos un árbol
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

print("Recorrido Inorden:")
inorden(raiz)
print("\nRecorrido Postorden:")
postorden(raiz)
print("\nRecorrido Preorden:")
preorden(raiz)