# Tarefas de Programação

Este repositório contém soluções o Desafio Target. Abaixo estão as descrições das tarefas e como executar os programas.

# Tarefa 1:
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


## Solução para a Tarefa 1: Sequência de Fibonacci

### Descrição
Este programa verifica se um número pertence à sequência de Fibonacci. A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.

### Como Executar
1. Clone o repositório:
   ```sh
   git clone https://github.com/carolyneoliverr/Desafio-Target.git
2. Navegue até o diretório do projeto:
cd Desafio-Target
3.Execute o programa:
python fibonacci.py

Insira um número quando solicitado.

# Tarefa 2: 
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

## Solução para a Tarefa 2: Contar Letras 'a' em uma String
### Descrição
Este programa conta a quantidade de letras 'a' (maiúsculas ou minúsculas) em uma string fornecida pelo usuário.

### Como Executar
1. Clone o repositório:
   ```sh
   git clone https://github.com/carolyneoliverr/Desafio-Target.git
2. Navegue até o diretório do projeto:
cd Desafio-Target
3. Execute o programa: 
python contar_letras_a.py


Insira uma string quando solicitado.

# Tarefa 3:
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

## Solução para a Tarefa 3: Valor da Variável SOMA
### Descrição
Este programa calcula o valor da variável SOMA após executar um loop específico.

### Como Executar
1. Clone o repositório:
   ```sh
   git clone https://github.com/carolyneoliverr/Desafio-Target.git
2. Navegue até o diretório do projeto:
cd Desafio-Target
3. Execute o programa:
python soma.py

# Tarefa 4:
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____

## Solução para a Tarefa 4: Descubra a Lógica e Complete o Próximo Elemento
### Descrição
Esta tarefa envolve descobrir a lógica de várias sequências numéricas e completar o próximo elemento.

Soluções:

a) 1, 3, 5, 7, 9 (a sequência é de números ímpares)

b) 2, 4, 8, 16, 32, 64, 128 (a sequência é de potências de 2)

c) 0, 1, 4, 9, 16, 25, 36, 49 (a sequência é de quadrados perfeitos: 0^2, 1^2, 2^2, 3^2, ...)

d) 4, 16, 36, 64, 100 (a sequência é de quadrados dos números pares: 2^2, 4^2, 6^2, 8^2, ...)

e) 1, 1, 2, 3, 5, 8, 13 (a sequência de Fibonacci)

f) 2, 10, 12, 16, 17, 18, 19, 200 (a sequência não apresenta uma lógica clara, mas se considerarmos que a sequência é de números crescentes com um salto inicial, podemos considerar que o próximo número seja 200)


# Tarefa 5: 
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

## Solução para a Tarefa 5: Descobrir Qual Interruptor Controla Qual Lâmpada
### Descrição
Esta tarefa envolve descobrir qual interruptor controla qual lâmpada em duas idas até a sala das lâmpadas.

Solução:

Para descobrir qual interruptor controla qual lâmpada em duas idas, você pode seguir estes passos:

Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.

Desligue o primeiro interruptor e ligue o segundo interruptor.

   Vá até a sala das lâmpadas:
   A lâmpada que estiver acesa é controlada pelo segundo interruptor.
   A lâmpada que estiver quente (mas não acesa) é controlada pelo primeiro interruptor.
   A lâmpada que estiver fria e apagada é controlada pelo terceiro interruptor.
