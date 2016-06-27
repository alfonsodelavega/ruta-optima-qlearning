#!/ usr/bin/python -tt
# -*- coding: utf-8 -*-
# Ronny Conde at Monkey from the Future

def acciones_disponibles(estado):
    """ Devuelve una lista con las posibles acciones que el agente puede
    seleccionar desde estado.
    
    E.g. acciones_disponibles((0,0)) devolvera ['W', 'N', 'E', 'S'];
    acciones_disponibles((1,3)) devolvera ['EXIT']
    """
    pass

def recompensa(estado, accion):
    """ Devuelve la recompensa que se recibira al abandonar estado tras
    seleccionar accion.
    
    E.g. recompensa((0,0), 'E') devolvera 0.0; recompensa((0,3), 'EXIT')
    devolvera 1.0
    """
    pass

def reset():
    """ Resetea el entorno, devolviendo el estado inicial.
    
    E.g. reset() puede devolver (0, 0) o (2, 0) o (2, 1), ...
    """
    pass

def paso(estado, accion):
    """ El entorno recibe la accion seleccionada por el agente desde estado y le
    devuelve una tupla con:
        - el nuevo estado
        - la recompensa (funcion del estado de partida y la accion elegida)
        - una variable que indica si ha terminado el episodio (True / False).
    
    E.g. paso((0, 0), 'E') puede devolver ((0, 1), 0.0, False)
    o ((0, 0), 0.0, False) o ((1, 0), 0.0, False)
    """
    pass

def desplazamiento(accion):
    """ Devuelve un posible desplazamiento tras seleccionar accion (en esta
    funcion no puede ser 'EXIT'). El desplazamiento coincidira con accion el 80%
    de las veces, se desviara a la derecha, respecto a la orientación de la
    acción, un 10% y a la izquierda otro 10%.
    
    E.g. desplazamiento('W') devolvera 'W' el 80% de las veces, 'N' el 10% de
    las veces y 'S' el 10% restante.
    """
    pass

def siguiente_estado(estado, accion):
    """ Devuelve la celda en la que acabara el agente tras elegir accion desde
    estado. La componente estocastica se tendra en cuenta llamando a la funcion
    desplazamiento(accion). Hay que tener en cuenta el comportamiento ante los
    obstaculos y limites del laberinto.
    
    E.g. siguiente_estado((0, 1), 'E') puede devolver (0, 2) o (0, 1)
    """
    pass
