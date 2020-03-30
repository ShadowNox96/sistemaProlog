
from pyswip import Prolog, Variable, Query, call, Functor, registerForeign
# Primera prueba de funcionamiento
"""
def hello(x):
    print(x)
hello.arity = 1
registerForeign(hello)
prolog = Prolog()
prolog.consult("Parientes.pl")
result = []
x = ''
print(list(prolog.query("progenitor(pedro,X). , hello(X)")))
"""


def main():
    prolog = Prolog()
    prolog.consult("Parientes.pl")
    result = []
    progenitor = Functor("progenitor", 2)

    X = Variable()

    q = Query(progenitor("pedro", X))
    while q.nextSolution():
        print(X.value)
        result.append(X.value)
    q.closeQuery()
    return result


def hola():
    main()


if __name__ == "__main__":
    hola()
