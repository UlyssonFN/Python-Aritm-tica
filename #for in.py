import tkinter as tk
from tkinter import ttk, messagebox

class Avaliacao:
    def __init__(self, setor, nota, anonimo, colaborador):
        self.setor = setor
        self.nota = nota
        self.anonimo = anonimo
        self.colaborador = "Anônimo" if anonimo else colaborador

    def __str__(self):
        return f"Setor: {self.setor} | Nota: {self.nota}/5 | Colaborador: {self.colaborador}"


class TotemAvaliacaoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Totem de Avaliação")

        self.avaliacoes = []

        # Dropdown de setores
        self.setores = ["RH", "T.I", "Refeitório", "SESMT"]
        ttk.Label(root, text="Selecione o setor:").pack()
        self.combo_setor = ttk.Combobox(root, values=self.setores)
        self.combo_setor.current(0)
        self.combo_setor.pack(pady=5)

        # Slider de nota
        ttk.Label(root, text="Nota:").pack()
        self.slider_nota = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL)
        self.slider_nota.set(3)
        self.slider_nota.pack(pady=5)

        # Checkbox de anonimato
        self.anonimo_var = tk.BooleanVar()
        self.check_anonimo = tk.Checkbutton(root, text="Enviar como anônimo", variable=self.anonimo_var, command=self.toggle_nome_entry)
        self.check_anonimo.select()
        self.check_anonimo.pack()

        # Campo de nome
        self.nome_label = ttk.Label(root, text="Seu nome:")
        self.nome_label.pack()
        self.entry_nome = ttk.Entry(root)
        self.entry_nome.pack(pady=5)
        self.entry_nome.configure(state="disabled")

        # Botão de enviar
        self.botao_enviar = ttk.Button(root, text="Enviar Avaliação", command=self.enviar_avaliacao)
        self.botao_enviar.pack(pady=10)

        # Lista de avaliações
        self.lista_resultados = tk.Text(root, height=10, width=60, state="disabled")
        self.lista_resultados.pack(pady=10)

    def toggle_nome_entry(self):
        if self.anonimo_var.get():
            self.entry_nome.configure(state="disabled")
        else:
            self.entry_nome.configure(state="normal")

    def enviar_avaliacao(self):
        setor = self.combo_setor.get()
        nota = self.slider_nota.get()
        anonimo = self.anonimo_var.get()
        nome = self.entry_nome.get()

        if not anonimo and not nome:
            messagebox.showwarning("Atenção", "Por favor, informe o nome ou selecione envio anônimo.")
            return

        avaliacao = Avaliacao(setor, nota, anonimo, nome)
        self.avaliacoes.append(avaliacao)

        self.atualizar_resultado()
        messagebox.showinfo("Sucesso", "Avaliação registrada com sucesso!")

    def atualizar_resultado(self):
        self.lista_resultados.configure(state="normal")
        self.lista_resultados.delete(1.0, tk.END)
        for av in self.avaliacoes:
            self.lista_resultados.insert(tk.END, str(av) + "\n")
        self.lista_resultados.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = TotemAvaliacaoApp(root)
    root.mainloop()