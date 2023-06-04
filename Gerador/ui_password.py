from passwords import generator
from tkinter import *
from tkinter import ttk

def ui():
    # Cria a instância root
    root = Tk()
    root.title("Password Generator")
    root.geometry("120x100")
    frame = ttk.Frame(root, padding=20)
    # "Transforma" o frame em grid para facilitar alocação
    frame.grid()

    # Cria um label no frame e usa .grid para organizar
    ttk.Label(frame, text=generator()[0]).grid(column=0, row=0)
    ttk.Label(frame, text=generator()[1]).grid(column=0, row=1)
    ttk.Label(frame, text=generator()[2]).grid(column=0, row=2)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=3)

    root.mainloop()

# Garante a inicialização caso este seja o código principal
if(__name__=="__main__"):
    ui()