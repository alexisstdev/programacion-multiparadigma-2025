import json
import os
from tarea import Tarea

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self._tareas = []
        self._archivo = archivo
        self.cargar()

    def agregar(self, tarea):
        self._tareas.append(tarea)
        self.guardar()

    def listar(self):
        if not self._tareas:
            print("No hay tareas registradas.")
            return
        
        print("\n=== LISTA DE TAREAS ===")
        for i, tarea in enumerate(self._tareas, 1):
            print(f"{i}. {tarea.mostrar_info()}")
        print()

    def marcar_completada(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].marcar_completada()
            self.guardar()
            return True
        return False

    def eliminar(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)
            self.guardar()
            return True
        return False

    def guardar(self):
        data = [tarea.to_dict() for tarea in self._tareas]
        with open(self._archivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def cargar(self):
        if os.path.exists(self._archivo):
            try:
                with open(self._archivo, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._tareas = [Tarea.from_dict(d) for d in data]
            except:
                self._tareas = []

    def __len__(self):
        return len(self._tareas)