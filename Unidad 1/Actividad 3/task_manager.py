# filepath: /home/sanmiguel/code/programacion-multiparadigma-2025/Unidad 1/Actividad 3/task_manager_gui.py

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class TaskManagerGUI:
    def __init__(self):
        self.tasks = []
        self.root = tk.Tk()
        self.root.title("Gestor de Tareas Personales")
        self.root.geometry("900x700")
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Title
        title_label = ttk.Label(main_frame, text="Gestor de Tareas Personales", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Task input frame
        input_frame = ttk.LabelFrame(main_frame, text="Agregar Nueva Tarea", padding="10")
        input_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        
        self.task_entry = ttk.Entry(input_frame, width=60, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=(0, 10))
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        add_button = ttk.Button(input_frame, text="Agregar Tarea", command=self.add_task)
        add_button.grid(row=0, column=1)
        
        # Task list frame
        list_frame = ttk.LabelFrame(main_frame, text="Lista de Tareas", padding="10")
        list_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(0, 10))
        
        # Treeview for task list
        self.task_tree = ttk.Treeview(list_frame, columns=("Status",), show="tree headings", height=15)
        self.task_tree.heading("#0", text="Tarea")
        self.task_tree.heading("Status", text="Estado")
        self.task_tree.column("#0", width=600)
        self.task_tree.column("Status", width=150)
        
        # Configure row height and font
        style = ttk.Style()
        style.configure("Treeview", rowheight=30, font=("Arial", 11))
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.task_tree.yview)
        self.task_tree.configure(yscrollcommand=scrollbar.set)
        
        self.task_tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        
        complete_button = ttk.Button(button_frame, text="Marcar Completada", 
                                   command=self.complete_task)
        complete_button.grid(row=0, column=0, padx=(0, 10))
        
        delete_button = ttk.Button(button_frame, text="Eliminar Tarea", 
                                 command=self.delete_task)
        delete_button.grid(row=0, column=1, padx=(0, 10))
        
        refresh_button = ttk.Button(button_frame, text="Actualizar Lista", 
                                  command=self.refresh_task_list)
        refresh_button.grid(row=0, column=2)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
    
    def add_task(self):
        description = self.task_entry.get().strip()
        if not description:
            messagebox.showwarning("Advertencia", "La descripcion de la tarea no puede estar vacia.")
            return
        
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.task_entry.delete(0, tk.END)
        self.refresh_task_list()
        messagebox.showinfo("Exito", f"Tarea agregada: {description}")
    
    def refresh_task_list(self):
        # Clear existing items
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        
        # Add tasks to treeview
        for task in self.tasks:
            status = "Completada" if task['completed'] else "Pendiente"
            tags = ("completed",) if task['completed'] else ("pending",)
            self.task_tree.insert("", "end", text=task['description'], 
                                 values=(status,), tags=tags)
        
        # Configure tags for styling
        self.task_tree.tag_configure("completed", foreground="gray")
        self.task_tree.tag_configure("pending", foreground="black")
    
    def get_selected_task(self):
        selection = self.task_tree.selection()
        if not selection:
            return None
        
        item = selection[0]
        task_description = self.task_tree.item(item, "text")
        
        # Find task by description
        for task in self.tasks:
            if task['description'] == task_description:
                return task
        return None
    
    def complete_task(self):
        task = self.get_selected_task()
        if not task:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea de la lista.")
            return
        
        if task['completed']:
            messagebox.showinfo("Informacion", "La tarea ya estaba completada.")
        else:
            task['completed'] = True
            self.refresh_task_list()
            messagebox.showinfo("Exito", f"Tarea marcada como completada: {task['description']}")
    
    def delete_task(self):
        task = self.get_selected_task()
        if not task:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea de la lista.")
            return
        
        result = messagebox.askyesno("Confirmar", 
                                   f"¿Esta seguro de que desea eliminar la tarea: {task['description']}?")
        if result:
            self.tasks.remove(task)
            # Update IDs
            for i, t in enumerate(self.tasks):
                t['id'] = i + 1
            self.refresh_task_list()
            messagebox.showinfo("Exito", f"Tarea eliminada: {task['description']}")
    
    def run(self):
        self.root.mainloop()

def main():
    app = TaskManagerGUI()
    app.run()

if __name__ == "__main__":
    main()