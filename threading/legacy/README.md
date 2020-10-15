# Servidor legado

Este componente representa o servidor legado com uma camada intermediária que
implementa uma API HTTP.

Ele é um servidor de exemplo que recebe uma requisição para a criação de um
usuário e, toda vez que ele recebe uma requisição para verificação se o
processamento do usuário está pronto, ele verifica se já se passou um
determinado tempo e, em caso afirmativo, uma decisão é tomada sobre o sucesso
do cadastro ou não. A chance de dar certo é 50%.

## Como executar

O Flask já deve estar instalado no seu ambiente virtual, se você já tiver
executado o `pipenv install`. Neste caso, basta iniciar a aplicação:

```bash
python3 ./app.py
```

Caso tudo esteja correto, o log inicial do flask deve aparecer no console:

```text
 * Serving Flask app "legacy-server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:3000/ (Press CTRL+C to quit)
```

Pronto! Servidor de pé, vamos enviar algumas requisições:

```bash
$ curl 0:3000/registration -H 'content-type:application/json' -d '{"name": "José da Silva", "age": 30}' -X POST
{"message":"ok","userid":"17b0030e-9fd8-406a-98ca-0cd5e21c4348"}
$ curl 0:3000/registration/17b0030e-9fd8-406a-98ca-0cd5e21c4348
{"message":"ok","user":{"age":30,"name":"Jos\u00e9 da Silva","process_status":"not-ready","user_id":"17b0030e-9fd8-406a-98ca-0cd5e21c4348"}}
$ curl 0:3000/registration/17b0030e-9fd8-406a-98ca-0cd5e21c4348
{"message":"ok","user":{"age":30,"name":"Jos\u00e9 da Silva","process_status":"ok","user_id":"17b0030e-9fd8-406a-98ca-0cd5e21c4348"}}
```

## Experimento: injeção de dependências

Decidi, para a implementação deste serviço, usar uma abordagem que venho
empregando nos componentes que ando desenvolvendo em NodeJS. Eu defino métodos
de construção de classes os quais recebem a lista de dependências. As classes
geradas vão construir objetos que utilizam estas dependências, por conta do
contexto onde foram criadas. Assim é possível se criar os controladores,
roteadores e repositórios de forma imutável, ou seja, uma vez definidas as
dependências e o seu comportamento, não é possível alterá-las em tempo de
execução (ou pelo menos não é esta a intenção).
