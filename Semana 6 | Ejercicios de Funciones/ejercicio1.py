# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def suma():
    primer=20
    segundo=10
    print(f"Este es la suma {primer+segundo}")
    texto()


def texto():
    print("y esto es otra funcion")

suma()