# App de Finanças Pessoais

Este programa permite registrar receitas e despesas, armazenando os dados em um arquivo JSON.
Também é possível visualizar o extrato, gerar um relatório com saldo e totais por categoria e exportar os lançamentos para um arquivo de texto.

## Como rodar

bash
python financas.py


## Funcionalidades

- Registrar: adiciona uma receita ou despesa com data, valor, categoria e descrição.
- Extrato: mostra todos os lançamentos cadastrados.
- Relatório: calcula o total de receitas, despesas, saldo e o total por categoria.
- Exportar: salva todos os lançamentos em um arquivo `relatorio.txt`.
- Sair: encerra o programa.
(NESSA PARTE DE FUNCIONAR O CODIGO COLOQUE NA ABA DO PYCHARM DO LANCAMENTOS.JSON E RELATORIO.TXT; (SEMPRE COLOQUE NO COMEÇO ANTES DE RODAR O FINANCIAS.PY COLOQUE [] ISSO NOS LANCAMENTOS.JSON E RELATORIO.TXT)).
## Funções implementadas

Este projeto foi desenvolvido utilizando a estrutura principal do programa (`while`) e blocos `if/elif`, sem a criação de funções separadas.

| Estrutura | Responsabilidade |
|-----------|------------------|
| Carregamento do JSON | Lê os lançamentos salvos no arquivo lancamentos.json. |
| Registro de lançamento | Solicita os dados do usuário e salva um novo lançamento. |
| Exibição do extrato | Lista todos os lançamentos cadastrados. |
| Geração de relatório | Calcula receitas, despesas, saldo e totais por categoria. |
| Exportação | Cria o arquivo `relatorio.txt` com os lançamentos. |

## Tecnologias usadas

- Python 3
- json

## O que aprendi

Durante este projeto aprendi a trabalhar com arquivos JSON para salvar informações de forma permanente. Também pratiquei o uso de listas, dicionários, estruturas de repetição e condicionais em Python. A parte mais difícil foi organizar os cálculos do relatório e garantir que os dados fossem salvos corretamente. Se fosse começar novamente, criaria funções para deixar o código mais organizado e fácil de manter.
