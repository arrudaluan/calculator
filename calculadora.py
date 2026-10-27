
import tkinter as tk

# Criando a janela
janela = tk.Tk()
janela.title("Minha Calculadora")
janela.geometry("320x430")
janela.resizable(False, False)
janela.configure(bg="#171B25")

# Variáveis
expressao = ""
texto_visor = tk.StringVar(value="0")


# Função para adicionar números e operações
def clicar(valor):
    global expressao

    expressao += str(valor)
    texto_visor.set(expressao)


# Função para limpar o visor
def limpar():
    global expressao

    expressao = ""
    texto_visor.set("0")


# Função para apagar o último caractere
def apagar():
    global expressao

    expressao = expressao[:-1]
    texto_visor.set(expressao if expressao else "0")


# Função para calcular o resultado
def calcular():
    global expressao

    try:
        # Permite somente números e operadores matemáticos
        permitidos = "0123456789+-*/. "

        if not expressao or any(
            caractere not in permitidos
            for caractere in expressao
        ):
            raise ValueError("Expressão inválida")

        resultado = eval(
            expressao,
            {"__builtins__": {}},
            {}
        )

        if not isinstance(resultado, (int, float)):
            raise ValueError("Resultado inválido")

        expressao = str(round(resultado, 10))
        texto_visor.set(expressao)

    except (ValueError, SyntaxError, ZeroDivisionError,
            TypeError, OverflowError, NameError):
        expressao = ""
        texto_visor.set("Erro")


# Criando o visor
visor = tk.Entry(
    janela,
    textvariable=texto_visor,
    font=("Arial", 26),
    bg="#262D3C",
    fg="white",
    justify="right",
    bd=0,
    state="readonly",
    readonlybackground="#262D3C"
)

visor.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=15
)


# Área dos botões
frame = tk.Frame(janela, bg="#171B25")
frame.pack(expand=True, fill="both", padx=10, pady=10)


# Botões da calculadora
botoes = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "00", ""]
]


# Criando os botões
for linha, itens in enumerate(botoes):
    frame.rowconfigure(linha, weight=1)

    for coluna, texto in enumerate(itens):
        frame.columnconfigure(coluna, weight=1)

        if texto == "":
            continue

        if texto == "C":
            comando = limpar
        elif texto == "⌫":
            comando = apagar
        elif texto == "=":
            comando = calcular
        else:
            comando = lambda valor=texto: clicar(valor)

        cor = "#4F8CFF" if texto == "=" else "#30394B"

        botao = tk.Button(
            frame,
            text=texto,
            font=("Arial", 18),
            bg=cor,
            fg="white",
            activebackground="#65748F",
            activeforeground="white",
            bd=0,
            command=comando
        )

        botao.grid(
            row=linha,
            column=coluna,
            padx=4,
            pady=4,
            sticky="nsew"
        )


# Mantém a janela aberta
janela.mainloop()
