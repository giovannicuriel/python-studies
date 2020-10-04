# Threads em Python

Este projeto é um exemplo de como utilizar threads em Python. Nele, tentamos
construir um serviço que lida com um sistema legado que possui características
peculiares de funcionamento. Assim, podemos fazer uso de threads para conseguir
atender a um volume maior de dados

## O que é o projeto

O projeto implementa um serviço que deve fazer requisições a um sistema legado
de cadastro de usuários que possui as seguintes características (qualquer
semelhança com algum evento passado é mera coincidência):

- Sistema API REST HTTP: este sistema demora bastante para concluir um
  cadastro. Na verdade, a API utilizada é oferecida por um serviço
  intermediário que implementa a API REST e reencaminha as requisições para uma
  aplicação escrita em VB6 utilizando um protocolo proprietário (porta TCP
  9998). O último desenvolvedor que conhecia o sistema morreu de desgosto em
  2013. Assim, as requisições são recebidas por este serviço intermediário
  (vamos chamá-lo daqui por diante de "camada de adaptação") e, assim que
  detecta que a requisição é sintaticamente válida, devolve uma mensagem `201`
  significando "ok, recebi sua requisição e ela é válida. O identificador da
  sua requisição é AB583C-X".
- API assíncrona: O cliente que enviou a requisição deve verificar
  continuamente como está o andamento da requisição em um endpoint específico
  para isso, passando o identificador da requisição. Em média, o tempo entre o
  envio da requisição e a recepção do seu identificador é rápido: algo da ordem
  de várias dezenas de milissegundos. No entanto, a resposta positiva do seu
  processamento demora algo da ordem de vários segundos, talvez algumas poucas
  dezenas de segundos (10~20 segundos).
- Tempo total de processamento: O tempo total de processamento de uma
  requisição não parece ser afetado significativamente pelo volume de
  transações, ou seja, se houver poucas unidades ou algumas dezenas de milhares
  de requisições o sistema legado sempre retorna o resultado final entre 10 e
  20 segundos após o envio da requisição.

O nosso serviço deverá receber mensagens via RabbitMQ e encaminhar as
requisições para este serviço. Os resultados com sucesso devem ser armazenados
em uma coleção do MongoDB (atualização de um parâmetro indicando a situação do
cadastro em uma coleção do MongoDB) e os resultados de falha devem ser
encaminhados para uma fila de, ahm, falhas - algo como uma DLQ do SQS.

## Como executar

Como ainda não há código, não há o que executar.
