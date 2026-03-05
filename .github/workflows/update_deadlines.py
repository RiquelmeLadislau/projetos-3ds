import datetime
import re
import os

# Configuração das Deadlines
deadlines = {
    "P1": datetime.datetime(2026, 3, 6, 23, 59),
    "P2": datetime.datetime(2026, 3, 18, 23, 59),
}

def calcular_restante(data_final):
    agora = datetime.datetime.now()
    diff = data_final - agora
    
    if diff.total_seconds() <= 0:
        return "🔴 Prazo Encerrado"
    
    dias = diff.days
    horas = diff.seconds // 3600
    
    if dias > 0:
        return f"⏳ {dias}d {horas}h restantes"
    return f"⚠️ Apenas {horas}h restantes!"

def atualizar_readme():
    if not os.path.exists("README.md"):
        print("Erro: README.md não encontrado.")
        return

    with open("README.md", "r", encoding="utf-8") as f:
        conteudo_original = f.read()

    novo_conteudo = conteudo_original

    for tag, data in deadlines.items():
        texto_dinamico = calcular_restante(data)
        
        # O Regex abaixo busca: QUALQUER_COISA # O '?' torna a busca não-gananciosa (impede que ele apague o arquivo todo)
        padrao = rf".*?"
        substituicao = f"{texto_dinamico} "
        
        # Verifica se a tag existe antes de tentar substituir
        if re.search(padrao, novo_conteudo, flags=re.DOTALL):
            novo_conteudo = re.sub(padrao, substituicao, novo_conteudo, flags=re.DOTALL)
        else:
            print(f"Aviso: Tag {tag} não encontrada no documento.")

    # Só salva se houve alteração real para evitar commits inúteis
    if novo_conteudo != conteudo_original:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(novo_conteudo)
        print("README atualizado com sucesso!")
    else:
        print("Nenhuma alteração necessária.")

if __name__ == "__main__":
    atualizar_readme()
