# Simulador_de_Automatos_Finitos

Este simulador de autômatos foi feito como projeto de Teoria da Computação na [UENP](https://uenp.edu.br/).




- ``Obs: O main.py foi a primeira versão do simulador de autômatos, já o main2.py é uma versão aprimorada do simulador de autômatos.``




## Sobre

Um simulador de autômatos finitos determinísticos e não determinísticos realizado em python. O simulador processa o estado inicial, o(s) estados(s) final(is) e as transições do arquivo_do_automato.aut, que está em formato JSON. Depois processa o arquivo_de_testes.in, que está em formato CSV, e por fim a saída ocorre no arquivo_de_saida.out.



- Exemplo do arquivo JSON ```arquivo_do_automato.aut```

```json
{
    "initial": 0,
    "final" : [7],
    "transitions": [
      {"from": 0, "read": "a", "to": "0" },
      {"from": 0, "read": "b", "to": "0" },
      {"from": 0, "read": "c", "to": "0" },
      {"from": 0, "read": null, "to": "1" },
      {"from": 0, "read": null, "to": "2" },
      {"from": 0, "read": null, "to": "4" },
      {"from": 1, "read": "a", "to": 7 },
      {"from": 2, "read": "b", "to": 3 },
      {"from": 3, "read": "b", "to": 7 },
      {"from": 4, "read": "c", "to": 5 },
      {"from": 5, "read": "c", "to": 6 },
      {"from": 6, "read": "c", "to": 7 }
    ]
}
```

- Exemplo do arquivo CSV de entrada ```arquivo_de_testes.in```

```csv
abcb;0
abbbaba;1
cb;0
ccabac;1
a;0
```

- Exemplo do arquivo CSV de saída ```arquivo_de_saida.out```

```csv
abcb;0;0;0.0011
abbbaba;1;1;0.0013
cb;0;0;0.0013
ccabac;1;1;0.0013
a;0;0;0.0014
```



## Como usar

Para clonar o repositório

```bash
   git clone https://github.com/RafaelTomazGraciano/Simulador_de_Automatos_Finitos.git
```

Abra o terminal na pasta que está o repositório e então digite:

```bash
  python main.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out
```

Ou então digite:

```bash
  python main2.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out
```

