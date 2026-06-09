#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

#define CICLOS_DE_SIMULACAO 5
#define CAPACIDADE_MAXIMA_BATERIA 10000.0
#define CONSUMO_BASE 500.0
#define GASTO_RESFRIAMENTO 1200.0
#define GASTO_PROPULSOR 2500.0
#define POTENCIA_SOLAR_MAXIMA 6000.0

int main() {
    int ENERGIA, COMUNICACAO, RESFRIAMENTO, TEMPERATURACRITICA;
    int PROPULSOR1, PROPULSOR2, FECHAMENTODECABINE, PRESSAOOXIGENIO;
    int RESFRIAMENTO_LED, PROPULSOR1_SAIDA, PROPULSOR2_SAIDA, ALERTA_CIRCUITO;

    float bateria_central = 8000.0;
    float orientacao_nave;
    float geracao_solar_watts;
    float consumo_watts;
    int alerta_sustentabilidade;

    srand(time(NULL));

    for (int i = 1; i <= CICLOS_DE_SIMULACAO; i++) {
        ENERGIA = rand() % 2;
        COMUNICACAO = rand() % 2;
        RESFRIAMENTO = rand() % 2;
        TEMPERATURACRITICA = rand() % 2;
        PROPULSOR1 = rand() % 2;
        PROPULSOR2 = rand() % 2;
        FECHAMENTODECABINE = rand() % 2;
        PRESSAOOXIGENIO = rand() % 2;

        orientacao_nave = (rand() % 101) / 100.0;

        RESFRIAMENTO_LED = !RESFRIAMENTO;
        PROPULSOR1_SAIDA = !PROPULSOR1;
        PROPULSOR2_SAIDA = PROPULSOR1 && !PROPULSOR2;

        ALERTA_CIRCUITO = (ENERGIA && COMUNICACAO) ||
                          (RESFRIAMENTO && TEMPERATURACRITICA) ||
                          (PROPULSOR1 && PROPULSOR2) ||
                          (FECHAMENTODECABINE || PRESSAOOXIGENIO);

        geracao_solar_watts = orientacao_nave * POTENCIA_SOLAR_MAXIMA;

        consumo_watts = CONSUMO_BASE;
        if (RESFRIAMENTO_LED) consumo_watts += GASTO_RESFRIAMENTO;
        if (PROPULSOR1_SAIDA) consumo_watts += GASTO_PROPULSOR;
        if (PROPULSOR2_SAIDA) consumo_watts += GASTO_PROPULSOR;

        bateria_central += (geracao_solar_watts - consumo_watts);

        if (bateria_central > CAPACIDADE_MAXIMA_BATERIA) {
            bateria_central = CAPACIDADE_MAXIMA_BATERIA;
        } else if (bateria_central < 0.0) {
            bateria_central = 0.0;
        }

        alerta_sustentabilidade = (consumo_watts > geracao_solar_watts);

        printf("\n====================================================\n");
        printf("       PAINEL DE TELEMETRIA - CICLO %d\n", i);
        printf("====================================================\n");

        printf(" [GESTAO DE ENERGIA RENOVAVEL E SUSTENTAVEL]\n");
        printf(" Alinhamento Solar: %.0f%%\n", orientacao_nave * 100);
        printf(" Geracao Solar: %.2f W\n", geracao_solar_watts);
        printf(" Consumo Total: %.2f W\n", consumo_watts);
        printf(" Carga da Bateria Central: %.2f W/h\n", bateria_central);

        printf("\n [LEITURA DOS SENSORES LOGICOS]\n");
        printf(" Energia: %d             | Comunicacao: %d\n", ENERGIA, COMUNICACAO);
        printf(" Resfriamento: %d        | Temp. Critica: %d\n", RESFRIAMENTO, TEMPERATURACRITICA);
        printf(" Propulsor 1: %d         | Propulsor 2: %d\n", PROPULSOR1, PROPULSOR2);
        printf(" Fechamento Cabine: %d   | Pressao O2: %d\n", FECHAMENTODECABINE, PRESSAOOXIGENIO);

        printf("\n [STATUS DOS SUBSISTEMAS ATIVOS]\n");
        printf(" -> Resfriamento LED: %d\n", RESFRIAMENTO_LED);
        printf(" -> Propulsor 1 Saida: %d\n", PROPULSOR1_SAIDA);
        printf(" -> Propulsor 2 Saida: %d\n", PROPULSOR2_SAIDA);

        printf("\n [DIAGNOSTICO E TOMADA DE DECISAO]\n");

        if (alerta_sustentabilidade) {
            printf(" [!] ALERTA DE SUSTENTABILIDADE [!]\n");
            printf(" - CAUSA: Consumo de potencia ultrapassou a geracao renovavel.\n");
            printf(" ACAO: Despriorizando modulos nao essenciais para preservar bateria.\n");
        }

        if (ALERTA_CIRCUITO) {
            printf(" [!] ALERTA CRITICO DOS SISTEMAS LOGICOS [!]\n");
            if (ENERGIA && COMUNICACAO)
                printf(" - CAUSA: Anomalia no barramento Energia/Comunicacao.\n");
            if (RESFRIAMENTO && TEMPERATURACRITICA)
                printf(" - CAUSA: Risco de colapso termico detectado.\n");
            if (PROPULSOR1 && PROPULSOR2)
                printf(" - CAUSA: Conflito de ignicao simultanea nos propulsores.\n");
            if (FECHAMENTODECABINE || PRESSAOOXIGENIO)
                printf(" - CAUSA: Comprometimento de suporte a vida ou vedacao.\n");
            printf(" ACAO: Iniciando protocolo de contencao de hardware.\n");
        }

        if (!alerta_sustentabilidade && !ALERTA_CIRCUITO) {
            printf(" - STATUS NOMINAL: Sistemas operando perfeitamente e energia superavitaria.\n");
        }
        printf("====================================================\n");
        Sleep(1500);
    }

    return 0;
}
