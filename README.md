Nome dos Integrantes  e RM's
Enrico Marinho de Aquino RM569338
Fernando Lobato Rodrigues RM569377
Manoel da Silva Ferreira RM572045








Para acessar a a documentação, clicar em "view raw" quando acessar a página da mesma, caso não de certo, a mesma documentação vai estar alocada abaixo:









DSA-GS
Explicação do código:
O sistema desenvolvido usa um vetor chamado leituras[], responsável por armazenar objetos que contém três atributos principais: temperatura, energia e comunicação. Cada vez que o usuário insere informações, esses valores são registrados nesse vetor, permitindo que o sistema mantenha um histórico das leituras realizadas (mais tarde usada para a função HistoricoDasLeituras().
A inserção de dados para simulação do painel ocorre por meio da função InserirDados(), que solicita ao usuário, através do prompt(), com auxilio das funções parseFloat para temperatura e energia e parseInt para a comunicação, dessa forma garantindo a entrada correta de dados do usuário, os valores de temperatura, energia e comunicação. Esses dados são encapsulados em um objeto e adicionados ao vetor de leituras.
As condições do sistema são verificadas utilizando estruturas condicionais if. O programa avalia se a temperatura ultrapassa 80 °C, se a energia está abaixo de 20% ou se há falha na comunicação (valor igual a 0). Cada uma dessas situações gera alertas específicos para o usuário, garantindo que problemas sejam identificados rapidamente.
Na etapa de análise, a função ExecutarAnalise() percorre a última leitura registrada e cria uma lista de problemas encontrados. Caso não haja falhas, o sistema informa que está estável, em destaque verde, caso contrário, apresenta os problemas em destaque vermelho, facilitando a visualização.



O histórico das leituras é construído pela função HistoricoDasLeituras(), que utiliza um laço de repetição for para percorrer o vetor(leituras[]) e montar uma tabela em HTML. Essa tabela exibe todas as leituras realizadas, permitindo ao usuário acompanhar a evolução dos dados ao longo do tempo
O encerramento do sistema é feito pela função EncerrarSistema(), que limpa o vetor de leituras e mostra uma mensagem indicando que o sistema foi finalizado. Isso garante que os dados anteriores não interfiram em novas execuções.
Extra: 
Foi projetada como um extra simples uma função chamada condicoes(), representada pelo botão condicoes() criada para exibir as condições do sistema exibindo as condições e repostas do sistema:
Temperatura maior que 80 → Superaquecimento
Energia menor que 20 → Economia de energia
Comunicação = 0 → Falha na comunicação
Comunicação = 1 → Comunicação normal
Criada caso o usuário queira verificar as condições e se o sistema está funcionando.
Conclui-se que o sistema atende a todos os requisitos solicitados, utilizando estrutura de dados, condicionais e laços de repetição para simular um painel de controle funcional. Além disso, a função extra de verificação das condições reforça a usabilidade e clareza para o usuário.




