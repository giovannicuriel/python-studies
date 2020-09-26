# Módulo `dis`

Este é um exemplo de como o módulo `dis` pode ajudar o desenvolvimento de
aplicações com melhor desempenho. Lembre-se de que as conclusões tiradas aqui
são válidas apenas para o CPython.

## O que este projeto é

Este projeto tem o intuito de analisar várias implementações que resolvem um
mesmo problema (formatação de CPF) a fim de analisar seu desempenho. Para ter
uma ideia do que está acontecendo e onde podemos melhorar o código, vamos ver
qual é a saída do descompilador(1) e verificar se há alguma instrução que pode
ser removida ou substituída.

## Como executar

É simples. Você irá precisar de:

- pipenv
- Python 3.8

Ative o ambiente virtual e instale as dependências (não são muitas) com:

```shell
pipenv shell
pipenv install
```

Para executar os exemplos:

```shell
python3 ./main.py 1 2 3 4
```

Temos 7 funções de exemplo, cada uma das entradas seleciona uma das funções.
Veja [aqui](./cpf_utils.py) quais são as funções.

## Notas

(1) Desculpem, pessoas, não consigo misturar inglês e português quando há mais
um claramente um termo preciso em português.

Haverá um post em um determinado blog de uma empresa GPTW sendo preparado por
mim \o/ a respeito do módulo dis. Aguardem.
