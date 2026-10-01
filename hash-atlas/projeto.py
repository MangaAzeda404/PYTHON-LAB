"""HASH ATLAS — demonstrações locais e didáticas, sem armazenamento real."""
import itertools

def calcula_hash(senha):
    valor = 0
    for letra in senha:
        valor = valor * 31 + ord(letra)
        valor %= 2**32
    return f"0x{valor:08x}"

calcular_hash = calcula_hash

def buscar_tres_digitos(senha):
    if len(senha) != 3 or any(c not in "0123456789" for c in senha):
        raise ValueError("Use três dígitos ASCII.")
    alvo = calcula_hash(senha)
    for numero, caracteres in enumerate(itertools.product("0123456789", repeat=3), 1):
        tentativa = "".join(caracteres)
        if calcula_hash(tentativa) == alvo:
            return tentativa, numero
    return None, 1000

def main():
    print("HASH ATLAS | Use somente textos fictícios. Hash didático.")
    while True:
        escolha = input("1 Hash | 2 Hexadecimal | 3 Módulo | 4 Cadastro simulado | 5 Login simulado | 6 Busca de 3 dígitos | 0 Sair: ")
        if escolha == "0": break
        try:
            if escolha == "1": print(calcula_hash(input("Texto: ")))
            elif escolha in ("2", "3"):
                n = int(input("Inteiro: ")) % (2**32)
                print(f"{n:08x}" if escolha == "2" else n)
            elif escolha == "4":
                senha_original = input("Texto fictício: ")
                hash_para_salvar = calcular_hash(senha_original)
                banco_de_dados = hash_para_salvar
                print("Cadastro simulado:", banco_de_dados)
            elif escolha == "5":
                hash_banco = calcula_hash(input("Texto fictício cadastrado: "))
                hash_teste = calcula_hash(input("Tentativa: "))
                print("Acesso permitido" if hash_teste == hash_banco else "Hashes diferentes")
            elif escolha == "6": print(buscar_tres_digitos(input("Três dígitos: ")))
            else: print("Escolha uma opção válida.")
        except ValueError as e: print(e)

if __name__ == "__main__": main()
