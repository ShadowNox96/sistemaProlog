from pyswip import Prolog, Variable, Query, call, Functor, registerForeign

# clase principal


def main():
    x = 1
    # Menu
    while x != 0:
        print('---------Ingrese la opcion que desee:--------------')
        print('Consulta = 1')
        print('Salir = 0 ')
        entrada = int(input())
        if(entrada == 1):
            consultaProlog()
        else:
            x = 0
            print('Adios')
            break

# Clase que realiza la consulta


def consultaProlog():
    relacion = '0'
    nombre1 = '0'
    nombre2 = '0'
    prolog = Prolog()
    prolog.consult("Parientes.pl")
    result = []

    # Solicito la entrada
    print('Ingrese la pregunta:')
    pregunta = input()

    y = pregunta.split(' ')

    p = 0
    while p != len(y):

        if relacion == '0':
            relacion = relaciones(y[p])

        if nombre1 == '0':
            nombre1 = nombres(y[p])

        if nombre2 == '0':
            nombre2 = nombres(y[p])

        p = p+1

    rel = Functor(""+relacion+"", 2)

    X = Variable()

    q = Query(rel(""+nombre1+"", X))
    print('')
    print('')
    while q.nextSolution():
        print("LA RESPUESTA ES: ", X.value)

    q.closeQuery()


# Diccionario de relaciones
def relaciones(x):
    rel = ['progenitor', 'descendiente', 'hombre', 'mujer',
           'hermana', 'nieto', 'tio', 'hijo', 'mama', 'esposo', 'papa']

    if x in rel:
        return x
    else:
        return '0'

# Diccionario de nombres


def nombres(x):
    nom = ['pedro', 'teresa', 'maria', 'elena', 'jorge', 'raquel', 'miguel']

    if x in nom:
        return x
    else:
        return '0'


if __name__ == '__main__':
    main()
