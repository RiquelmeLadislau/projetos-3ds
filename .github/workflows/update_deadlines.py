import datetime
import re

# Configuração das Deadlines (Ano, Mês, Dia)
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

# Lendo o README
with open("README.md", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Atualizando cada tag
for tag, data in deadlines.items():
    texto_novo = calcular_restante(data)
    padrao = f".*?"
    substituicao = f"{texto_novo} "
    conteudo = re.sub(padrao, substituicao, conteudo)

# Salvando o arquivo
with open("README.md", "w", encoding="utf-8") as f:
    f.write(conteudo)
