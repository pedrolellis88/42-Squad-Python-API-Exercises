42 Squad Python API Exercises

This project has been created as part of the 42 curriculum by <pdiniz-l>

Description

This repository contains three small Python scripts that practice:

-Consuming a public REST API (PokeAPI) to fetch Pokémon data.
-Authenticating and consuming the 42 Intra API to list project progress.
-Writing structured data into Google Sheets using a Service Account.

Scripts included:

-exercicio1.py: fetches and formats Pokémon information from PokeAPI.
-exercicio2.py: authenticates in the 42 API and prints your projects progress.
-exercicio_bonus.py: uses exercicio1.py + Google Sheets API to append Pokémon data into a spreadsheet.

Instructions
Prerequisites

-Python 3.10+ recommended
-pip available

Install dependencies
```bash
pip install requests gspread google-auth
```
How to run
1) exercicio1.py — Pokémon info (PokeAPI)

What it does:

Asks for a Pokémon name
Queries:

https://pokeapi.co/api/v2/pokemon/<name>
https://pokeapi.co/api/v2/pokemon-species/<name>

Prints name, generation, Pokédex number, types, weight (kg/lbs), and an English description.

Run:

```bash
python3 exercicio1.py
Enter Pokémon name:
```
Example output (format may vary):
```text
Name: Pikachu
Generation: generation-i
Number in Pokédex: 25
Type: Electric
Weight: 6.0kg | 13.23lbs
Description: ...
```
2) exercicio2.py — 42 projects progress (42 Intra API)

What it does:

Requests an OAuth token with client_credentials

Calls:
GET https://api.intra.42.fr/v2/users/<LOGIN_42>/projects_users

Paginates results and prints a table:
project name | status | grade

Security note (important)

Do not hardcode your client_secret in the file, and do not commit it to Git.
Recommended approach: use environment variables.

Example (Linux/macOS):
```bash
export FT42_UID="your_uid"
export FT42_SECRET="your_secret"
export FT42_LOGIN="pdiniz-l"
python3 exercicio2.py
```

3) exercicio_bonus.py — Append Pokémon data to Google Sheets

What it does:

Authenticates with a Google Service Account JSON file

Opens the spreadsheet (by name) and appends a row with Pokémon info coming from get_pokemon_info

Setup steps

Create a Google Cloud project + enable Google Sheets API and Google Drive API

Create a Service Account and download the JSON credentials file

Put it in the project root (example name):


Share your spreadsheet with the service account email (Editor permission)

Run:
```bash
python3 exercicio_bonus.py
```
Expected sheet columns appended:

Name
Generation
Pokédex number
Types
Weight (kg)
Weight (lbs)

Description

Resources

-PokeAPI documentation: https://pokeapi.co/docs/v2
-42 Intra API docs: https://api.intra.42.fr/apidoc
-gspread docs: https://docs.gspread.org/
-Google Service Accounts: https://cloud.google.com/iam/docs/service-account-overview

Library / Module description (required)

Although this repository is composed of scripts, exercicio1.py effectively acts as a reusable module.

exercicio1.py

Public function:

get_pokemon_info(pokemon_name: str) -> dict | None

Behavior:

Normalizes the Pokémon name
Fetches data from PokeAPI endpoints (pokemon + pokemon-species)
Returns None if the Pokémon does not exist or the request fails
Otherwise returns a dict with:

name (str)

generation (str)

pokedex_number (int)

types (str, formatted like "Grass & Poison")

weight_kg (float)

weight_lbs (float)

description (str, English flavor text)

Português:

Este projeto foi criado como parte do currículo da 42 por <pdiniz-l>

Descrição

Este repositório contém três pequenos scripts em Python que praticam:

-Consumir uma API REST pública (PokeAPI) para buscar dados de Pokémon.
-Autenticar e consumir a API da 42 Intra para listar o progresso dos projetos.
-Escrever dados estruturados no Google Sheets usando uma Service Account.

Scripts incluídos:

-exercicio1.py: busca e formata informações de Pokémon a partir da PokeAPI.
-exercicio2.py: autentica na API da 42 e imprime o progresso dos seus projetos.
-exercicio_bonus.py: usa exercicio1.py + Google Sheets API para adicionar dados de Pokémon em uma planilha.

Instruções
Pré-requisitos

-Python 3.10+ recomendado
-pip disponível

Instalar dependências
```bash
pip install requests gspread google-auth
```

Como executar

exercicio1.py — Informações do Pokémon (PokeAPI)

O que faz:

Pede o nome de um Pokémon
Consultas:

https://pokeapi.co/api/v2/pokemon/
<name>
https://pokeapi.co/api/v2/pokemon-species/
<name>

Imprime nome, geração, número na Pokédex, tipos, peso (kg/lbs) e uma descrição em inglês.

Executar:
```bash
python3 exercicio1.py
Enter Pokémon name:
```

Exemplo de saída (o formato pode variar):
```text
Name: Pikachu
Generation: generation-i
Number in Pokédex: 25
Type: Electric
Weight: 6.0kg | 13.23lbs
Description: ...
```

exercicio2.py — Progresso dos projetos na 42 (42 Intra API)

O que faz:

Solicita um token OAuth com client_credentials

Chama:
GET https://api.intra.42.fr/v2/users/
<LOGIN_42>/projects_users

Faz paginação dos resultados e imprime uma tabela:
nome do projeto | status | nota

Nota de segurança (importante)

Não coloque seu client_secret diretamente no arquivo e não faça commit dele no Git.
Abordagem recomendada: usar variáveis de ambiente.

Exemplo (Linux/macOS):
```bash
export FT42_UID="your_uid"
export FT42_SECRET="your_secret"
export FT42_LOGIN="pdiniz-l"
python3 exercicio2.py
```

exercicio_bonus.py — Adicionar dados de Pokémon ao Google Sheets

O que faz:

Autentica com um arquivo JSON de Service Account do Google

Abre a planilha (pelo nome) e adiciona uma linha com informações do Pokémon vindas de get_pokemon_info

Passos de configuração

Criar um projeto no Google Cloud + habilitar Google Sheets API e Google Drive API

Criar uma Service Account e baixar o arquivo JSON de credenciais

Colocar no diretório raiz do projeto (nome de exemplo):

Compartilhar sua planilha com o e-mail da service account (permissão de Editor)

Executar:
```bash
python3 exercicio_bonus.py
```

Colunas esperadas adicionadas na planilha:

Name
Generation
Pokédex number
Types
Weight (kg)
Weight (lbs)

Description

Recursos

-PokeAPI documentation: https://pokeapi.co/docs/v2

-42 Intra API docs: https://api.intra.42.fr/apidoc

-gspread docs: https://docs.gspread.org/

-Google Service Accounts: https://cloud.google.com/iam/docs/service-account-overview

Descrição da biblioteca / módulo (obrigatório)

Embora este repositório seja composto por scripts, o exercicio1.py efetivamente atua como um módulo reutilizável.

exercicio1.py

Função pública:

get_pokemon_info(pokemon_name: str) -> dict | None

Comportamento:

Normaliza o nome do Pokémon
Busca dados nos endpoints da PokeAPI (pokemon + pokemon-species)
Retorna None se o Pokémon não existir ou se a requisição falhar
Caso contrário, retorna um dict com:

name (str)

generation (str)

pokedex_number (int)

types (str, formatado como "Grass & Poison")

weight_kg (float)

weight_lbs (float)

description (str, texto de flavor em inglês)
