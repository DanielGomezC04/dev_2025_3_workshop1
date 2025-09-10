class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        invertida = []
        for i in range(len(lista) - 1, -1, -1): 
          invertida.append(lista[i])
        return invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for indice, item in enumerate(lista):
            if item == elemento:
                return indice
            else:
                # Do nothing, continue the loop
                pass
        # The 'return -1' is executed only after the loop finishes.
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        lista_sin_duplicados = []
        for elemento in lista:
            if not any(e is elemento or (e == elemento and type(e) == type(elemento)) 
                       for e in lista_sin_duplicados):
                lista_sin_duplicados.append(elemento)
        return lista_sin_duplicados
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        combinada = []
        i = 0  # Índice para lista1
        j = 0  # Índice para lista2

        # Recorrer ambas listas mientras queden elementos en ellas
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                combinada.append(lista1[i])
                i += 1
            else:
                combinada.append(lista2[j])
                j += 1

        # Agregar los elementos restantes de la lista1 (si los hay)
        while i < len(lista1):
            combinada.append(lista1[i])
            i += 1

        # Agregar los elementos restantes de la lista2 (si los hay)
        while j < len(lista2):
            combinada.append(lista2[j])
            j += 1

        return combinada
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
          return []
        k = k % len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        n = len(lista) + 1
    
        suma_total_esperada = n * (n + 1) // 2

        suma_lista_actual = sum(lista)

        numero_faltante = suma_total_esperada - suma_lista_actual
    
        return numero_faltante
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elemento in conjunto1:
          if elemento not in conjunto2:
            return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = []

        def push(elemento):
        
          pila.append(elemento)

        def pop():
           if not is_empty():
              return pila.pop()
           else:
             raise IndexError("pop desde una pila vacía")

        def peek():
           if not is_empty():
             return pila[-1]
           else:
              raise IndexError("peek desde una pila vacía")

        def is_empty():
           return len(pila) == 0
        return {
         "push": push,
         "pop": pop,
         "peek": peek,
         "is_empty": is_empty
        }

    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = []

        def enqueue(elemento):
          cola.append(elemento)

        def dequeue():
          if not cola:
            return None
          return cola.pop(0)

        def peek():
           if not cola:
              return None
           return cola[0]

        def is_empty():
           return len(cola) == 0

        return {
          'enqueue': enqueue,
          'dequeue': dequeue,
          'peek': peek,
          'is_empty': is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        if not matriz:
          return []

        return [list(fila) for fila in zip(*matriz)]