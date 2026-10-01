# PYTHON LAB — Fundamentos na prática

Projeto de estudo baseado em exercícios de Python básico: variáveis, strings, números, booleanos, entrada de dados, operadores aritméticos, comparações e condições.

## O que está incluído

- `index.html`, `style.css`, `script.js` e `modules.json`: apresentação interativa. A interface simula os cálculos em JavaScript e mostra o código equivalente em Python; não é um interpretador Python.
- `projeto.py`: programa Python com menu e validação de entradas, sem dependências externas.
- `python_lab.ipynb`: caderno com os exemplos em Python para Google Colab ou Jupyter.

## Executar Python

Instale Python 3 e execute `python projeto.py` (no Windows, também pode usar `py projeto.py`). Escolha uma opção de 1 a 7; digite 0 para sair. O programa aceita números não negativos, protege a divisão por zero e aceita vírgula ou ponto em campos decimais. As células do notebook são exemplos didáticos independentes: informe entradas numéricas válidas e use ponto decimal.

## Abrir no Google Colab

Acesse https://colab.research.google.com/ e escolha **Arquivo > Fazer upload de notebook**. Envie `python_lab.ipynb` e execute as células. O notebook contém código Python verdadeiro.

## Executar o site localmente

Na pasta do projeto, execute `python -m http.server 8000` e abra http://localhost:8000. O servidor é necessário porque o site carrega `modules.json`.

## Publicar no GitHub

1. Crie um repositório e extraia o ZIP.
2. Envie os arquivos extraídos para a raiz do repositório; não envie apenas o ZIP.
3. O link do repositório permite compartilhar o código.
4. Para publicar a apresentação, ative GitHub Pages em **Settings > Pages**, escolhendo a branch principal e a pasta raiz, se essa opção estiver disponível.
5. Depois da publicação, use a URL exibida pelo GitHub Pages. Não confunda essa URL com o endereço do repositório.

## Experiências e resultados iniciais

| Experiência | Conceito | Resultado |
|---|---|---|
| Esmaltes | Variáveis e soma | 37 esmaltes |
| Pontuação de Pedro | Multiplicação e soma | 55 pontos |
| Jogos entre amigos | Divisão inteira e resto | 4 por amigo, sobram 3 |
| Idade futura | input, int e f-string | 21 anos após 5 anos |
| Triângulo | float e divisão | 7,5 unidades² |
| Carrinho | if, else e <= | 20 kg: itens cabem |
| Cinema | Sequência e condição | 100 pessoas: todos entram |

O cinema é considerado vazio. Base e altura usam a mesma unidade. O limite de 20 kg e a capacidade de 100 pessoas incluem a igualdade.

## Decisões do projeto

As questões fornecidas foram usadas como base; o enunciado de entrega disponível não especifica um tema obrigatório. O uso de float em medidas e pesos aceita decimais. O programa completo acrescenta validação para entradas inválidas sem alterar as regras dos exercícios.
