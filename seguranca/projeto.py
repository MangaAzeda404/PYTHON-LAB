"""PYTHON LAB 03 — exemplos didáticos; não use estas transformações para proteger senhas reais."""
ALFABETO = "phqgiumeaylnofdxjkrcvstzwb"

def transformar_digitos(base):
    if any(d not in "0123456789" for d in base):
        raise ValueError("Use somente dígitos ASCII de 0 a 9.")
    senha_final = ""
    for digito in base:
        senha_final += str(int(digito) + 2)
    return senha_final

def proteger_nome(nome):
    if any(not ("a" <= c <= "z") for c in nome):
        raise ValueError("Use apenas letras minúsculas de a a z.")
    return "".join(ALFABETO[ord(c) - ord("a")] for c in nome)

def gerar_token(palavra):
    token_final = "SEC_" + palavra
    return token_final

def codifica(senha):
    senha_criptografada = ""
    for letra in senha:
        if "a" <= letra <= "z":
            posicao = ord(letra) - ord("a")
            senha_criptografada += ALFABETO[posicao]
        else:
            senha_criptografada += letra
    return senha_criptografada

def criar_hash(texto):
    valor = 0
    for letra in texto:
        valor = valor + ord(letra)
    return valor

calcula_hash = criar_hash

def main():
    opcoes = {"1": ("Transformar dígitos", transformar_digitos), "2": ("Proteger nome", proteger_nome), "3": ("Gerar token", gerar_token), "4": ("Codificar texto", codifica), "5": ("Somar códigos Unicode", criar_hash)}
    print("PYTHON LAB 03 | Strings, criptografia e hash\nExemplos didáticos, sem segurança para senhas reais.")
    while True:
        for chave, (nome, _) in opcoes.items():
            print(f"{chave} — {nome}")
        escolha = input("0 — Sair\nEscolha: ").strip()
        if escolha == "0":
            break
        if escolha not in opcoes:
            print("Escolha uma opção válida.")
            continue
        try:
            print("Resultado:", opcoes[escolha][1](input("Texto: ")))
        except ValueError as erro:
            print(erro)

if __name__ == "__main__":
    main()
