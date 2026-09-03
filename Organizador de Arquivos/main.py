import os
import shutil

origem = r"C:\origem\caminho\pasta"

for arquivo in os.listdir(origem):
    caminho_completo = os.path.join(origem, arquivo)

    if os.path.isfile(caminho_completo):
        extensao = os.path.splitext(arquivo)[1].lower().replace(".", "")

        if extensao == "":
            continue

        pasta_destino = os.path.join(origem, extensao)
        os.makedirs(pasta_destino, exist_ok=True)

        shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
        print(f"Movido: {arquivo} -> {pasta_destino}")