import tkinter as tk
from tkinter import messagebox
from datetime import datetime


#1021 Admin, clave: 1031
#1022 vendendor clave: 2020
#1023 operario clave: 123456



lista_usuarios = [
    {"Usuario": "1021", "Clave": "1031", "Rol": "admin"},
    {"Usuario": "1022", "Clave": "2020", "Rol": "vendedor"},
    {"Usuario": "1023", "Clave": "123456", "Rol": "Operario"},
]


class SistemaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de sesión")
        self.master.geometry("300x250")
        self.master.configure(bg="#f0f0f0")
        self.master.resizable(False, False)
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.historial = []
        self.crear_login()

    def crear_login(self):
        """Interfaz de inicio de sesión"""
        self.limpiar_ventana()
        tk.Label(self.master, text="Inicio de sesión", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

        tk.Label(self.master, text="Usuario", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.usuario_entry = tk.Entry(self.master, font=("Arial", 12))
        self.usuario_entry.pack(pady=5)

        tk.Label(self.master, text="Clave", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.clave_entry = tk.Entry(self.master, font=("Arial", 12), show="*")
        self.clave_entry.pack(pady=5)

        tk.Button(
            self.master, text="Iniciar sesión", font=("Arial", 12), bg="#d1e7dd",
            command=self.verificar_login
        ).pack(pady=10)

    def verificar_login(self):
        """Verifica el inicio de sesión y redirige según el rol"""
        usuario = self.usuario_entry.get()
        clave = self.clave_entry.get()

        try:
            if not usuario or not clave:
                raise ValueError("Debe llenar todos los campos")

            usuario_encontrado = None
            for u in lista_usuarios:
                if u["Usuario"] == usuario:
                    usuario_encontrado = u
                    break

            if usuario_encontrado is None:
                raise LookupError("Usuario no encontrado")

            if usuario_encontrado["Clave"] != clave:
                raise PermissionError("Clave incorrecta")

            # Login exitoso
            self.registrar_log(usuario, "Inicio exitoso", "OK")
            messagebox.showinfo("Bienvenido", f"Inicio exitoso como {usuario_encontrado['Rol']}")

            if usuario_encontrado["Rol"] == "admin":
                self.ventana_admin()
            elif usuario_encontrado["Rol"] == "vendedor":
                self.ventana_vendedor()
            else:
                self.ventana_operario()

        except ValueError as e:
            self.registrar_log(usuario, str(e), "Error")
            messagebox.showerror("Error", str(e))

        except LookupError as e:
            self.registrar_log(usuario, str(e), "Error")
            messagebox.showerror("Error", str(e))

        except PermissionError as e:
            self.registrar_log(usuario, str(e), "Error")
            messagebox.showerror("Error", str(e))

        except Exception as e:
            self.registrar_log(usuario, f"Error inesperado: {e}", "Error")
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    def registrar_log(self, usuario, mensaje, estado):
        """Guarda el historial de inicio de sesión"""
        hora = datetime.now().strftime("%H:%M:%S")
        log = f"{hora} - {usuario} - {mensaje} - {estado}"
        self.historial.append(log)
        print(log)

    # Interfaces por rol
    def ventana_admin(self):
        self.limpiar_ventana()
        self.master.configure(bg="#000000")
        tk.Label(self.master, text="Bienvenido Administrador", font=("Arial", 16),
                 bg="#000000", fg="#ffffff").pack(pady=10)
        tk.Button(self.master, text="Ver historial", font=("Arial", 12),
                  bg="#ffffff", fg="#000000", command=self.mostrar_log).pack(pady=5)
        tk.Button(self.master, text="Cerrar sesión", font=("Arial", 12),
                  bg="#ffffff", fg="#000000", command=self.crear_login).pack(pady=5)

    def ventana_vendedor(self):
        self.limpiar_ventana()
        self.master.configure(bg="#0066cc")
        tk.Label(self.master, text="Bienvenido Vendedor", font=("Arial", 16),
                 bg="#0066cc", fg="#ffffff").pack(pady=10)
        tk.Button(self.master, text="Cerrar sesión", font=("Arial", 12),
                  bg="#ffffff", fg="#000000", command=self.crear_login).pack(pady=10)

    def ventana_operario(self):
        self.limpiar_ventana()
        self.master.configure(bg="#228B22")
        tk.Label(self.master, text="Bienvenido Operario", font=("Arial", 16),
                 bg="#228B22", fg="#ffffff").pack(pady=10)
        tk.Button(self.master, text="Cerrar sesión", font=("Arial", 12),
                  bg="#ffffff", fg="#000000", command=self.crear_login).pack(pady=10)

    # Historial
    def mostrar_log(self):
        log_window = tk.Toplevel(self.master)
        log_window.title("Historial de inicio de sesión")
        log_window.geometry("400x250")
        log_window.configure(bg="#f0f0f0")
        log_window.resizable(False, False)

        tk.Label(log_window, text="Historial de inicio de sesión", font=("Arial", 14, "bold"),
                 bg="#f0f0f0").pack(pady=10)

        for log in self.historial:
            tk.Label(log_window, text=log, font=("Arial", 10), bg="#f0f0f0").pack(anchor="w")

        tk.Button(log_window, text="Cerrar", command=log_window.destroy,
                  bg="#e57373", fg="white", font=("Arial", 12)).pack(pady=10)

    def limpiar_ventana(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def on_close(self):
        self.master.destroy()


# Ejecucion principal
if __name__ == "__main__": #Profe lo hago asi para que inicie directo sin errores
    root = tk.Tk()
    app = SistemaLogin(root)
    root.mainloop()
