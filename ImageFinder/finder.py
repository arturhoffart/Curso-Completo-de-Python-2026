import os
import hashlib
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from open_nsfw2 import NSFWClassifier

# -------------------------------
# VARIÁVEIS
# -------------------------------
pasta_base = ""
hashes = {}
extensoes_imagem = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")
classificador = NSFWClassifier()

# -------------------------------
# FUNÇÕES LÓGICAS
# -------------------------------
def log(msg):
    caixa_log.insert(tk.END, msg + "\n")
    caixa_log.see(tk.END)

def escolher_pasta():
    global pasta_base
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_base = pasta
        log(f"📂 Pasta selecionada: {pasta_base}")

def gerar_hash(caminho):
    with open(caminho, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def analisar_imagens():
    if not pasta_base:
        messagebox.showwarning("Aviso", "Escolha uma pasta primeiro.")
        return

    hashes.clear()
    total = 0
    log("🔍 Analisando imagens (pasta e subpastas)...")

    for pasta_atual, _, arquivos in os.walk(pasta_base):
        for arquivo in arquivos:
            if arquivo.lower().endswith(extensoes_imagem):
                caminho = os.path.join(pasta_atual, arquivo)
                total += 1
                try:
                    h = gerar_hash(caminho)
                    hashes.setdefault(h, []).append(caminho)
                except Exception as e:
                    log(f"Erro: {e}")

    log(f"📸 Total de imagens analisadas: {total}")

def classificar_imagem(caminho):
    score = classificador.predict(caminho)
    if score <= 0.20:
        return "PG"
    elif score <= 0.40:
        return "PG-13"
    elif score <= 0.60:
        return "R"
    elif score <= 0.80:
        return "X"
    else:
        return "XXX"

def garantir_pastas():
    for cat in ["PG", "PG-13", "R", "X", "XXX"]:
        os.makedirs(os.path.join(pasta_base, cat), exist_ok=True)

def classificar_imagens():
    if not hashes:
        messagebox.showwarning("Aviso", "Faça a análise primeiro.")
        return

    garantir_pastas()
    log("🤖 Classificando imagens...")

    for lista in hashes.values():
        for img in lista:
            try:
                categoria = classificar_imagem(img)
                destino = os.path.join(pasta_base, categoria, os.path.basename(img))
                if not os.path.exists(destino):
                    shutil.copy2(img, destino)
                log(f"{categoria} → {img}")
            except Exception as e:
                log(f"Erro: {e}")

    log("✅ Classificação concluída.")

# -------------------------------
# INTERFACE GRÁFICA
# -------------------------------
janela = tk.Tk()
janela.title("Gerenciador de Imagens com IA")
janela.geometry("800x500")

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="📂 Escolher Pasta", width=20, command=escolher_pasta).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="🔍 Analisar Imagens", width=20, command=analisar_imagens).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="🤖 Classificar Conteúdo", width=20, command=classificar_imagens).grid(row=0, column=2, padx=5)

caixa_log = scrolledtext.ScrolledText(janela, width=95, height=22)
caixa_log.pack(pady=10)

janela.mainloop()
