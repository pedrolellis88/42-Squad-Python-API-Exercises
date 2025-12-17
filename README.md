42 Squad Python API Exercises

This project has been created as part of the 42 curriculum by <pdiniz-l>

Description

This repository contains three small Python scripts that practice:

Consuming a public REST API (PokeAPI) to fetch Pokémon data.

Authenticating and consuming the 42 Intra API to list project progress.

Writing structured data into Google Sheets using a Service Account.

Scripts included:

exercicio1.py: fetches and formats Pokémon information from PokeAPI.

exercicio2.py: authenticates in the 42 API and prints your projects progress.

exercicio_bonus.py: uses exercicio1.py + Google Sheets API to append Pokémon data into a spreadsheet.

Instructions
Prerequisites

Python 3.10+ recommended

pip available

Install dependencies
pip install requests gspread google-auth

How to run
1) exercicio1.py — Pokémon info (PokeAPI)

What it does:

Asks for a Pokémon name

Queries:

https://pokeapi.co/api/v2/pokemon/<name>

https://pokeapi.co/api/v2/pokemon-species/<name>

Prints name, generation, Pokédex number, types, weight (kg/lbs), and an English description.

Run:

python3 exercicio1.py

Example output (format may vary):

Name: Pikachu
Generation: generation-i
Number in Pokédex: 25
Type: Electric
Weight: 6.0kg | 13.23lbs
Description: ...

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

export FT42_UID="your_uid"
export FT42_SECRET="your_secret"
export FT42_LOGIN="pdiniz-l"
python3 exercicio2.py


(If your current script uses constants inside the file, replace them with os.getenv(...) before committing.)

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

python3 exercicio_bonus.py


Expected sheet columns appended:

Name

Generation

Pokédex number

Types

Weight (kg)

Weight (lbs)

Description

Resources

PokeAPI documentation: https://pokeapi.co/docs/v2

42 Intra API docs: https://api.intra.42.fr/apidoc

gspread docs: https://docs.gspread.org/

Google Service Accounts: https://cloud.google.com/iam/docs/service-account-overview

AI usage

AI assistance was used for:

Explaining API request/response structure and JSON fields.

Improving code readability and formatting.

Identifying security issues (secrets in code) and suggesting safer patterns (environment variables, .gitignore).

Library / Module description (required)

Although this repository is composed of scripts, exercicio1.py effectively acts as a reusable module.

exercicio1.py

Public function

get_pokemon_info(pokemon_name: str) -> dict | None

Behavior

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
