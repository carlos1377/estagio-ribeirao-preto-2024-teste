# Teste Técnico - Estágio Ribeirão Preto 2024

### Pergunta 1

O resultado será 91, conforme calculado no arquivo sum.py
 
### Pergunta 2
 ```python

 def fibonacci(num: int) -> int:
    if num in [0, 1]:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


def is_on_fibonacci_sequence(target: int) -> bool:
    if target == 0:
        return True

    value = 0
    n = 0

    while value < target:
        value = fibonacci(n)

        if value == target:
            return True
        if value > target:
            return False

        n = n + 1
 ```

A resolução completa com exemplos está no arquivo fibonacci.py

### Pergunta 3

- A) 1, 3, 5, 7, *9*
- B) 2, 4, 8, 16, 32, 64, *128*
- C) 0, 1, 4, 9, 16, 25, 36, *49*
- D) 4, 16, 36, 64, *144*
- E) 1, 1, 2, 3, 5, 8, *13*
- F) 2, 10, 12, 16, 17, 18, 19, *20*

### Pergunta 4

Para resolver esse problema, podemos pensar no layout dos interruptores como: Esquerda, Meio e Direita.

Tendo essa definição, podemos ligar o interruptor do meio e o da direita, ir ver quais lampadas estão ligadas e retornar.
Após isso, voltamos e desligamos o interruptor da direita e ligamos o da esquerda, mantendo o do meio ligado.
Assim quando formos ver as lampadas, saberemos que o que permanecer ligado nas duas idas, é o do meio, o que estiver
desligado é o da direita e o que estiver ligado, mas não estava ligado antes era o da esquerda.


### Pergunta 5

```python
def reverse_string(string: str) -> str:
    lista = list(string)
    new = ''

    i = -1
    for _ in range(len(lista)):
        new += lista[i]
        i = i - 1
    return new
```

A resolução completa com exemplo de uso está no arquivo reverter_string.py