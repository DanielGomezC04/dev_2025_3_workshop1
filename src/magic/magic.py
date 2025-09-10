class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n < 0:
          raise ValueError("n debe ser un número entero no negativo")
        elif n == 0:
          return 0
        elif n == 1:
          return 1
    
        a, b = 0, 1
        for _ in range(2, n + 1):
           a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n < 0:
           raise ValueError("n debe ser un entero no negativo")
        if n == 0:
           return []
        if n == 1:
           return [0]

        secuencia = [0, 1]
        while len(secuencia) < n:
          secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
           return False
        if n <= 3:
           return True
        if n % 2 == 0 or n % 3 == 0:
           return False

        i = 5
        while i * i <= n:
           if n % i == 0 or n % (i + 2) == 0:
             return False
        i += 6
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        if n < 2:
          return []

        primos = []
        for i in range(2, n + 1):
          if self.es_primo(i):
            primos.append(i)
        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n <= 1:
          return False

        suma_divisores = 1  # 1 siempre es divisor (excepto de 0 y 1)
        for i in range(2, int(n ** 0.5) + 1):
           if n % i == 0:
             suma_divisores += i
             if i != n // i:  # evitar sumar el mismo divisor dos veces
                suma_divisores += n // i

        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        if filas <= 0:
          return []

        triangulo = [[1]]
        for i in range(1, filas):
           fila = [1]
           for j in range(1, i):
             fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
           fila.append(1)
           triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n < 0:
          raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(2, n + 1):
          resultado *= i
        return resultado
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        a, b = abs(a), abs(b)  # aseguramos que sean positivos
        while b != 0:
          a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
           return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        n = abs(n)  # por si es negativo
        suma = 0
        while n > 0:
           suma += n % 10   # último dígito
           n //= 10         # quitar último dígito
        return suma
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        digitos = str(n)
        potencia = len(digitos)
        suma = sum(int(d)**potencia for d in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = len(matriz)
    
    # comprobar que es cuadrada
        if any(len(fila) != n for fila in matriz):
          return False
    
    # suma objetivo (primera fila)
        suma_objetivo = sum(matriz[0])
    
    # verificar filas
        for fila in matriz:
          if sum(fila) != suma_objetivo:
            return False
    
    # verificar columnas
        for j in range(n):
           if sum(matriz[i][j] for i in range(n)) != suma_objetivo:
              return False
    
    # diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
          return False
    
    # diagonal secundaria
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_objetivo:
          return False
    
        return True