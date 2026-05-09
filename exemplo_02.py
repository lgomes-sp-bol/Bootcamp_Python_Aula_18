import requests
from pydantic import BaseModel, ConfigDict


class PokemonSchema(BaseModel):
    name: str
    type: str

    model_config = ConfigDict(from_attributes=True)


def pegar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()

    data_types = data["types"]
    types_list = []

    for type_info in data_types:
        types_list.append(type_info["type"]["name"])

    types = ", ".join(types_list)

    return PokemonSchema(
        name=data["name"],
        type=types
    )

if __name__ == "__main__":
    print(pegar_pokemon(6))
    print(pegar_pokemon(10))
    print(pegar_pokemon(13))
    print(pegar_pokemon(25))
    print(pegar_pokemon(72))