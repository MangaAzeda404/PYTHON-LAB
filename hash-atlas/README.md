# HASH ATLAS — O caminho da senha

Projeto independente com as oito questões mais recentes.

Site: https://mangaazeda404.github.io/PYTHON-LAB/hash-atlas/

1. Montar a função hash — def → valor = 0 → for → multiplicação e soma → módulo → return
2. Oito dígitos, sempre — A) Módulo 2**32, hexadecimal e zeros à esquerda até 8 dígitos.
3. O papel do módulo — A) Manter o valor dentro de um limite definido de memória.
4. Cadastro na ordem certa — Receber senha → calcular hash → armazenar hash → confirmar
5. Comparar credenciais — B) if hash_tentativa == hash_cadastrado:
6. O que guardar da senha? — B) Apenas I, II e IV.
7. Construir o fluxo de login — Entrada → cálculo do hash → comparação → acesso permitido
8. Encontrar e parar — for → if → print → break

## Executar
Abra index.html no navegador. Python: python projeto.py. No Colab, envie hash_atlas.ipynb e execute as células em ordem.

## Notas de precisão
O hash é didático, sem segurança para senhas reais. Os exemplos de cadastro são variáveis em memória; não há banco, envio ou persistência. A imagem da busca tem inconsistências: o exemplo foi ajustado para três dígitos, nome consistente de função e join() das tuplas. O módulo limita o valor numérico, não o tamanho físico do int Python. O prefixo 0x não conta nos oito dígitos hexadecimais. Nenhum salt foi adicionado, porque os blocos fornecidos não o incluem.
