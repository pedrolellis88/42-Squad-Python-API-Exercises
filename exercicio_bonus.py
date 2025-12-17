import gspread
from google.oauth2.service_account import Credentials
from exercicio1 import get_pokemon_info
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(
    "google_sheets_credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open("Pokémon Database").sheet1
pokemon_name = input("Enter Pokémon name: ").strip()
info = get_pokemon_info(pokemon_name)
if not info:
    print("Pokémon not found.")
    exit()
sheet.append_row([
    info["name"],
    info["generation"],
    info["pokedex_number"],
    info["types"],
    info["weight_kg"],
    info["weight_lbs"],
    info["description"]
])
print("Pokémon added to Google Sheets successfully!")
