from pydantic import BaseModel, ConfigDict

class PokemonSchema(BaseModel):
    name: str
    type: str

    model_config = ConfigDict(from_attributes=True)