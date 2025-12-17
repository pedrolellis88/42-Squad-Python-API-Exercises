import requests


def get_pokemon_info(pokemon_name: str) -> dict | None:
    pokemon_name = pokemon_name.lower()
    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    url_species = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}"
    response_all = requests.get(url_pokemon)
    response_species = requests.get(url_species)
    if response_all.status_code != 200 or response_species.status_code != 200:
        return None
    data_all = response_all.json()
    data_species = response_species.json()
    name = data_all["name"].capitalize()
    weight_kg = data_all["weight"] / 10
    weight_lbs = round(data_all["weight"] * 11 / 50, 2)
    types = " & ".join(
        t["type"]["name"].capitalize()for t in data_all["types"])
    generation = data_species["generation"]["name"]
    pokedex_number = data_species["pokedex_numbers"][0]["entry_number"]
    info = ""
    for entry in data_species["flavor_text_entries"]:
        if entry["language"]["name"] == "en":
            info = entry["flavor_text"].replace("\n", " ").replace("\f", " ")
            break
    return {
        "name": name,
        "generation": generation,
        "pokedex_number": pokedex_number,
        "types": types,
        "weight_kg": weight_kg,
        "weight_lbs": weight_lbs,
        "description": info
    }


if __name__ == "__main__":
    pokemon = input("Enter Pokémon name: ").strip()
    info = get_pokemon_info(pokemon)
    if not info:
        print("Pokémon not found")
        exit()
    print("\n========================")
    print("Pokémon Info")
    print("========================")
    print(f"Name: {info['name']}")
    print(f"Generation: {info['generation']}")
    print(f"Number in Pokédex: {info['pokedex_number']}")
    print(f"Type: {info['types']}")
    print(f"Weight: {info['weight_kg']}kg | {info['weight_lbs']}lbs")
    print(f"Description: {info['description']}")
    print("========================")
