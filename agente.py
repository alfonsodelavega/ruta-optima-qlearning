#!/ usr/bin/python -tt
# -*- coding: utf-8 -*-
# Ronny Conde at Monkey from the Future

def valor_estado(estado, valores_q):
    """ Devuelve el valor de un estado teniendo en cuenta los valores_q. """
    pass

def print_state_values(states, qvalues):
    """ Calcula e imprime los valores de todos los estados. """
    pass

def qlearning():
    gamma = 0.9
    alpha = 0.01
    N = 20000 # Numero de episodios

    # Inicializamos estados como una lista que almacena cada posible estado. Hay
    # que tener en cuenta que (1, 1) no estara en la lista al ser un obstaculo.
    # E.g. estados se inicializara como [(0, 0), (0, 1), ... ] 
    
    # Inicializamos valores_q como un diccionario:
    #   - claves: tuplas con la combinacion de estados y acciones disponibles
    #   - valores: suma de las recompensas medias que se recibiran hasta el
    #   final del episodio si tras seleccionar accion desde estado se actua de
    #   manera optima, teniendo en cuenta el factor de descuento gamma.
    # Inicialmente todos los valores se inicializaran a 0.0

    # Actualizar valores_q entrenando el agente con qlearning durante N
    # episodios.
    # E.g.
    # for episode in range(N):
    #     s = env.reset()
    #     for _ in range(10000): # Numero limite de pasos por episodio
    #         ...
    #         ...
    #         if done: #End of Episode
    #             ...
    #             break
    #     ...


    # Imprime los valores de los estados (no valores_q)

if __name__ == "__main__":
    qlearning()
