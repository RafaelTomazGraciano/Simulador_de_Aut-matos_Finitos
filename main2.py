import json
import csv
import time
import sys

if len(sys.argv) != 4:  # Tratando os arquivos de entrada
    print("Use: python main2.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out")
    sys.exit(1)

def main():
    # Inicia contar o tempo
    inicio_tempo = time.perf_counter()

    # Lendo JSON .aut
    with open(sys.argv[1]) as arquivo_json:
        dadosJson = json.load(arquivo_json)
    
    deterministico = e_deterministico(dadosJson)  # Resultado do automato se é determinístico ou não

    # Definindo os estados
    estadoInicial = int(dadosJson['initial'])
    estadoFinal = set(dadosJson['final']) if isinstance(dadosJson['final'], list) else {int(dadosJson['final'])}
    transicoes = dadosJson['transitions']

    with open(sys.argv[3], 'w', newline='') as arquivo_out:  # Criando arquivo out
        escritor = csv.writer(arquivo_out, delimiter=';')

        with open(sys.argv[2], 'r') as arquivo_in:  # Lendo arquivo in
            leitor = csv.reader(arquivo_in, delimiter=';')
            for linha in leitor:  # Lendo arquivo CSV .in
                estadosAtuais = {estadoInicial}
                palavra = linha[0]
                caracteres = list(palavra)  # Separando a palavra por caracteres

                estados = set()
                for caractere in caracteres:
                    novos_estados = set()  # Novos estados para cada caractere
                    for estado_atual in estadosAtuais:
                        novos_estados.update(delta(estado_atual, caractere, transicoes))
                    estadosAtuais = novos_estados
                    estados.update(estadosAtuais.union(novos_estados))
                    #print(estadosAtuais)# Atualizando os estados atuais
                    if not estadosAtuais:
                        break
                #print(estadosAtuais)
                resultado_obtido = 0
                if deterministico == True:
                    if estadoFinal & estadosAtuais:  # Verificando se há interseção entre estados finais e atuais
                        resultado_obtido = 1
                else:
                    if estadoFinal & estados:
                        resultado_obtido = 1  
                # Escrevendo arquivo out
                fim_tempo = time.perf_counter()
                tempo = fim_tempo - inicio_tempo
                tempo = f"{tempo:.4f}"
                escritor.writerow([linha[0], linha[1], resultado_obtido, tempo])


def delta(q, a, transicoes):  # Função delta que executa as transições do automato
    resultados = set()
    for transicao in transicoes:
        if int(transicao['from']) == q and (transicao['read'] == a or transicao['read'] is None):
            resultados.add(int(transicao['to']))
    return resultados

def e_deterministico(dadosJson): #Verifica se o automato e deterministico ou nao deterministico
    estados = set()
    transicoes = set() 
    for transicao in dadosJson['transitions']:
        estados.add(int(transicao['from']))
        transicao_atual = (int(transicao['from']), transicao['read'])
        if transicao_atual in transicoes:
            return False 
        transicoes.add(transicao_atual)
    return True

main()