"""PYTHON LAB: sete experiências de Python básico. Execute: python projeto.py."""
import math

def ler_numero(mensagem, inteiro=False, positivo=False):
    while True:
        try:
            texto = input(mensagem).strip().replace(",", ".")
            valor = int(texto) if inteiro else float(texto)
            if not math.isfinite(valor) or valor < 0 or (positivo and valor == 0):
                raise ValueError
            return valor
        except ValueError:
            tipo = "inteiro" if inteiro else "número"
            limite = "positivo" if positivo else "não negativo"
            print(f"Informe um {tipo} {limite} válido.")

def esmaltes():
    esmaltes_azuis = 7
    esmaltes_vermelhos = 18
    esmaltes_brancos = 12
    
    esmaltes_totais = esmaltes_azuis + esmaltes_vermelhos + esmaltes_brancos
    print(f"Luiza tem {esmaltes_totais} esmaltes.")

def pontos():
    corrida = 3
    natacao = 5
    quilometros = ler_numero('Quilômetros corridos: ')
    voltas = ler_numero('Voltas na piscina: ', inteiro=True)
    
    total = corrida * quilometros + natacao * voltas
    print(f"A pontuação total de Pedro é {total:g}")

def jogos():
    total_jogos = ler_numero('Digite o total de jogos: ', inteiro=True)
    numero_amigos = ler_numero('Digite o número de amigos: ', inteiro=True, positivo=True)
    
    if total_jogos < 0 or numero_amigos <= 0:
        print("Informe jogos não negativos e pelo menos um amigo.")
    else:
        jogos_por_amigo = total_jogos // numero_amigos
        resto = total_jogos % numero_amigos
        print(f"Cada amigo recebe {jogos_por_amigo} jogos.")
        print(f"Restam {resto} jogos.")

def idade():
    idade_atual = ler_numero('Digite sua idade atual: ', inteiro=True)
    anos_adicionar = ler_numero('Quantos anos você quer adicionar? ', inteiro=True)
    
    idade_futura = idade_atual + anos_adicionar
    print(f"Daqui a {anos_adicionar} anos, você terá {idade_futura} anos.")

def triangulo():
    base = ler_numero('Digite a base do triângulo: ', positivo=True)
    altura = ler_numero('Digite a altura do triângulo: ', positivo=True)
    
    if base <= 0 or altura <= 0:
        print("A base e a altura devem ser positivas.")
    else:
        area = base * altura / 2
        print(f"A área do triângulo é {area:g}.")

def carrinho():
    peso_item1 = ler_numero('Digite o peso do item 1: ')
    peso_item2 = ler_numero('Digite o peso do item 2: ')
    
    if peso_item1 + peso_item2 <= 20:
        print("Os itens cabem no carrinho.")
    else:
        print("Os itens excedem o peso permitido.")

def cinema():
    total_pessoas = ler_numero('Quantas pessoas estão no grupo? ', inteiro=True)
    
    if total_pessoas <= 100:
        print("Todos podem entrar.")
    else:
        print("O grupo excede a capacidade.")

EXPERIENCIAS = [
    ('Coleção de esmaltes', esmaltes),
    ('Pontuação de Pedro', pontos),
    ('Jogos entre amigos', jogos),
    ('Idade no futuro', idade),
    ('Área do triângulo', triangulo),
    ('Limite do carrinho', carrinho),
    ('Capacidade do cinema', cinema),
]

def main():
    while True:
        print("\nPYTHON LAB — Fundamentos na prática")
        for indice, (titulo, _) in enumerate(EXPERIENCIAS, 1):
            print(f"{indice}. {titulo}")
        print("0. Sair")
        escolha = input("Escolha uma experiência: ").strip()
        if escolha == "0":
            print("Até a próxima!")
            break
        if escolha.isdigit() and 1 <= int(escolha) <= len(EXPERIENCIAS):
            EXPERIENCIAS[int(escolha) - 1][1]()
        else:
            print("Escolha uma opção de 0 a 7.")

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma encerrado.")
