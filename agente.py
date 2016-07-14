#!/ usr/bin/python -tt
# -*- coding: utf-8 -*-
# Ronny Conde at Monkey from the Future

def valor_estado(estado, valores_q):
    """ Calculara y devolvera el valor asociado a estado teniendo en cuenta
    valores_q.
    """ 
    pass

def imprimir_valores_estados(estados, valores_q):
    """ imprime por pantalla los valores asociados a cada estado."""
    pass

def qlearning():
    gamma = 0.9
    alpha = 0.01
    N = 20000 # Numero de episodios

    # Inicializamos estados como una lista que almacena cada posible posicion
    # del agente en el laberinto. Hay que tener en cuenta que (1, 1) no estara
    # en la lista al ser un obstaculo.
    # E.g. estados se inicializara como [(0, 0), (0, 1), ... ] 
    pass

    # valores_q sera un diccionario:
    #   - Claves. Tuplas con la combinacion de cada estado y sus acciones disponibles
    #   - Valores: Suma de las recompensas que se esperan recibir hasta el final
    #   del episodio si se actua de manera optima partiendo del estado Q (la
    #   clave asociada) y teniendo en cuenta el factor de descuento gamma.
    # Inicializaremos todos los valores a 0.0
    # E.g. valores_q se inicializara como {((0, 0), 'W'): 0.0, ((0, 0), 'N'):
    # 0.0, ... }
    pass

    # Actualizar valores_q entrenando el agente con qlearning durante N
    # episodios.
    # E.g. A continuacion se muestra una posible estructura
    # for episode in range(N):
    #     s = entorno.reset()
    #     for _ in range(10000): # Numero limite de pasos por episodio
    #         ...
    #         ...
    #         if done: # Fin del Episodio
    #             ...
    #             break
    #     ...
    pass

    # Llamada a imprimir_valores_estados(estados, valores_q).
    pass

if __name__ == "__main__":
    qlearning()
