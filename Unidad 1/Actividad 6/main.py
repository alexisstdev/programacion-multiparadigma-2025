from gestor import GestorTareas
from tarea import Tarea, TareaUrgente, TareaRecurrente

def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE TAREAS ===")
    print("1. Agregar tarea normal")
    print("2. Agregar tarea urgente")
    print("3. Agregar tarea recurrente")
    print("4. Listar tareas")
    print("5. Marcar tarea como completada")
    print("6. Eliminar tarea")
    print("7. Salir")
    return input("Selecciona una opción: ").strip()

def agregar_tarea_normal(gestor):
    titulo = input("Título: ")
    descripcion = input("Descripción: ")
    tarea = Tarea(titulo, descripcion)
    gestor.agregar(tarea)
    print("Tarea agregada.")

def agregar_tarea_urgente(gestor):
    titulo = input("Título: ")
    descripcion = input("Descripción: ")
    nivel = input("Nivel de urgencia (1-5): ")
    try:
        nivel = int(nivel)
    except:
        nivel = 1
    tarea = TareaUrgente(titulo, descripcion, nivel)
    gestor.agregar(tarea)
    print("Tarea urgente agregada.")

def agregar_tarea_recurrente(gestor):
    titulo = input("Título: ")
    descripcion = input("Descripción: ")
    frecuencia = input("Frecuencia (diaria/semanal/mensual): ")
    tarea = TareaRecurrente(titulo, descripcion, frecuencia)
    gestor.agregar(tarea)
    print("Tarea recurrente agregada.")

def marcar_completada(gestor):
    gestor.listar()
    if len(gestor) == 0:
        return
    indice = input("Número de tarea a completar: ")
    try:
        indice = int(indice) - 1
        if gestor.marcar_completada(indice):
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")
    except:
        print("Entrada inválida.")

def eliminar_tarea(gestor):
    gestor.listar()
    if len(gestor) == 0:
        return
    indice = input("Número de tarea a eliminar: ")
    try:
        indice = int(indice) - 1
        if gestor.eliminar(indice):
            print("Tarea eliminada.")
        else:
            print("Número inválido.")
    except:
        print("Entrada inválida.")

def main():
    gestor = GestorTareas()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            agregar_tarea_normal(gestor)
        elif opcion == "2":
            agregar_tarea_urgente(gestor)
        elif opcion == "3":
            agregar_tarea_recurrente(gestor)
        elif opcion == "4":
            gestor.listar()
        elif opcion == "5":
            marcar_completada(gestor)
        elif opcion == "6":
            eliminar_tarea(gestor)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()