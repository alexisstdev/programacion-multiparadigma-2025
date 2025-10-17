class Tarea:
    def __init__(self, titulo, descripcion):
        self._titulo = titulo
        self._descripcion = descripcion
        self._completada = False

    @property
    def titulo(self):
        return self._titulo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def completada(self):
        return self._completada

    def marcar_completada(self):
        self._completada = True

    def mostrar_info(self):
        estado = "✓" if self._completada else "✗"
        return f"[{estado}] {self._titulo}: {self._descripcion}"

    def to_dict(self):
        return {
            "tipo": "normal",
            "titulo": self._titulo,
            "descripcion": self._descripcion,
            "completada": self._completada
        }

    @staticmethod
    def from_dict(data):
        tipo = data.get("tipo", "normal")
        if tipo == "urgente":
            tarea = TareaUrgente(data["titulo"], data["descripcion"], data["nivel"])
        elif tipo == "recurrente":
            tarea = TareaRecurrente(data["titulo"], data["descripcion"], data["frecuencia"])
        else:
            tarea = Tarea(data["titulo"], data["descripcion"])
        
        if data["completada"]:
            tarea.marcar_completada()
        return tarea


class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion, nivel=1):
        super().__init__(titulo, descripcion)
        self._nivel = nivel

    @property
    def nivel(self):
        return self._nivel

    def mostrar_info(self):
        estado = "✓" if self._completada else "✗"
        return f"[{estado}] URGENTE (Nivel {self._nivel}) - {self._titulo}: {self._descripcion}"

    def to_dict(self):
        d = super().to_dict()
        d["tipo"] = "urgente"
        d["nivel"] = self._nivel
        return d


class TareaRecurrente(Tarea):
    def __init__(self, titulo, descripcion, frecuencia="semanal"):
        super().__init__(titulo, descripcion)
        self._frecuencia = frecuencia

    @property
    def frecuencia(self):
        return self._frecuencia

    def mostrar_info(self):
        estado = "✓" if self._completada else "✗"
        return f"[{estado}] RECURRENTE ({self._frecuencia}) - {self._titulo}: {self._descripcion}"

    def to_dict(self):
        d = super().to_dict()
        d["tipo"] = "recurrente"
        d["frecuencia"] = self._frecuencia
        return d