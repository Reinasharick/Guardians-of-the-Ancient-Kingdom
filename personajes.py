from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    # --- Encapsulamiento y Validaciones ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if not isinstance(valor, (int, float)) or not (0 <= valor <= 100):
            raise ValueError("La vida debe ser un entero entre 0 y 100.")
        self._vida = int(valor)

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El ataque debe ser un entero positivo.")
        self._ataque = int(valor)

    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("La defensa debe ser un entero no negativo.")
        self._defensa = int(valor)

    # --- Métodos Comunes ---
    def recibir_danio(self, cantidad: int) -> int:
        if cantidad < 0:
            cantidad = 0
        danio_efectivo = min(self.vida, cantidad)
        self.vida -= danio_efectivo
        return danio_efectivo

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def mostrar_estado(self) -> str:
        return f"{self.nombre} (Vida: {self.vida} | Ataque: {self.ataque} | Defensa: {self.defensa})"

    @abstractmethod
    def atacar(self, objetivo) -> int:
        pass


class Guerrero(Personaje):
    def atacar(self, objetivo) -> int:
        if not self.esta_vivo():
            raise ValueError(f"{self.nombre} está derrotado y no puede atacar.")
        if not objetivo.esta_vivo():
            raise ValueError(f"El objetivo {objetivo.nombre} ya está derrotado.")
        
        # Golpe poderoso: Aumenta ataque un 20% antes de descontar defensa
        ataque_potenciado = self.ataque * 1.20
        danio_calculado = int(ataque_potenciado - objetivo.defensa)
        danio_final = max(0, danio_calculado)
        return objetivo.recibir_danio(danio_final)


class Mago(Personaje):
    def atacar(self, objetivo) -> int:
        if not self.esta_vivo():
            raise ValueError(f"{self.nombre} está derrotado y no puede atacar.")
        if not objetivo.esta_vivo():
            raise ValueError(f"El objetivo {objetivo.nombre} ya está derrotado.")
        
        # Hechizo penetrante: Ignora completamente la defensa
        danio_final = self.ataque
        return objetivo.recibir_danio(danio_final)


class Arquero(Personaje):
    def atacar(self, objetivo) -> int:
        if not self.esta_vivo():
            raise ValueError(f"{self.nombre} está derrotado y no puede atacar.")
        if not objetivo.esta_vivo():
            raise ValueError(f"El objetivo {objetivo.nombre} ya está derrotado.")
        
        # Disparo crítico: Duplica el daño si el ataque supera la defensa
        if self.ataque > objetivo.defensa:
            danio_base = self.ataque - objetivo.defensa
            danio_final = danio_base * 2
        else:
            danio_final = 0
        return objetivo.recibir_danio(danio_final)


class Combate:
    def __init__(self, personaje1: Personaje, personaje2: Personaje):
        self.p1 = personaje1
        self.p2 = personaje2
        self.turno_actual = 1 # 1 para p1, 2 para p2
        self.ronda = 0

    def cambiar_turno(self):
        self.turno_actual = 2 if self.turno_actual == 1 else 1

    def verificar_ganador(self):
        if not self.p1.esta_vivo() and not self.p2.esta_vivo():
            return "Empate técnico"
        elif not self.p1.esta_vivo():
            return self.p2
        elif not self.p2.esta_vivo():
            return self.p1
        return None

    def iniciar(self):
        print(f"\n--- INICIO DEL COMBATE: {self.p1.nombre} vs {self.p2.nombre} ---")
        print(f"Estado inicial -> {self.p1.mostrar_estado()} | {self.p2.mostrar_estado()}")
        
        while self.p1.esta_vivo() and self.p2.esta_vivo() and self.ronda < 50:
            self.ronda += 1
            print(f"\n--- Ronda {self.ronda} ---")
            
            if self.turno_actual == 1:
                atacante, defensor = self.p1, self.p2
            else:
                atacante, defensor = self.p2, self.p1

            vida_antes = defensor.vida
            danio = atacante.atacar(defensor)
            print(f"Turno de {atacante.nombre} ({type(atacante).__name__}) ataca a {defensor.nombre} causando {danio} de daño.")
            print(f"Estado: {self.p1.nombre} (Vida: {self.p1.vida}) - {self.p2.nombre} (Vida: {self.p2.vida})")
            
            ganador = self.verificar_ganador()
            if ganador:
                break
                
            self.cambiar_turno()

        self.mostrar_resultado()

    def mostrar_resultado(self):
        ganador = self.verificar_ganador()
        print("\n=== RESULTADO FINAL DEL COMBATE ===")
        if isinstance(ganador, Personaje):
            print(f" ¡El vencedor es {ganador.nombre}!")
        else:
            print(" El combate terminó en empate.")
