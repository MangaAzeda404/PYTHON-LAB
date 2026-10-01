# PYTHON LAB 03 — Strings, criptografia e hash

Oito exercícios reunidos em um site responsivo, programa Python e notebook Colab.

## Conteúdo
1. Transformação da senha 1111 em 3333 — alternativa C (I, III e IV).
2. Alfabeto secreto: bia → hap.
3. Retorno de token — A, return token_final.
4. Ordenação do laço de substituição de letras.
5. Caso contrário — A, else:.
6. Propriedade de mão única do hash — B.
7. Acumulação e retorno em criar_hash.
8. ROMA e AMOR — D, colisão no valor 303.

O site mostra explicações de alternativas, permite editar entradas e copiar os códigos. A unidade anterior continua na raiz do repositório.

## Abrir
Site: https://mangaazeda404.github.io/PYTHON-LAB/seguranca/
Código: https://github.com/MangaAzeda404/PYTHON-LAB/tree/main/seguranca

Abra index.html diretamente no navegador ou execute python -m http.server 8000 nesta pasta. O site é autossuficiente e simula a lógica em JavaScript; não executa um interpretador Python.

## Executar
Python 3: python projeto.py. No Google Colab, use Arquivo → Fazer upload de notebook e escolha python_lab_03.ipynb.

## Precisão dos exemplos
ord() retorna um ponto de código Unicode, que coincide com ASCII nos caracteres ASCII. A soma de ord() e a substituição de letras são exemplos didáticos e não protegem senhas reais. O exercício do nome aceita apenas a-z; a codificação com else preserva os outros caracteres. O site usa Array.from e codePointAt para reproduzir a iteração Unicode do Python. Colisão exige textos distintos com a mesma saída. O dicionário de exemplo é o alfabeto secreto fornecido no exercício de Bia.
