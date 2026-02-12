import os
import hashlib

# Pergunta ao usuário onde procurar
pasta_base = input("Digite o caminho da pasta onde deseja procurar imagens: ").strip()

# Remove aspas se o usuário colar o caminho com aspas
pasta_base = pasta_base.strip('"').strip("'")

# Verifica se a pasta existe
if not os.path.isdir(pasta_base):
    print("❌ Caminho inválido. Verifique e tente novamente.")
    exit()

extensoes_imagem = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")
hashes = {}

def gerar_hash(caminho_arquivo):
    with open(caminho_arquivo, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

print("\n🔍 Procurando imagens...\n")

for pasta_atual, _, arquivos in os.walk(pasta_base):
    for arquivo in arquivos:
        if arquivo.lower().endswith(extensoes_imagem):
            caminho = os.path.join(pasta_atual, arquivo)

            try:
                hash_img = gerar_hash(caminho)

                if hash_img in hashes:
                    hashes[hash_img].append(caminho)
                else:
                    hashes[hash_img] = [caminho]

            except Exception as erro:
                print(f"Erro ao ler {caminho}: {erro}")

print("\n📸 Imagens duplicadas encontradas:\n")

tem_duplicadas = False

for lista in hashes.values():
    if len(lista) > 1:
        tem_duplicadas = True
        print("Duplicatas:")
        for img in lista:
            print("  ", img)
        print("-" * 40)

if not tem_duplicadas:
    print("Nenhuma imagem duplicada encontrada ✅")
