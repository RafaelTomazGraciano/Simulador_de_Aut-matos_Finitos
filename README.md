# Simulador_de_Automatos_Finitos

Este simulador de autômatos foi feito como projeto de Teoria da Computação na [UENP](https://uenp.edu.br/).




## Sobre

Um simulador de autômatos finitos determinísticos e não determinísticos realizado em python. O simulador processa o estado inicial, o(s) estados(s) final(is) e as transições do arquivo_do_automato.aut, que está em formato JSON. Depois processa o arquivo_de_testes.in, que está em formato CSV, com uma palavra e o resultado esperado (1 = aceita ou 0 = rejeita), e por fim a saída ocorre no arquivo_de_saida.out onde temos a palavra e o resultado esperado do arquivo_de_testes.in, o resultado obtido pelo simulador de autômatos e o tempo demorado para processamento.


Obs: O main.py foi a primeira versão como simulador de autômatos, já o main2.py é uma versão aprimorada do simulador de autômatos.




## Como usar

Para clonar o repositório

```bash
   git clone https://github.com/RafaelTomazGraciano/Simulador_de_Automatos_Finitos.git
```

Abra o terminal na pasta que está o repositório, então digite:

```bash
  python main.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out
```

Ou então digite:

```bash
  python main2.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out
```

