# 🚀 Mission Control AI

Sistema inteligente de monitoramento de missão espacial desenvolvido em Python.

## 📋 Descrição

O Mission Control AI simula o acompanhamento de uma missão espacial experimental.
O sistema analisa ciclos de monitoramento com dados de temperatura, comunicação,
bateria, oxigênio e estabilidade — gerando alertas automáticos, calculando o risco
de cada ciclo e exibindo um relatório final da operação.

## 👥 Equipe

- **Missão:** Artemis
- **Equipe:** Baba Yaga
- **Integrante:** Enrico Marinho — RM: 569338
		   Fernando Lobato- RM: 569337
		   Manoel Silva —  - RM: 572045

## ⚙️ Como executar

1. Certifique-se de ter o Python instalado
2. Clone o repositório ou baixe o arquivo `mission_control.py`
3. Execute no terminal:

python mission_control.py

## 🚨 Regras de alerta

Cada sensor é classificado em NORMAL, ATENÇÃO ou CRÍTICO:

| Sensor       | ATENÇÃO            | CRÍTICO     |
|-------------|-------------------|---------------|
| Temperatura | < 18°C ou > 30°C  | > 35°C        |
| Comunicação | 30% a 59%         | < 30%         |
| Bateria     | 20% a 49%         | < 20%         |
| Oxigênio    | 80% a 89%         | < 80%         |
| Estabilidade| 40% a 69%         | < 40%         |

## 📁 Estrutura do projeto

mission-control-ai/
├── README.md
└── mission_control.py

## 🤖 Funcionalidades

- Análise automática de 6 ciclos de monitoramento
- Geração de alertas por sensor
- Cálculo de risco por ciclo
- Identificação da área mais afetada
- Análise de tendência da missão
- Relatório final completo no terminal

