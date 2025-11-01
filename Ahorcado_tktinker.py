import tkinter as tk
from tkinter import messagebox

class AhorcadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Ahorcado entre dos jugadores 🎮")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.ahorcado_etapas = [
            "+---+\n    |\n    |\n    |\n=====",
            "+---+\n😢  |\n    |\n    |\n=====",
            "+---+\n😢  |\n |  |\n    |\n=====",
            "+---+\n😢  |\n/|  |\n    |\n=====",
            "+---+\n😢  |\n/|\\ |\n    |\n=====",
            "+---+\n😢  |\n/|\\ |\n/   |\n=====",
            "+---+\n😢  |\n/|\\ |\n/ \\ |\n=====",
        ]

        self.crear_pantalla_inicio()

    def crear_pantalla_inicio(self):
      #  """Pantalla inicial donde el jugador 1 escribe la palabra secreta"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Jugador 1: Escribe la palabra secreta", font=("Arial", 12)).pack(pady=20)
        self.palabra_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.palabra_entry.pack(pady=10)

        tk.Button(self.root, text="Comenzar juego", command=self.iniciar_juego).pack(pady=10)

    def iniciar_juego(self):
        """Configuración inicial del juego"""
        self.palabra_secreta = self.palabra_entry.get().lower()
        if not self.palabra_secreta.isalpha():
            messagebox.showerror("Error", "La palabra debe contener solo letras.")
            return

        self.progreso = ["_"] * len(self.palabra_secreta)
        self.letras_usadas = []
        self.intentos = 6
        self.fallos = 0

        self.crear_pantalla_juego()

    def crear_pantalla_juego(self):
        """Pantalla donde el jugador 2 juega"""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.lbl_ahorcado = tk.Label(self.root, text=self.ahorcado_etapas[0], font=("Courier", 14), justify="left")
        self.lbl_ahorcado.pack(pady=10)

        self.lbl_progreso = tk.Label(self.root, text=" ".join(self.progreso), font=("Arial", 18))
        self.lbl_progreso.pack(pady=10)

        self.lbl_info = tk.Label(self.root, text="Adivina una letra:", font=("Arial", 12))
        self.lbl_info.pack()

        self.letra_entry = tk.Entry(self.root, font=("Arial", 14), width=5, justify="center")
        self.letra_entry.pack(pady=5)

        tk.Button(self.root, text="Probar", command=self.probar_letra).pack(pady=10)
        self.lbl_letras_usadas = tk.Label(self.root, text="Letras usadas: ", font=("Arial", 10))
        self.lbl_letras_usadas.pack(pady=5)

    def probar_letra(self):
        """Lógica para procesar la letra ingresada"""
        letra = self.letra_entry.get().lower()
        self.letra_entry.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Atención", "Introduce una sola letra válida.")
            return

        if letra in self.letras_usadas:
            messagebox.showinfo("Atención", "Esa letra ya la intentaste.")
            return

        self.letras_usadas.append(letra)
        self.lbl_letras_usadas.config(text="Letras usadas: " + ", ".join(self.letras_usadas))

        if letra in self.palabra_secreta:
            for i, l in enumerate(self.palabra_secreta):
                if l == letra:
                    self.progreso[i] = letra
            self.lbl_progreso.config(text=" ".join(self.progreso))
        else:
            self.fallos += 1
            self.intentos -= 1
            self.lbl_ahorcado.config(text=self.ahorcado_etapas[self.fallos])

        self.verificar_estado()

    def verificar_estado(self):
        """Comprueba si el juego terminó"""
        if "_" not in self.progreso:
            messagebox.showinfo("🎉 ¡Ganaste!", f"La palabra era: {self.palabra_secreta}")
            self.reiniciar()
        elif self.intentos == 0:
            messagebox.showerror("💀 Fin del juego", f"Te quedaste sin intentos.\nLa palabra era: {self.palabra_secreta}")
            self.reiniciar()

    def reiniciar(self):
        """Permite volver a empezar"""
        if messagebox.askyesno("Reiniciar", "¿Quieres jugar otra vez?"):
            self.crear_pantalla_inicio()
        else:
            self.root.destroy()

# Ejecutar el juego
if __name__ == "__main__":
    root = tk.Tk()
    app = AhorcadoApp(root)
    root.mainloop()
