# ============================================================
# MISSION CONTROL AI
# ============================================================

nome_missao = "Artemis"
nome_equipe = "Baba yaga"

dados_missao = [
    [20, 72, 67, 69, 81],
    [34, 60, 62, 67, 42],
    [11, 76, 69, 90, 12],
    [23, 34, 30, 56, 11],
    [32, 40, 30, 45, 95],
    [14, 67, 67, 69, 23]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def classificar_ciclo(valor):
    if 0 <= valor <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= valor <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def calcular_risco_ciclo(ciclo):
    status_temp, pontos_temp = analisar_temperatura(ciclo[0])
    status_com,  pontos_com  = analisar_comunicacao(ciclo[1])
    status_bat,  pontos_bat  = analisar_bateria(ciclo[2])
    status_ox,   pontos_ox   = analisar_oxigenio(ciclo[3])
    status_est,  pontos_est  = analisar_estabilidade(ciclo[4])

    total_pontos = pontos_temp + pontos_com + pontos_bat + pontos_ox + pontos_est
    return total_pontos

def analisar_tendencia(riscos):
    if riscos[0] > riscos[-1]:
        return "RISCO DIMINUÍDO, TUDO SOB CONTROLE!"
    elif riscos[0] < riscos[-1]:
        return "AS COISAS ESTÃO PIORANDO, FICA ESPERTO!"
    else:
        return "NADA DE DIFERENTE, TUDO CERTO!"

def identificar_area_mais_afetada(pontos_areas, areas_monitoradas):
    maior = max(pontos_areas)
    indice = pontos_areas.index(maior)
    area = areas_monitoradas[indice]
    return area

def gerar_recomendacao(ciclo):
    recomendacoes = []

    status_temp, _ = analisar_temperatura(ciclo[0])
    if status_temp == "CRÍTICO":
        recomendacoes.append("Verificar controle térmico da missão.")

    status_com, _ = analisar_comunicacao(ciclo[1])
    if status_com == "CRÍTICO":
        recomendacoes.append("Tentar restabelecer contato com a base.")

    status_bat, _ = analisar_bateria(ciclo[2])
    if status_bat == "CRÍTICO":
        recomendacoes.append("Ativar modo de economia de energia.")

    status_ox, _ = analisar_oxigenio(ciclo[3])
    if status_ox == "CRÍTICO":
        recomendacoes.append("Acionar protocolo de suporte à vida.")

    status_est, _ = analisar_estabilidade(ciclo[4])
    if status_est == "CRÍTICO":
        recomendacoes.append("Reduzir operações não essenciais.")

    if len(recomendacoes) == 0:
        return "Manter operação normal e continuar monitoramento."

    return " | ".join(recomendacoes)

def gerar_relatorio_final(riscos_por_ciclo, pontos_por_area):
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Ciclos analisados: {len(dados_missao)}")

    # Médias de cada sensor
    media_temp = sum([c[0] for c in dados_missao]) / len(dados_missao)
    media_com  = sum([c[1] for c in dados_missao]) / len(dados_missao)
    media_bat  = sum([c[2] for c in dados_missao]) / len(dados_missao)
    media_ox   = sum([c[3] for c in dados_missao]) / len(dados_missao)
    media_est  = sum([c[4] for c in dados_missao]) / len(dados_missao)

    print(f"\nMédia de temperatura:  {media_temp:.2f}°C")
    print(f"Média de comunicação:  {media_com:.2f}%")
    print(f"Média de bateria:      {media_bat:.2f}%")
    print(f"Média de oxigênio:     {media_ox:.2f}%")
    print(f"Média de estabilidade: {media_est:.2f}%")

    # Estatísticas dos ciclos
    maior_risco   = max(riscos_por_ciclo)
    ciclo_critico = riscos_por_ciclo.index(maior_risco) + 1
    risco_medio   = sum(riscos_por_ciclo) / len(riscos_por_ciclo)
    qtd_criticos  = sum(1 for r in riscos_por_ciclo if r >= 6)

    print(f"\nCiclo mais crítico: Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Ciclos críticos: {qtd_criticos}")

    # Tendência
    tendencia = analisar_tendencia(riscos_por_ciclo)
    print(f"\nTendência da missão: {tendencia}")

    # Pontuação por área
    print("\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontos_por_area[i]} pontos")

    # Área mais afetada
    area_afetada = identificar_area_mais_afetada(pontos_por_area, areas_monitoradas)
    print(f"\nÁrea mais afetada: {area_afetada}")

    # Classificação final
    classificacao_final = classificar_ciclo(int(risco_medio))
    print(f"\nClassificação final: {classificacao_final}")
    print("=" * 60)


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

riscos_por_ciclo = []
pontos_por_area = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Ciclos analisados: {len(dados_missao)}")
print("=" * 60)

for numero, ciclo in enumerate(dados_missao):

    status_temp, pontos_temp = analisar_temperatura(ciclo[0])
    status_com,  pontos_com  = analisar_comunicacao(ciclo[1])
    status_bat,  pontos_bat  = analisar_bateria(ciclo[2])
    status_ox,   pontos_ox   = analisar_oxigenio(ciclo[3])
    status_est,  pontos_est  = analisar_estabilidade(ciclo[4])

    risco = calcular_risco_ciclo(ciclo)
    classificacao = classificar_ciclo(risco)
    recomendacao = gerar_recomendacao(ciclo)

    riscos_por_ciclo.append(risco)
    pontos_por_area[0] += pontos_temp
    pontos_por_area[1] += pontos_com
    pontos_por_area[2] += pontos_bat
    pontos_por_area[3] += pontos_ox
    pontos_por_area[4] += pontos_est

    print(f"\nCICLO {numero + 1}")
    print("-" * 60)
    print(f"Temperatura:  {ciclo[0]}°C | {status_temp}")
    print(f"Comunicação:  {ciclo[1]}%  | {status_com}")
    print(f"Bateria:      {ciclo[2]}%  | {status_bat}")
    print(f"Oxigênio:     {ciclo[3]}%  | {status_ox}")
    print(f"Estabilidade: {ciclo[4]}%  | {status_est}")
    print(f"Pontuação de risco: {risco}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")

gerar_relatorio_final(riscos_por_ciclo, pontos_por_area)