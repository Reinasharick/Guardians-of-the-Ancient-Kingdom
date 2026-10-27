from personajes import Guerrero, Mago, Arquero, Combate

def ejecutar_pruebas():
    print("=== EJECUTANDO CASOS DE PRUEBA OBLIGATORIOS ===")
    
    # 1. Creación correcta de personajes
    try:
        arthas = Guerrero("Arthas", 100, 30, 20)
        gandalf = Mago("Gandalf", 80, 40, 10)
        legolas = Arquero("Legolas", 90, 35, 15)
        print(" 1. Personajes creados correctamente.")
    except Exception as e:
        print(f" Error en creación: {e}")

    # 2. Rechazo de vida superior a 100 o negativa
    try:
        bad_char = Guerrero("FalloVida", 150, 20, 10)
    except ValueError as e:
        print(f" 2. Validación de vida superior a 100 exitosa: {e}")

    # 3. Rechazo de nombres vacíos
    try:
        bad_name = Mago("   ", 80, 30, 10)
    except ValueError as e:
        print(f" 3. Validación de nombre vacío exitosa: {e}")

    # 4. Rechazo de ataques inválidos
    try:
        bad_atk = Arquero("FalloAtk", 80, -5, 10)
    except ValueError as e:
        print(f" 4. Validación de ataque inválido exitosa: {e}")

    print("\n=== SIMULACIÓN DE COMBATE (Ejemplo del enunciado) ===")
    g1 = Guerrero("Arthas", 100, 30, 20)
    g2 = Mago("Gandalf", 80, 40, 10)
    
    combate = Combate(g1, g2)
    combate.iniciar()

if __name__ == "__main__":
    ejecutar_pruebas()
