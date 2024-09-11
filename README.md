# Tarefas de Programação

Este repositório contém soluções para diversas tarefas de programação. Cada tarefa é implementada em um arquivo Python separado.

## Tarefas

### Tarefa 1: Sequência de Fibonacci

Este programa verifica se um número pertence à sequência de Fibonacci.

**Arquivo:** `fibonacci.py`

**Como Executar:**
```sh
python fibonacci.py
Tarefa 2: Contar Letras 'a' em uma String
Este programa conta a quantidade de letras 'a' (maiúsculas ou minúsculas) em uma string.

Arquivo: contar_letras_a.py

Como Executar:

python contar_letras_a.py
Tarefa 3: Valor da Variável SOMA
Este trecho de código calcula o valor da variável SOMA após um loop.

Arquivo: Não há arquivo específico, a análise está documentada aqui.

Tarefa 4: Descubra a Lógica e Complete o Próximo Elemento
A lógica para completar as sequências está documentada aqui.

Tarefa 5: Descobrir Qual Interruptor Controla Qual Lâmpada
A solução para descobrir qual interruptor controla qual lâmpada está documentada aqui.

Como Executar os Programas
Clone o Repositório:
git clone https://github.com/seu-usuario/tarefas.git
cd tarefas
Execute os Programas:
Para verificar se um número pertence à sequência de Fibonacci:
python fibonacci.py
Para contar letras 'a' em uma string:
python contar_letras_a.py
Contribuição
Sinta-se à vontade para contribuir com melhorias ou novas tarefas. Abra uma issue ou envie um pull request.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Email: seu-email@example.com
GitHub: seu-usuario

### Estrutura do Repositório

Certifique-se de que a estrutura do seu repositório esteja organizada da seguinte forma:
tarefas/ │ ├── fibonacci.py ├── contar_letras_a.py ├── README.md └── LICENSE


### Código dos Programas

#### `fibonacci.py`

```python
def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

numero = int(input("Informe um número: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
contar_letras_a.py
def contar_letras_a(string):
    count = 0
    for char in string:
        if char.lower() == 'a':
            count += 1
    return count

string = input("Informe uma string: ")
quantidade = contar_letras_a(string)
print(f"A string possui {quantidade} letras 'a'.")
