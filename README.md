# Guardians-of-the-Ancient-Kingdom
Proyecto integrador desarrollado para la asignatura de **Programación Orientada a Objetos (POO)**. Consiste en un sistema de combate por turnos en Python que enfrenta a diferentes órdenes de guardianes (Guerreros, Magos y Arqueros) aplicando los pilares fundamentales de la POO.

---

##  1. Estructura del Repositorio

El proyecto está organizado en tres archivos principales para separar la lógica del sistema, su ejecución y su documentación:

- **`personajes.py`**: Contiene la definición de la clase abstracta `Personaje`, sus subclases (`Guerrero`, `Mago`, `Arquero`) con sus lógicas de daño personalizadas, y la clase `Combate` para administrar los turnos y las reglas de enfrentamiento.
- **`main.py`**: Archivo dedicado a la ejecución del programa, la creación de instancias y la verificación de los casos de prueba obligatorios y manejo de excepciones.
- **`LÉAME.md`** (este archivo): Documentación técnica del proyecto, explicación de clases, relaciones, conceptos de POO y evidencia de los retos adicionales.

---

##  2. Responsabilidad de las Clases

- **`Personaje` (Clase Abstracta):** Centraliza los atributos comunes (`nombre`, `vida`, `ataque`, `defensa`) protegidos mediante propiedades (`@property`) y validaciones estrictas. Define el contrato mediante `@abstractmethod def atacar()`.
- **`Guerrero`:** Hereda de `Personaje`. Implementa el *Golpe poderoso*, aumentando su ataque un 20% antes de calcular el daño contra la defensa del rival.
- **`Mago`:** Hereda de `Personaje`. Implementa el *Hechizo penetrante*, ignorando por completo la defensa del objetivo.
- **`Arquero`:** Hereda de `Personaje`. Implementa el *Disparo crítico*, duplicando el daño base si su ataque supera la defensa enemiga.
- **`Combate`:** Administra de manera independiente los turnos entre dos participantes, controla las rondas máximas (50) y verifica las condiciones de victoria o empate de forma polimórfica.

---

##  3. Relaciones entre Clases

- **Herencia:** `Guerrero`, `Mago` y `Arquero` heredan de la clase base `Personaje`, reutilizando atributos y validaciones comunes.
- **Asociación:** Se manifiesta cuando un personaje interactúa directamente con otro al invocar el método de ataque y recibir daño.
- **Agregación:** La clase `Combate` administra y contiene a dos participantes (`Personaje`), los cuales fueron creados de forma independiente fuera del contexto del combate.

---

##  4. Aplicación de los Conceptos de POO

- **Abstracción:** Se utiliza la clase `Personaje` con el módulo `abc` para definir un comportamiento común y obligar a las clases hijas a implementar su propia versión del método `atacar()`.
- **Herencia:** Permite extender la clase base hacia las tres órdenes de guardianes sin duplicar código de atributos ni validaciones de encapsulamiento.
- **Polimorfismo:** La clase `Combate` ejecuta el método `atacar()` sobre cualquier personaje de manera uniforme, sin necesidad de preguntar explícitamente a qué subclase pertenece.
- **Encapsulamiento:** Los atributos se protegen con guion bajo (`_nombre`, `_vida`, etc.) y se exponen mediante getters y setters con validaciones estrictas (evitando nombres vacíos, vidas fuera del rango 0-100 o valores negativos).

---

##  5. Casos de Prueba Implementados

El archivo `main.py` comprueba automáticamente:
1. Creación correcta de los tres tipos de personajes.
2. Rechazo de valores de vida inválidos (mayores a 100 o negativos).
3. Rechazo de nombres vacíos o espacios en blanco.
4. Rechazo de atributos de ataque o defensa inválidos.
5. Ejecución exitosa de un combate por turnos completo.

---

##  6. Instrucciones de Ejecución

1. Asegúrate de tener instalado **Python 3.x** en tu equipo.
2. Clona este repositorio o descarga los archivos en una misma carpeta:
   - `personajes.py`
   - `main.py`
3. Abre tu terminal o entorno de desarrollo (como VS Code) en la carpeta del proyecto y ejecuta:
   ```bash
   python main.py
