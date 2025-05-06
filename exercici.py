import requests

def buscar_pokeson(nom):
    url = f"https://pokeapi.co/api/v2/pokemon/{nom.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dades = resposta.json()
        nom_pokemon = dades['name']
        altura = dades['height']
        pes = dades['weight']
        numero = dades['id']
        tipus = dades['types']
        habilitats = dades['abilities']
        imatge = dades['sprites']['front_default']

        print(f"\nNom: {nom_pokemon}")
        print(f"Número Pokédex: {numero}")
        print(f"\nAlçada: {altura} dm")
        print(f"Pes: {pes} hg")

        
        print("\nTipus:")
        for t in tipus:
            tipus_nom = t['type']['name']
            print(f"- {tipus_nom}")
        
        print("\nHabilitats:")
        for hab in habilitats:
            habilitat = hab['ability']['name']
            print(f"- {habilitat}")

        print(f"\nImatge: {imatge}")

    else:
        print("No s'ha trobat aquest Pokémon. Comprova el nom.")

nom_poke = input("Introdueix el nom d'un Pokémon: ")
buscar_pokeson(nom_poke)
