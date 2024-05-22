import json
import csv
import time
import sys


if len(sys.argv) != 4: #Trantando os arquivos de entrada
    print("Use: python main.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out")
    sys.exit(1)


def delta(q, a, transicoes):#Função delta que executa as transicoes do automato
    resultados = []
    for transicao in  transicoes:
        if transicao['from'] == q and transicao['read'] == a or transicao['read'] == None:
            resultados.append(transicao['to'])
    return resultados


def deterministico(dadosJson):#Verifica se o automato e deterministico ou nao deterministico
    estados = set()
    transicoes = set() 
    for transicao in dadosJson['transitions']:
        estados.add(transicao['from'])
        transicao_atual = (transicao['from'], transicao['read'])
        if transicao_atual in transicoes:
            return False 
        transicoes.add(transicao_atual)
    return True

def remover_duplicatas(lista):
    return list(dict.fromkeys(lista))

#inicia contar o tempo
inicio_tempo = time.perf_counter() #Inicia a contar o tempo

# Lendo JSON .aut
arquivo_json = open(sys.argv[1]) 
 
# retorna o JSON 
dadosJson = json.load(arquivo_json) 

#definindo os estados
estadoInicial = dadosJson['initial']
estadoFinal = [(dadosJson['final'])]
transicoes = dadosJson['transitions']

with open(sys.argv[3], 'w', newline='') as arquivo_out: #criando arquivo out
    with open(sys.argv[2], 'r') as arquivo_in: #lendo arquivo in
        leitor = csv.reader(arquivo_in, delimiter = ';')
        for linha in leitor: #Lendo arquivo CSV .in
            estadosAtuais = [estadoInicial]
            palavra = linha[0] 
            caracteres = list(palavra) #separando a palavra por caracteres
            #print(caracteres)
            estados = [] #estados do automato para cada palavra
            for caractere in caracteres:
                novos_estados = [] #novos estados para cada caractere
                for estado_atual in estadosAtuais:
                    novos_estados.extend(delta(estado_atual, caractere, transicoes))
                estadosAtuais = novos_estados #os estadosAtuais recebe os novos_estados
                estados.append(remover_duplicatas(estadosAtuais))
                if estadosAtuais == -1:
                    break
            if deterministico(dadosJson) == True: 
                for estado in estados: #Verificando se o automato chegou no estado final para automato deterministico
                    for final in estadoFinal:
                        if final in estado:
                            resultado_obtido = 1
                        else:
                            resultado_obtido = 0
            else:
                encontrou_final = False
                for estado in estados: #Verificando se o automato chegou no estado final para automato nao deterministico
                    for final in estadoFinal: 
                        if final in estado:
                            resultado_obtido = 1
                            encontrou_final = True
                            break  # Interrompe o loop interno
                        else:
                            resultado_obtido = 0
                    if encontrou_final:
                        break  # Interrompe o loop externo 
            #Escrevendo arquivo out
            escritor = csv.writer(arquivo_out, delimiter = ';')
            fim_tempo = time.perf_counter() 
            tempo = fim_tempo - inicio_tempo #calcula o tempo
            tempo = f"{tempo:.4f}"
            escritor.writerow([linha[0], linha[1], resultado_obtido, tempo])
    
