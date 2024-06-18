import tkinter as tk
from tkinter import messagebox
import sqlite3

def ler_dados():
    conn = sqlite3.connect('dados.db')
    cursor = conn.execute("SELECT id, nome, idade FROM usuarios")
    dados = cursor.fetchall()
    conn.close()
    return dados

def mostrar_dados():
    dados = ler_dados()
    if dados:
        for row in dados:
            text_box.insert(tk.END, f"ID: {row[0]}, Nome: {row[1]}, Idade: {row[2]}\n")

def arthur():
    sql = "INSERT INTO usuarios (id, nome, idade) VALUES (5, 'Arthur', 18)"
    conn = sqlite3.connect('dados.db')
    conn.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo("Informação", "Usuário Arthur inserido com sucesso!")

def limpar():
    text_box.delete('1.0', tk.END)

root = tk.Tk()
root.title("Leitor de Dados")

label = tk.Label(root, text="Dados dos Usuários")
label.pack()

text_box = tk.Text(root, height=10, width=50)
text_box.pack()

btn_mostrar = tk.Button(root, text="Mostrar Dados", command=mostrar_dados)
btn_mostrar.pack()

btn_limpar = tk.Button(root, text="Limpar", command=limpar)
btn_limpar.pack()

btn_novo = tk.Button(root, text="Inserir Arthur", command=arthur)
btn_novo.pack()

root.mainloop()