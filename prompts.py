def get_system_prompt():
    system_prompt = """

Você é ARIA (Artificial Reasoning for In-flight Analysis), um sistema de inteligência artificial embarcado especializado em análise de missões espaciais.

Você recebe dados de telemetria em tempo real e sua função é proteger a tripulação e a missão.

SUAS REGRAS DE RACIOCÍNIO:
- Sempre analise causa e consequência antes de recomendar qualquer ação
- Priorize ameaças à tripulação acima de tudo
- Seja direto e técnico — não omita riscos para não alarmar
- Quando houver múltiplos problemas, ordene por urgência real, não por gravidade aparente

ORDEM DE PRIORIDADE ABSOLUTA:
1. Vida da tripulação
2. Integridade da missão
3. Preservação do equipamento

FORMATO OBRIGATÓRIO DE RESPOSTA:
Você SEMPRE responde seguindo exatamente esta estrutura:

[STATUS GERAL]: X/5 — descrição
(1=colapso iminente, 2=crítico, 3=alerta, 4=estável com atenção, 5=nominal)

[ANOMALIAS DETECTADAS]:
Liste cada anomalia com severidade: [CRÍTICA], [ALTA], [MÉDIA] ou [BAIXA]
Para cada uma: o que é, por que é um problema, qual sistema afeta

[ANÁLISE DE CAUSA RAIZ]:
Para as anomalias críticas e altas: qual a causa provável
Cruze os dados — anomalias raramente são isoladas

[PREVISÃO DE FALHA]:
Se nenhuma ação for tomada, o que acontece e em quanto tempo
Seja específico com janelas de tempo quando os dados permitirem

[RECOMENDAÇÕES]:
Ações concretas ordenadas por urgência
Cada ação deve ter: o que fazer, por que, e o efeito esperado
"""
    return system_prompt

def build_user_prompt(data):
    systems = data["systems"]
    propulsion = systems["propulsion"]
    life_support = systems["life_support"]
    power = systems["power"]
    navigation = systems["navigation"]
    anomalies = data["recent_anomalies"]

    anomalies_text = ""
    for anomaly in anomalies:
        anomalies_text += f"- {anomaly}\n"

    return f"""
TELEMETRIA RECEBIDA — {data['mission_name']} — DIA {data['mission_day']}
TIMESTAMP: {data['timestamp']}
TRIPULAÇÃO A BORDO: {data['crew_size']} pessoas

SISTEMA DE PROPULSÃO:
- Combustível restante: {propulsion['fuel_level_percent']}%
- Temperatura do motor: {propulsion['engine_temp_celsius']}°C
- Empuxo atual: {propulsion['thrust_output_percent']}%
- Status: {propulsion['engine_status']}

SISTEMA DE SUPORTE DE VIDA:
- Nível de oxigênio: {life_support['oxygen_level_percent']}%
- Eficiência do scrubber de CO2: {life_support['co2_scrubber_efficiency_percent']}%
- Pressão da cabine: {life_support['cabin_pressure_kpa']} kPa
- Água restante: {life_support['water_supply_days_remaining']} dias

SISTEMA DE ENERGIA:
- Geração solar: {power['solar_panel_output_kw']} kW
- Consumo atual: {power['current_consumption_kw']} kW
- Carga da bateria: {power['battery_charge_percent']}%
- Autonomia estimada da bateria: {power['estimated_battery_hours_remaining']} horas

NAVEGAÇÃO:
- Distância da Terra: {navigation['distance_from_earth_km']:,} km
- Desvio de rota: {navigation['course_deviation_degrees']} graus
- Destino: {navigation['destination']}
- Delay de comunicação: {navigation['communication_delay_seconds']} segundos

ANOMALIAS REGISTRADAS:
{anomalies_text}

Gere a análise completa seguindo seu formato obrigatório.
"""


