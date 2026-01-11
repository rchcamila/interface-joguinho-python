import tkinter as tk
from tkinter import messagebox
import random
import os

ARQUIVO_PLAYER = "player.txt"

# ---------------- CONFIG ----------------
pontos = 0


# ---------------- FUNÇÕES DOS DESAFIOS ----------------

def soma_dois():
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    tela = nova_janela(f"Quanto é {a} + {b}?")

    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack(pady=10)

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    def verificar():
        global pontos
        try:
            resp = int(entrada.get())
            if resp == a + b:
                pontos += 10
                resultado.config(text="✅ Correto! +10 pontos")
            else:
                resultado.config(text=f"❌ Errado! A resposta era {a+b}")

            atualizar_pontos()
            tela.after(1200, tela.destroy)
        except:
            messagebox.showerror("Erro", "Digite um número")

    tk.Button(tela, text="Confirmar", command=verificar).pack()


def par_ou_impar():
    n = random.randint(1, 100)
    tela = nova_janela(f"O número é {n}. Ele é:")

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    def escolher(valor):
        global pontos
        certo = "par" if n % 2 == 0 else "ímpar"

        if valor == certo:
            pontos += 10
            resultado.config(text="✅ Correto!")
        else:
            resultado.config(text=f"❌ Errado! Era {certo}")

        atualizar_pontos()
        tela.after(1200, tela.destroy)

    tk.Button(tela, text="Par", width=15, command=lambda: escolher("par")).pack(pady=5)
    tk.Button(tela, text="Ímpar", width=15, command=lambda: escolher("ímpar")).pack(pady=5)


def fatorial():
    n = random.randint(1, 7)
    tela = nova_janela(f"Qual é o fatorial de {n}?")

    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack(pady=10)

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    correto = 1
    for i in range(1, n + 1):
        correto *= i

    def verificar():
        global pontos
        try:
            if int(entrada.get()) == correto:
                pontos += 10
                resultado.config(text="✅ Correto!")
            else:
                resultado.config(text=f"❌ Errado! Era {correto}")

            atualizar_pontos()
            tela.after(1200, tela.destroy)
        except:
            messagebox.showerror("Erro", "Digite um número")

    tk.Button(tela, text="Confirmar", command=verificar).pack()


def soma_ate_n():
    n = random.randint(5, 30)
    correto = sum(range(1, n + 1))

    tela = nova_janela(f"Quanto é a soma de 1 até {n}?")

    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack(pady=10)

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    def verificar():
        global pontos
        try:
            if int(entrada.get()) == correto:
                pontos += 10
                resultado.config(text="✅ Correto!")
            else:
                resultado.config(text=f"❌ Errado! Era {correto}")

            atualizar_pontos()
            tela.after(1200, tela.destroy)
        except:
            messagebox.showerror("Erro", "Digite um número")

    tk.Button(tela, text="Confirmar", command=verificar).pack()


def tabuada():
    n = random.randint(2, 10)
    i = random.randint(1, 10)
    correto = n * i

    tela = nova_janela(f"Quanto é {n} x {i}?")

    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack(pady=10)

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    def verificar():
        global pontos
        try:
            if int(entrada.get()) == correto:
                pontos += 10
                resultado.config(text="✅ Correto!")
            else:
                resultado.config(text=f"❌ Errado! Era {correto}")

            atualizar_pontos()
            tela.after(1200, tela.destroy)
        except:
            messagebox.showerror("Erro", "Digite um número")

    tk.Button(tela, text="Confirmar", command=verificar).pack()


def contagem_regressiva():
    inicio = random.randint(10, 30)
    posicao = random.randint(2, 6)
    correto = inicio - (posicao - 1)

    tela = nova_janela(f"Contando de {inicio} para baixo...\nQual é o {posicao}º número?")

    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack(pady=10)

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    def verificar():
        global pontos
        try:
            if int(entrada.get()) == correto:
                pontos += 10
                resultado.config(text="✅ Correto!")
            else:
                resultado.config(text=f"❌ Errado! Era {correto}")

            atualizar_pontos()
            tela.after(1200, tela.destroy)
        except:
            messagebox.showerror("Erro", "Digite um número")

    tk.Button(tela, text="Confirmar", command=verificar).pack()


def soma_varios():
    numeros = [random.randint(1, 10) for _ in range(4)]
    correto = sum(numeros)

    tela = nova_janela(f"Soma estes números: {numeros}")

    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack(pady=10)

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    def verificar():
        global pontos
        try:
            if int(entrada.get()) == correto:
                pontos += 10
                resultado.config(text="✅ Correto!")
            else:
                resultado.config(text=f"❌ Errado! Era {correto}")

            atualizar_pontos()
            tela.after(1200, tela.destroy)
        except:
            messagebox.showerror("Erro", "Digite um número")

    tk.Button(tela, text="Confirmar", command=verificar).pack()


def maior_de_tres():
    a, b, c = random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)

    tela = nova_janela(f"Qual é o maior? {a}, {b}, {c}")

    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack(pady=10)

    resultado = tk.Label(tela, text="")
    resultado.pack(pady=10)

    def verificar():
        global pontos
        try:
            resp = int(entrada.get())
            if resp == max(a, b, c):
                pontos += 10
                resultado.config(text="✅ Correto!")
            else:
                resultado.config(text=f"❌ Errado! Era {max(a, b, c)}")

            atualizar_pontos()
            tela.after(1200, tela.destroy)
        except:
            messagebox.showerror("Erro", "Digite um número")

    tk.Button(tela, text="Confirmar", command=verificar).pack()


# ---------------- FUNÇÕES DE INTERFACE ----------------

def salvar_nome(nome):
    with open(ARQUIVO_PLAYER, "w") as f:
        f.write(nome)


def carregar_nome():
    if os.path.exists(ARQUIVO_PLAYER):
        with open(ARQUIVO_PLAYER, "r") as f:
            return f.read().strip()
    return None


def pedir_nome():
    tela = tk.Toplevel(janela)
    tela.geometry("300x200")
    tela.title("Seu nome")

    tk.Label(tela, text="Digite seu nome:", font=("Arial", 12)).pack(pady=10)
    entrada = tk.Entry(tela, font=("Arial", 14))
    entrada.pack()

    def confirmar():
        nome = entrada.get().strip()
        if nome:
            salvar_nome(nome)
            label_nome.config(text=f"Olá, {nome} 👋")
            tela.destroy()

    tk.Button(tela, text="Confirmar", command=confirmar).pack(pady=10)


def nova_janela(titulo):
    tela = tk.Toplevel(janela)
    tela.geometry("350x250")
    tk.Label(tela, text=titulo, font=("Arial", 14)).pack(pady=10)
    return tela


def atualizar_pontos():
    label_pontos.config(text=f"Pontos: {pontos}")


def trocar_jogador():
    global pontos
    resposta = messagebox.askyesno("Trocar jogador", "Deseja sair e entrar com outro jogador?")
    if resposta:
        if os.path.exists(ARQUIVO_PLAYER):
            os.remove(ARQUIVO_PLAYER)

        pontos = 0
        atualizar_pontos()

        label_nome.config(text="")
        pedir_nome()

def sair():
    nome = carregar_nome()
    if not nome:
        nome = "jogador"

    resposta = messagebox.askyesno("Sair", f"Deseja mesmo sair, {nome}?")

    if resposta:
        messagebox.showinfo("Até logo", f"Até logo, {nome}! 👋")
        janela.destroy()



# ---------------- JANELA PRINCIPAL ----------------

janela = tk.Tk()
janela.title("Joguinho Python")
janela.geometry("400x500")

tk.Label(janela, text="🎮 Joguinho Python", font=("Arial", 18)).pack(pady=5)

nome_salvo = carregar_nome()
label_nome = tk.Label(janela, text="", font=("Arial", 12))
label_nome.pack()

if nome_salvo:
    label_nome.config(text=f"Olá, {nome_salvo} 👋")
else:
    janela.after(100, pedir_nome)

label_pontos = tk.Label(janela, text="Pontos: 0", font=("Arial", 12))
label_pontos.pack()

tk.Button(janela, text="➕ Soma", width=20, command=soma_dois).pack(pady=5)
tk.Button(janela, text="🔢 Par ou Ímpar", width=20, command=par_ou_impar).pack(pady=5)
tk.Button(janela, text="🏆 Maior de 3", width=20, command=maior_de_tres).pack(pady=5)
tk.Button(janela, text="🔢 Fatorial", width=20, command=fatorial).pack(pady=5)
tk.Button(janela, text="➕ Soma até N", width=20, command=soma_ate_n).pack(pady=5)
tk.Button(janela, text="✖️ Tabuada", width=20, command=tabuada).pack(pady=5)
tk.Button(janela, text="🔄 Contagem", width=20, command=contagem_regressiva).pack(pady=5)
tk.Button(janela, text="📊 Soma vários", width=20, command=soma_varios).pack(pady=5)

tk.Button(janela, text="🔄 Trocar jogador", width=20, command=trocar_jogador).pack(pady=5)


tk.Button(janela, text="Sair", command=sair).pack(pady=20)


janela.mainloop()
